#include <vector>
#include <cstdio>

using std::vector;

// max. number of pancakes
#define LIMCAKES 1001
// t-value to print stats for
#define T_DEBUG -1

static int t;  // Current case number (for debugging)

// Find the quickest finishing time for pancake config Q.
int optimize(const vector<int> &Q,  // pancake config to optimize
		int Q_max,  // greatest k with Q[k] > 0
		int &time)  // return: best time for Q
{
	// Debug printing
	if (T_DEBUG == t+1) {
		fprintf(stderr, "Q_max: %d, Q[Q_max]: %d\n",
				Q_max, Q[Q_max]);
	}
	/* test small stacks */
	if (Q_max <= 3) {
		time = Q_max;
		return 0;
	}
	if (4 == Q_max) {
		if ((1 == Q[4]) && (0 == Q[3])) {
			// split the 4, then eat twice
			time = 3;
		} else {
			time = 4;
		}
		return 0;
	}
	if (5 == Q_max) {
		if ((1 == Q[5]) && (0 == Q[4])) {
			// split the 5, then eat three times
			time = 4;
		} else {
			time = 5;
		}
		return 0;
	}

	/* test larger stacks by splitting the piles of maximal height */
	vector<int> P;  // new pancake config
	int P_max;  // greatest k with P[k] > 0
	int P_time;  // best time for P

	const int Q_count = Q[Q_max];  // number of maximal piles
	int k;  // split each pile into k parts
	int p, q;  // size of smaller, larger parts
	int count_p;  // number of smaller parts (per pile of Q)
	int count_q;  // number of larger parts (per pile of Q)

	time = Q_max;  // if we don't split, this is the time
	for (k = 2; k < Q_max; ++k) {
		// calculate split of Q_count piles into k parts each
		p = Q_max / k;
		q = p + 1;
		count_q = Q_max % k;
		count_p = k - count_q;
		// Debug printing
		if (T_DEBUG == t+1) {
			fprintf(stderr, "k: %d, p: %d, q: %d, "
					"count_p: %d, count_q: %d\n",
					k, p, q, count_p, count_q);
		}

		// generate new config P with the parts split
		P = Q;
		P[Q_count] = 0;
		P[p] += count_p * Q_count;
		P[q] += count_q * Q_count;
		P_max = 0;
		for (int i = 1; i < Q_max; ++i) {
			if (P[i] > 0) { P_max = i; }
		}
		// Debug printing
		if (T_DEBUG == t+1) {
			fprintf(stderr, "Q_max: %d, P_max: %d, P[P_max]: %d\n",
					Q_max, P_max, P[P_max]);
		}
		// calculate best time (recursively) with this split
		// (this may try splitting smaller stacks too)
		optimize(P, P_max, P_time);
		// if better than old time, keep this time
		// (don't forget (k-1)*Q_count time to move the pancakes)
		if (P_time + (k - 1) * Q_count < time) {
			time = P_time + (k - 1) * Q_count;
		}

		if (q <= 3) {
			break;  // further splitting is pointless
		}
	}
	// time is updated, we're done optimizing.
	return 0;
}

int main()
{
	int T;  // number of test cases (T <= 100)
	// int t;  // test case counter -- made static for visibility
	int D;  // number of diners for this test case (D <= 1000)
	int d;  // diner counter
	int p;  // current pancake count (p <= 1000)
	vector<int> Q;  // Q[k] == # of diners with k pancakes
	int Q_max;  // greatest k with Q[k] > 0
	int best;  // best time possible for this case

	scanf("%d", &T);
	for (t=0; t < T; ++t) {
		/* Read data for test case t. */
		scanf("%d", &D);
		Q.clear();
		Q.resize(LIMCAKES, 0);
		Q_max = 0;
		for (d = 0; d < D; ++d) {
			scanf("%d", &p);
			++Q.at(p);
			if (Q_max < p) { Q_max = p; }
		}
		// Debug printing
		if (T_DEBUG == t+1) {
			fprintf(stderr, "Q_max: %d, Q[Q_max]: %d\n",
					Q_max, Q[Q_max]);
		}

		/* Process data. */
		optimize(Q, Q_max, best);

		/* Report final answer. */
		printf("Case #%d: %d\n", t+1, best);
	}
	return 0;
}
