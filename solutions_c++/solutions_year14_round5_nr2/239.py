#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <utility>
using namespace std;
#define fo(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define range(i,a,b) for(int i=(a),_n=(b); i<_n; ++i)

typedef long long ll;
const int MAX_N = 110, MAX_HITS = 1100;
bool seen[MAX_N][MAX_HITS];
ll best[MAX_N][MAX_HITS], money[MAX_N], tower[MAX_N], hits[MAX_N], N;

ll bestMoney(int n, int h) {

	if (n == N) return 0;

	if (!seen[n][h]) {

		ll res = 0;

		if (h + tower[n] >= hits[n]) {
			res = money[n] + bestMoney(n + 1, h + tower[n] - 1 - hits[n]);
		}

		res = max(res, bestMoney(n + 1, h + tower[n]));

		seen[n][h] = true;
		best[n][h] = res;
	}

	return best[n][h];
}


int main() {

	int T;
	cin >> T;
	range(testCase, 1, T+1) {

		int P, Q;
		cin >> P >> Q >> N;

		fo(i, N) {
			int H, G;
			cin >> H >> G;

			money[i] = G;
			tower[i] = (H + Q - 1) / Q;

			int toHit = H % Q;
			if (toHit == 0) toHit = Q;
			hits[i] = (toHit + P - 1) / P;
		}

		fo(i, N) fo(j, MAX_HITS) seen[i][j] = false;

		cout << "Case #" << testCase << ": " << bestMoney(0, 0) << endl;

	}

}