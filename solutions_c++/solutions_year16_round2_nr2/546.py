#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

char C[20], J[20];
long long best_c, best_j, best_diff;

long long labs(long long a) {
	return a > 0 ? a : -a;
}

void read(){
	scanf("%s%s", C, J);
}

void test(long long c, long long j) {
	long long diff = labs(j - c);
	if (best_diff == -1 || diff < best_diff || (diff == best_diff && c < best_c) ||
		(diff == best_diff && c == best_c && j < best_j)) {
		best_diff = diff;
		best_j = j;
		best_c = c;
	}
}

long long maximize(char *S, int pos, long long ac) {
	if (S[pos] == 0) {
		return ac;
	} else if (S[pos] == '?') {
		return maximize(S, pos+1, ac*10 + 9);
	} else {
		return maximize(S, pos+1, ac*10 + (S[pos] - '0'));
	}
}

long long minimize(char *S, int pos, long long ac) {
	if (S[pos] == 0) {
		return ac;
	} else if (S[pos] == '?') {
		return minimize(S, pos+1, ac*10);
	} else {
		return minimize(S, pos+1, ac*10 + (S[pos] - '0'));
	}
}

void go(int pos, long long c, long long j) {
	if (C[pos] == 0) {
		test(c, j);
	} else if (C[pos] == '?' && J[pos] == '?') {
		go(pos + 1, c * 10, j * 10);

		long long mc = maximize(C, pos + 1, c * 10);
		long long mj = minimize(J, pos + 1, j * 10 + 1);
		test(mc, mj);

		mc = minimize(C, pos + 1, c * 10 + 1);
		mj = maximize(J, pos + 1, j * 10);
		test(mc, mj);
	} else if (C[pos] == '?' && J[pos] != '?') {
		go(pos+ 1, c * 10 + (J[pos] - '0'), j * 10 + (J[pos] - '0'));

		if (J[pos] != '9') {
			long long mc = minimize(C, pos + 1, c * 10 + (J[pos] - '0') + 1);
			long long mj = maximize(J, pos + 1, j * 10 + (J[pos] - '0'));
			test(mc, mj);
		} 
		if (J[pos] != '0') {
			long long mc = maximize(C, pos + 1, c * 10 + (J[pos] - '0') - 1);
			long long mj = minimize(J, pos + 1, j * 10 + (J[pos] - '0'));
			test(mc, mj);
		}
	} else if (C[pos] != '?' && J[pos] == '?') {
		go(pos+ 1, c * 10 + (C[pos] - '0'), j * 10 + (C[pos] - '0'));

		if (C[pos] != '9') {
			long long mc = maximize(C, pos + 1, c * 10 + (C[pos] - '0'));
			long long mj = minimize(J, pos + 1, j * 10 + (C[pos] - '0') + 1);
			test(mc, mj);
		} 
		if (C[pos] != '0') {
			long long mc = minimize(C, pos + 1, c * 10 + (C[pos] - '0'));
			long long mj = maximize(J, pos + 1, j * 10 + (C[pos] - '0') - 1);
			test(mc, mj);
		}
	} else if (C[pos] != J[pos]) {
		if (C[pos] < J[pos]) {
			long long mc = maximize(C, pos, c);
			long long mj = minimize(J, pos, j);
			test(mc, mj);
		} else {
			long long mc = minimize(C, pos, c);
			long long mj = maximize(J, pos, j);
			test(mc, mj);
		}
	} else {
		go(pos+1, c * 10 + (C[pos] - '0'), j * 10 + (J[pos] - '0'));
	}
}

void process() {
	best_diff = -1;
	go(0, 0, 0);

	int size = strlen(C);

	for (int i = size-1; i >= 0; i--) {
		C[i] = '0'+ (best_c%10);
		J[i] = '0' + (best_j%10);
		best_c /= 10;
		best_j /= 10;
	}
	printf("%s %s\n", C, J);
}

int main() {
	
	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}

	return 0;
}