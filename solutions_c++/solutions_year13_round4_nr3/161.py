#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <assert.h>
#include <algorithm>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;

int n;

bool used[5555];
int increase[5555], decrease[5555];

bool conn[2222][2222];

VI edge[5555];

int ans[5555];

void solve(VI res, int l, int r) {
	// cout << "l = " << l << " r = " << r << endl;
	if (!res.size()) return;
	int key = res[0];
	VI left, right;
	TR(it, res) {
		if (*it != key && conn[*it][key]) {
			left.PB(*it);
		} else if (*it != key) {
			right.PB(*it);
		}
	}

	// cout << "key = " << key << " left.size() = " << left.size() << endl;

	ans[key] = l + left.size();
	solve(left, l, (int)l + left.size() - 1);
	solve(right, r - (int)right.size() + 1, r);
}

int main() {
	int T, nowCase = 0;
	cin >> T;
	while (T--) {
		cin >> n;
		REP(i, n) cin >> increase[i];
		REP(i, n) cin >> decrease[i];
		REP(i, n) edge[i].clear();

		REP(i, n) {
			for (int j = i - 1; j >= 0; --j) {
				if (increase[i] == increase[j] + 1) {
					edge[j].PB(i);
					break;
				}
			}

			for (int j = i - 1; j >= 0; --j) {
				if (increase[i] == increase[j]) {
					edge[i].PB(j);
					break;
				}
			}


			for (int j = i - 1; j >= 0; --j) {
				if (increase[i] == increase[j] - 1) {
					edge[i].PB(j);
					break;
				}
			}

			for (int j = i + 1; j < n; ++j) {
				if (decrease[i] == decrease[j] + 1) {
					edge[j].PB(i);
					break;
				}
			}

			for (int j = i + 1; j < n; ++j) {
				if (decrease[i] == decrease[j]) {
					edge[i].PB(j);
					break;
				}
			}

			for (int j = i + 1; j < n; ++j) {
				if (decrease[i] == decrease[j] - 1) {
					edge[i].PB(j);
					break;
				}
			}
		}

		REP(i, n) REP(j, n) conn[i][j] = false;
		REP(i, n) TR(it, edge[i]) conn[i][*it] = true;
		REP(k, n) REP(i, n) REP(j, n) conn[i][j] |= conn[i][k] & conn[k][j];
		REP(i, n) assert(!conn[i][i]);

		VI res;
		REP(i, n) res.PB(i);
		solve(res, 0, n - 1);
		cout << "Case #" << ++nowCase << ":";
		REP(i, n) {
			cout << " " << ans[i] + 1;
		}
		cout << endl;
	}
	return 0;
}