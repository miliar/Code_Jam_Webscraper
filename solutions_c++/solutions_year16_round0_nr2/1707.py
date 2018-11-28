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
		char s[200];
		scanf("%s", s);
		int n = 0, ans = 0;
		while (s[n] != '\0') n++;
		while (n > 0){
			if (s[n - 1] == '+'){
				n--;
				continue;
			}
			if (s[0] == '+'){
				int i = 0;
				while (s[i] == '+'){
					s[i] = '-';
					i++;
				}
				ans++;
			}
			reverse(s, s + n);
			forn(i, 0, n) s[i] = (s[i] == '+' ? '-' : '+');
			ans++;
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
	return 0;
}