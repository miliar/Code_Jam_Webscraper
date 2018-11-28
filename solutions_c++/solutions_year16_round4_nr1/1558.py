#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

typedef pair<int, int> pii;
typedef long long ll;

int N, D[3];
char cs[4] = "PRS";
int res[1 << 12 + 10];
int cache[13][1 << 12];
int cl = 0;

bool rec(int ind) {
	if (ind > 0) {
		cache[0][ind-1] = res[ind-1];
		int c = ind;
		// cout << c << endl;
		if (c > 0) {
			// cout << c << endl;
			int cnt = 0;
			while ((c & 1) == 0) {
				// cout << c << endl;
				int a = cache[cnt][c-1];
				int b = cache[cnt][c-2];
				c >>= 1;
				// cout << a << ' ' << b << endl;
				int rr;
				if (a == b) {
					return false;
				}
				if (a > b) swap (a, b);
				if (a == 0 && b == 1) rr = 0;
				if (a == 0 && b == 2) rr = 2;
				if (a == 1 && b == 2) rr = 1;
				cache[cnt+1][c-1] = rr;
				cnt++;
			}
		}
	}
	if (ind >= 1 << N) return true;
	REP(i, 3) {
		if (D[i] > 0) {
			D[i]--;
			res[ind] = i;
			if (rec(ind + 1)) return true;
			D[i]++;
		}
	}
	return false;
}

void solve() {
	cin >> N >> D[1] >> D[0] >> D[2];
	if (rec(0)) {
		REP(i, 1 << N) cout << cs[res[i]];
		// cout << cache[0];
	} else {
		cout << "IMPOSSIBLE";
	}
}

int main() {
	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << (i+1) << ": ";
		solve();
		cout << endl;
	}
}