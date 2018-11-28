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

int n;
double V, X;
double r[111];
double c[111];

void solve() {
	scanf("%d%lf%lf", &n, &V, &X);
	REP(i, n) {
		scanf("%lf%lf", &r[i], &c[i]);
	}
	if (n==2 && c[0]==c[1]) {
		n = 1;
		r[0] = r[0]+r[1];
	}
	if (n==1) {
		if (c[0]==X) printf("%.7lf\n", V/r[0]);
		else printf("IMPOSSIBLE\n");
	}
	else if (n==2) {
		if (min(c[0], c[1]) > X || max(c[0], c[1]) < X) printf("IMPOSSIBLE\n");
		else {
			double t1 = (X*V - c[1]*V)/(c[0]*r[0]-c[1]*r[0]);
			double t2 = (V - r[0]*t1)/r[1];
			printf("%.7lf\n", max(t1, t2));
		}
	}
	else printf("ERROR\n");
}

int main() {
	int t; scanf("%d", &t);
	REP(i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
