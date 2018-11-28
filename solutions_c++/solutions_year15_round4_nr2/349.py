#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define PI 3.1415926535897932384626433832795
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector< pii >   vpii;

#define MAXN 110
#define EPS 1e-10

int n;
double v, x;
double c[MAXN];
double r[MAXN];
double v1, v2;

bool eq(double x, double y) {
	return abs(x - y) < EPS;
}
int main() {
	int tc;
	
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%i", &tc);
	for(int tt=1; tt<=tc; ++tt) {
		scanf("%i%lf%lf", &n, &v, &x);
		printf("Case #%i: ", tt);

		for(int i=0; i<n; ++i) scanf("%lf %lf", &r[i], &c[i]);
		bool ok = false;
		if (n == 1 && abs(c[0] - x) < EPS) {
			ok = true;
			printf("%.12f\n", v / r[0]);
		}

		if (n == 2) {
			if (c[0] > c[1]) {
				swap(c[0], c[1]);
				swap(r[0], r[1]);
			}
			if (c[0] <= x + EPS && x - EPS <= c[1]) {
				if (eq(c[0], c[1]) && eq(c[0], x)) {
					printf("%.12f\n", v / (r[0] + r[1]));
					ok = true;
				} else if (eq(c[0], x)) {
					printf("%.12f\n", v / r[0] );
					ok = true;
				} else if (eq(c[1], x)) {
					printf("%.12f\n", v / r[1] );
					ok = true;
				} else {
					v1 = (v*x - v*c[1]) / (c[0] - c[1]);
					v2 = v - v1;
					v1 = v1 / r[0];
					v2 = v2 / r[1];
					printf("%.12f\n", max(v1, v2));
					ok = true;
				}
			}
		}

		if (!ok) {
			printf("IMPOSSIBLE\n");
		}
		
	}
    return 0;
}