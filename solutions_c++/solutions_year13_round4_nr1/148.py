#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
#define next NEXTHUI
#define prev PREVHUI
#define y1 Y1HUI

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

const int64 P = 1000002013;

int n, m;
vector<pii> Q;
map<int, int64> S, S1;

int64 solve() {
	cin >> n >> m;
	Q.clear();
	int64 res = 0;
	forn(i, m) {
		int x, y, z;
		scanf("%d%d%d", &x, &y, &z);
		Q.pb(mp(x, -z));
		Q.pb(mp(y, z));
		int64 d = (y - x);
		d = d * (n + n - d + 1) / 2 % P;
		d = d * z % P;
		res = (res + d) % P; 
	}
	sort(all(Q));
	S.clear();
	int cur = 1;
	int64 ans = 0;
	forn(i, Q.size()) {
		int64 d = Q[i].fs - cur;
		if (d > 0) {
			S1.clear();
			for(map<int, int64> :: iterator it = S.begin(); it != S.end(); it++) {
				ans = (ans + d * (it->fs + it->fs - d + 1) / 2 % P * (it->sc % P)) % P;
				S1[it->fs - d] = it->sc;
			}
			S = S1;
		}
		cur = Q[i].fs;
		int64 z = -Q[i].sc;
		if (z > 0)
			S[n] += z;
		else {
			z = -z;
			while (S.size() > 0) {
				int x = S.rbegin()->fs;
				int64 d = min(S[x], z);
				z -= d;
				S[x] -= d;
				if (S[x] == 0)
					S.erase(x);
				else
					break;
			}
		}	
	}
	return (res - ans + P) % P;
}

int main ()
{
	int tt;
	cin >> tt;
	forn(ii, tt) {
		printf("Case #%d: %d\n", ii + 1, I solve());
	}	
	return 0;
}
