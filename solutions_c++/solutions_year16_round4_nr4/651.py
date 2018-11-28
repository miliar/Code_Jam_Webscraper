#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <iostream>
#include <sstream>
#include <cctype>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> ii;

int n;
int graf[10][10];
int novy[10][10];
int chosen[10];

bool zkus(vector<int> &perm, int k) {
	if (k==perm.size()) return true;
	else {
		int a = perm[k];
		bool ans = false;
		REP(i, n) if (novy[a][i] && !chosen[i]) {
			ans = true;
			chosen[i] = 1;
			if (zkus(perm, k+1)==false) return false;
			chosen[i] = 0;
		}
		return ans;
	}
}

int sol(int K) {
	int ans = 0;
	REP(i, n) REP(j, n) novy[i][j] = graf[i][j];
	for(int i=0; i<n*n; i++) if ((K & (1<<i))!=0) {
		int a = i/n;
		int b = i%n;
		novy[a][b] = 1;
		ans++;
	}
	vector<int> perm; REP(i, n) perm.push_back(i);
	bool ok = true;
	do {
		REP(i, 10) chosen[i] = 0;
		ok &= zkus(perm, 0);
	} while(next_permutation(perm.begin(), perm.end()));
	if (!ok) return n*n;
	return ans;
}

void solve() {
	cin >> n;
	REP(i, 10) REP(j, 10) graf[i][j] = 0;
	REP(i, n) {
		string s; cin >> s;
		REP(j, s.size()) graf[i][j] = (s[j]=='1') ? 1 : 0;
	}
	int ans = n*n;
	int N = 1<<(n*n);
	REP(i, N) {
		ans = min(ans, sol(i));
	}
	cout << ans << endl;
}

int main() {
	int t; scanf("%d", &t);
	REP(i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
