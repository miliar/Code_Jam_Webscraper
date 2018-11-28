
#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <string.h>
#include <string>
#include <limits.h>
#include <algorithm>
#include <set>
#include <ctime>
using namespace std;
#define SZ(x) ((int)(x).size())
#define rep(i,a,n) for (int i=a; i<(int)n; i++)
#define per(i,n,a) for (int i=n; i>=a; i--)
#define hk push_back
#define pk pop_back
#define mp make_pair
#define PI 3.141592653589793
#define clr(a) memset(a, 0, sizeof(a))
#define clr1(a) memset(a, -1, sizeof(a))
typedef vector<int> VI;
typedef vector< pair<int, int> > VIP;
typedef vector< pair<int, pair<int, double> > > VIPP;
typedef vector<string> VS;
typedef vector <double> VD;
typedef vector <bool> VB;
typedef long long ll;
#define MAX_V 1000
const ll mod = 1000000007;
ll powmod(ll a, ll b) {
	ll res = 1; a %= mod; for (; b; b >>= 1){ if (b & 1)res = res*a%mod; a = a*a%mod; }return res;
}

double T, N, V, X, r, t;
vector< pair<double, double> > info;

int main() {
	cout.precision(12);
	cin >> T;
	int T1 = 0;
	while (T1++ < T) {
		info.clear();
		cin >> N >> V >> X;
		V *= 10000; X *= 10000;
		rep(i, 0, N) {
			cin >> r >> t; r *= 10000; t *= 10000;
			info.push_back(mp(r, t));
		}

		if (N == 1) {
			if (X != info[0].second) cout << "Case #" << T1 << ": " << "IMPOSSIBLE" << endl;
			else cout << "Case #" << T1 << ": " << V / info[0].first << endl;
		}
		else if (N == 2) {
			if (info[0].second == info[1].second) {
				if (X != info[0].second) cout << "Case #" << T1 << ": " << "IMPOSSIBLE" << endl;
				else cout << "Case #" << T1 << ": " << V / (info[0].first + info[1].first) << endl;
			}
			else {
				if (max(info[0].second, info[1].second) < X || min(info[0].second, info[1].second) > X)
					cout << "Case #" << T1 << ": " << "IMPOSSIBLE" << endl;

				else {
					double V0 = V*(X - info[1].second) / (info[0].second - info[1].second);
					double V1 = V - V0;
					cout << "Case #" << T1 << ": " << max(V0 / info[0].first, V1 / info[1].first) << endl;
				}
			}
		}
	}

	return 0;
}