#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

const int MAXN = 105;
const double INF = 1e15;
const double eps = 1e-9;

int tn;
int n;
double v, x;
double r[MAXN], t[MAXN];
bool bad = false;
double ans;

int main() {
	//assert(freopen("input.txt","r",stdin));
	//assert(freopen("output.txt","w",stdout));

	scanf("%d", &tn);
	
	for (int test = 1; test <= tn; test++) {
		scanf("%d %lf %lf", &n, &v, &x);

		for (int i = 1; i <= n; i++) {
			scanf("%lf %lf", &r[i], &t[i]);
		}

		bad = false;
		ans = INF;

		if (n == 1) {
			if (abs(t[1] - x) > eps)
				bad = true;
			else
				ans = v / r[1];
		}
		else {
			if (x > t[1] + eps && x > t[2] + eps)
				bad = true;
			else if (x + eps < t[1] && x + eps < t[2])
				bad = true;
			else {
				if (abs(t[1] - x) <= eps)
					ans = v / r[1];
				if (abs(t[2] - x) <= eps)
					ans = min(ans, v / r[2]);
				if (abs(t[1] - t[2]) > eps) {
					double v1 = (v * x - t[2] * v) / (t[1] - t[2]);
					double tm = max(v1 / r[1], (v - v1) / r[2]);
					ans = min(ans, tm);
				}
				else {
					if (abs(t[1] - x) <= eps) {
						ans = min(ans, v / (r[1] + r[2]));
					}
				}                 
			}	
		}

		if (bad)
			printf("Case #%d: IMPOSSIBLE\n", test);
		else
			printf("Case #%d: %.12lf\n", test, ans);
	}

	return 0;
}