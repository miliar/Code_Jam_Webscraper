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
#include <deque>
using namespace std;
//-----------------------------------------------------------
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
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
//-----------------------------------------------------------

#define MAXN 150
#define eps 1e-10

double tv, tt;

int N;
struct W{
	double s, t;
};
W w[MAXN];


void solve() {
	double T1, T2;

	if (N == 1) {
		if (tt != w[0].t) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("%.10lf\n", tv / w[0].s);
		}
	}
	else if (N == 2) {

		if (w[0].t == w[1].t) {
			if (tt != w[0].t) {
				printf("IMPOSSIBLE\n");
			}
			else {
				printf("%.10lf\n", tv / (w[0].s + w[1].s));
			}
		}
		else {

			T2 = (tv * (tt - w[0].t)) / (w[1].s * (w[1].t - w[0].t) );
			T1 = (tv - T2 * w[1].s) / w[0].s;

			//printf("%lf %lf => ", T1, T2);

			if (T1 + eps < 0 || T2 + eps < 0) {
				printf("IMPOSSIBLE\n");
			}
			else {
				printf("%.10lf\n", max(T1, T2));
			}
		}
	}
	fflush(stdout);
}

int main() {
	int cases;
	int caseid = 1;

	freopen("input", "r", stdin);
//freopen("output", "w", stdout);
	scanf("%d", &cases);
	while (cases--) {

		printf("Case #%d: ", caseid++);
		scanf("%d%lf%lf", &N, &tv, &tt);
		for(int i = 0; i < N; i++) {
			scanf("%lf%lf", &w[i].s, &w[i].t);
		}


		solve();
	}
	return 0;
}

