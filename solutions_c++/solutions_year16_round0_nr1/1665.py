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
		ll n;
		scanf("%lld", &n);
		if (n == 0){
			printf("Case #%d: INSOMNIA\n", tt + 1);
			continue;
		}
		vector<bool> used(11, false);
		int cnt = 10;
		ll i = 1;
		while (cnt){
			ll tmp = i * n;
			while (tmp){
				int d = (int)(tmp % 10);
				tmp /= 10;
				if (!used[d]) cnt--;
				used[d] = true;
				if (cnt == 0){
					printf("Case #%d: %lld\n", tt + 1, i * n);
					break;
				}
			}
			i++;
		}
	}
}

void gener()
{
	freopen("input.txt", "w", stdout);
	int n = 1000001;
	printf("%d\n", n);
	forn(i, 0, n) printf("%d\n", i);
}

int main()
{
	//gener();
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
	return 0;
}