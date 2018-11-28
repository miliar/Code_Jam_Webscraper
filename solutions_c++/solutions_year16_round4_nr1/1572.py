#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pi 3.14159265358979323846264338327950288
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SZ(x) ((int)x.size())
#define mid (l + r) / 2
#define Left k * 2, l, mid
#define Right k * 2 + 1, mid + 1, r
#define N 12
using namespace std;
vector<string> ans[20];
bool cmp(const string &s, int st, int ed, int len) {
	//st > ed
	for (int i = 0; i < len; i++)
		if (s[st + i] != s[ed + i])
			return s[st + i] > s[ed + i];
	return false;
}
bool check(const string &st, int p, int r, int s) {
	int cp = 0, cr = 0, cs = 0;
	for (int i = 0; i < st.length(); i++) {
		if (st[i] == 'P') cp++;
		if (st[i] == 'R') cr++;
		if (st[i] == 'S') cs++;
	}
	return p == cp && r == cr && s == cs;
}
int cas, cases;
int n, p, r, s;
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	ans[0].pb("P");
	ans[0].pb("R");
	ans[0].pb("S");
	for (int i = 1; i < N; i++) {
		for (int j = 0; j < ans[i - 1].size(); j++) {
			string now = "";
			string pre = ans[i - 1][j];
			for (int k = 0; k < pre.length(); k++) {
				if (pre[k] == 'P')
					now = now + "PR";
				if (pre[k] == 'R')
					now = now + "RS";
				if (pre[k] == 'S')
					now = now + "PS";
			}
			//sort the string
			int m = 1 << i;
			for (int step = 0; step < i; step ++) {
				int len = 1 << step;
				for (int k = 0; k < m - len; k += 2 * len)
					if (cmp(now, k, k + len, len)) {
						for (int l = 0; l < len; l++)
							swap(now[k + len + l], now[k + l]);
					}
			}
			ans[i].pb(now);
			//cout << now << " ";
		}
		//cout << endl;
	}
	scanf("%d", &cas);
	for (cases = 1; cases <= cas; cases ++) {
		scanf("%d%d%d%d", &n, &r, &p, &s);
		bool yes = false;
		printf("Case #%d: ", cases);
		for (int i = 0; i < ans[n].size(); i++)
			if (check(ans[n][i], p, r, s)) {
				cout << ans[n][i] << endl;
				yes = true;
				break;
			}
		if (!yes) cout << "IMPOSSIBLE" << endl;
	}
}
