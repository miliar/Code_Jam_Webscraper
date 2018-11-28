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

int n, r, p, s;
string res[3];

string rec(char c, int n) {
	if (n==0) return string(1, c);
	else {
		string l; string r;
		if (c=='R') {
			l = rec('R', n-1); r = rec('S', n-1);
		}
		if (c=='P') {
			l = rec('P', n-1); r = rec('R', n-1);
		}
		if (c=='S') {
			l = rec('P', n-1); r = rec('S', n-1);
		}
		string res = (l<r) ? (l+r) : (r+l);
		return res;
	}
}

int cnt(int k, char c) {
	int ans = 0;
	for (int i=0; i<res[k].size(); i++) if (res[k][i]==c) ans++;
	return ans;
}

void solve() {
	cin >> n >> r >> p >> s;
	res[0] = rec('R', n);
	res[1] = rec('P', n);
	res[2] = rec('S', n);
	bool exist = false;
	string ans = "";
	REP(i, 3) {
		if (cnt(i, 'R')==r && cnt(i, 'P')==p && cnt(i, 'S')==s) {
			exist = true;
			if (ans=="" || res[i]<ans) ans = res[i];
		}
	}
	if (exist) cout << ans << endl;
	else cout << "IMPOSSIBLE" << endl;
}

int main() {
	int t; scanf("%d", &t);
	REP(i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
