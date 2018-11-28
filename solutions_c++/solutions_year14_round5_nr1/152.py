#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <map>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

const int INF = 999666111;
int n;
ll a[1000100];
ll S[1000100];
ll p, q, r, s;

inline ll subsum(int a, int b) // sum of arr[a..b)
{
	return S[b] - S[a];
}

inline ll eval(int x, int y)
{
	ll s1 = subsum(0, x);
	ll s2 = subsum(x, y + 1);
	ll s3 = subsum(y + 1, n);
	ll sAll = s1 + s2 + s3;
	ll solveig = max(max(s1, s2), s3);
	ll arnar = sAll - solveig;
	return arnar;
}

double solve(void)
{
	if (n == 1) return 0;
	FOR(i, n)
		a[i] = ((((ll) i * p + q) % r) + s);
	//
	if (n == 2)
		return min(a[0], a[1]) / (double) (a[0] + a[1]);
	//
	S[0] = 0;
	FOR(i, n) {
		S[i + 1] = S[i] + a[i];
	}
	ll answer = 0;
	for (int x = 0; x < n; x++) {
		int yl = x, yr = n - 1;
		while (yr > yl + 4) {
			int mid1 = (2*yl + yr) / 3;
			int mid2 = (yl + 2*yr) / 3;
			ll score1 = eval(x, mid1);
			ll score2 = eval(x, mid2);
			if (score2 > score1) {
				yl = mid1;
			} else {
				yr = mid2;
			}
		}
		for (int y = yl; y <= yr; y++) {
			answer = max(answer, eval(x, y));
		}
	}
	return answer / (double) subsum(0, n);
}

int main(void)
{
// 	freopen("/home/vesko/gcj/a.in", "rt", stdin);
	int TC;
	cin >> TC;
	for (int T = 1; T <= TC; T++) {
		cin >> n >> p >> q >> r >> s;
		printf("Case #%d: %.9lf\n", T, solve());
	}
	return 0;
}
