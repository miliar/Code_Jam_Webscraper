#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <list>
#include <set>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <ctime>
#include <queue>
#include <map>
#include <cstring>
#include <unordered_map>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef bool bl;
typedef pair<bl, bl> pbl;
typedef pair<ld, ld> pld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define mp make_pair
#define ft first
#define sd second
#define forn(i, y, x) for(int i = y; i < x; i++)
#define ford(i, y, x) for(int i = y; i >= x; i--)
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define error exit(1)
#define DEBUG
const int mod = (int)1e9;
const int inf = (int)1e9;
const int base = 1000 * 1000 * 1000;
const int maxn = 2005;
const ld pi = acosl(-1.0);
const ld eps = 1e-9;

void solve()
{
	int t;
	scanf("%d", &t);
	forn(tt, 0, t){
		ll k, c, s;
		scanf("%lld %lld %lld", &k, &c, &s);
		ll val = 1;
		forn(i, 0, c - 1) val *= k;
		if (val == 1) val = 0;
		printf("Case #%d: ", tt + 1);
		forn(i, 0, s) printf("%lld ", i * (val + 1) + 1);
		printf("\n");
	}
}

void gener()
{
	int n, c;
	cin >> n >> c;
	vector<pair<string, string>> ans;
	forn(i, 0, 1 << n){
		string s = "";
		forn(j, 0, n) s += ((1 << j) & i ? 'L' : 'G');
		string t = s;
		forn(p, 1, c){
			string tmp = "";
			forn(k, 0, sz(t)){
				if (t[k] == 'L') tmp += s;
				else tmp += string(n, 'G');
			}
			t = tmp;
		}
		ans.push_back(mp(t, s));
	}
	vector<int> sum(sz(ans.front().ft), 0);
	forn(i, 0, sz(sum)) forn(j, 0, sz(ans)){
		if (ans[j].ft[i] == 'L') sum[i]++;
	}
	forn(i, 0, sz(ans)) cout << ans[i].ft << ' ' << ans[i].sd << endl;
	forn(i, 0, sz(sum)) cout << sum[i] << '|';
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	//gener();
	solve();
	return 0;
}