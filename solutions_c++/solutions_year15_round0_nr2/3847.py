#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

struct testcase {
	int n;
	vector<int> pck;

	static testcase* read() {
		return new testcase();
	}

	testcase() {
		// Read input
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			int q;
			scanf("%d", &q);
			pck.push_back(q);
		}
	}

	int rec(vector<int> &p) {
		int max = 0;
		int imax = -1;
		for (int i = 0; i < p.size(); i++) {
			if (p[i] > max) {
				max = p[i];
				imax = i;
			}
		}
		if (max <= 2) return max;

		// First possibility : let everyone eat until the end
		int best = max;

		// Second possibility : cut the biggest in two
		for (int j = 2; j <= p[imax] / 2; j++) {
			vector<int> q = p;

			q.push_back(j);
			q[imax] -= j;

			int b2 = 1 + rec(q);
			if (b2 < best) best = b2;
		}

		return best;
	}

	void solve() {
		printf("%d\n", rec(pck));
	}
};

struct problem {
	int ncases;
	vector<testcase*> cases;

	void read() {
		cases.clear();
		scanf("%d", &ncases);
		for (int i = 0; i < ncases; i++) {
			cases.push_back(testcase::read());
		}
	}
	void solve() {
		for (int i = 0; i < ncases; i++) {
			printf("Case #%d: ", i+1);
			cases[i]->solve();
		}
	}
};

int main() {
	problem p;
	p.read();
	p.solve();

	return 0;
}
