#include <iostream>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>
#include <cassert>
#include <sstream>
#include <bitset>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;

const int inf = 1e9;
const double eps = 1e-8;
const int maxn = 111;
const int mod = 1000000007;

int main() 
{
#ifdef DEBUG
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int T;
	scanf("%d\n", &T);
	for (int t = 0; t < T; ++t) {
		int n; 
		long double V, X;
		cin >> n >> V >> X;
		vd v(n), x(n);
		for (int i = 0; i < n; ++i) {
			cin >> v[i] >> x[i];
		}
		
		if (n == 2 && fabs(x[0] - x[1]) < eps) {
			v[0] += v[1];
			n = 1;
		}
		
		long double res = inf;
		if (n == 1) {
			if (fabs(X - x[0]) < eps) res = V / v[0];
		} else {
			
			long double v0 = (X * V - V * x[1]) / (x[0] - x[1]);
			if (v0 > -eps && v0 < V + eps) {
				ld t1 = v0 / v[0];
				ld t2 = (V - v0) / v[1];
				res = max(t1, t2);
			}
			/*
			int d = 100000;
			for (int k = 0; k < d; ++k) {
				double L = (double)k / d * V, R = (double)(k + 1) / d * V;
				//L = 0; R = V;
				//printf("%f %f\n", L, R);
				int it = 50;
				while (it--) {
					double M1 = L + (R - L) / 3;
					double M2 = L + (R - L) / 3 * 2;
					double diff1 = fabs(M1 * x[0] + (V - M1) * x[1] - X * V);
					double diff2 = fabs(M2 * x[0] + (V - M2) * x[1] - X * V);
					if (diff1 < diff2) R = M2;
					else L = M1;
				}
				double v0 = L;
				double diff = fabs(v0 * x[0] + (V - v0) * x[1] - X * V);
				if (diff < 1e-6) {
					double t1 = v0 / v[0];
					double t2 = (V - v0) / v[1];
					res = min(res, max(t1, t2));
				}
			}*/
		}
		
		if (fabs(res - inf) < eps) {
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
		} else {
			printf("Case #%d: %.10Lf\n", t + 1, res);
		}
	}
	
	return 0;
}
