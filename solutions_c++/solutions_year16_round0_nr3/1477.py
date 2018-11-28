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

int del[20] = { 0, 0, 3, 2, 5, 2, 7, 2, 3, 2, 11 };
int d[33][10];

void solve()
{
	int t;
	scanf("%d", &t);
	forn(tt, 0, t){
		srand(time(NULL));
		forn(b, 2, 11){
			int val = 1;
			forn(p, 0, 33){
				d[p][b] = val;
				val = (val * b) % del[b];
			}
		}
		int n, j;
		scanf("%d %d", &n, &j);
		vector<string> ans;
		while (sz(ans) != j){
			fprintf(stderr, "%d\n", sz(ans));
			string s = string(n, '1');
			forn(i, 1, n - 1) s[i] = (rand() & 1 ? '1' : '0');
			bool ok = true;
			forn(b, 2, 11){
				int val = 0;
				forn(p, 0, n) if (s[p] == '1')
					val = (val + d[p][b]) % del[b];
				if (val != 0){
					ok = false;
					break;
				}
			}
			if (!ok) continue;
			reverse(all(s));
			forn(i, 0, sz(ans)) if (ans[i] == s){
				ok = false;
				break;
			}
			if (!ok) continue;
			ans.push_back(s);
		}
		printf("Case #%d:\n", tt + 1);
		forn(i, 0, j){
			printf("%s ", ans[i].c_str());
			forn(b, 2, 11) printf("%d ", del[b]);
			printf("\n");
		}
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
	return 0;
}