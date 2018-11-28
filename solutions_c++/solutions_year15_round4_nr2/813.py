#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#define PB push_back
#define FI first
#define SE second
#define MP make_pair

using namespace std;

typedef int LL;
typedef pair<LL, LL> pi;

int main () {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		int n;
		double vk, tk;
		scanf("%d %lf %lf", &n, &vk, &tk);
		double v1, v2, t1, t2;		
		scanf("%lf %lf", &v1, &t1);
		if(n > 1) {
			scanf("%lf %lf", &v2, &t2);
		} else {
			t2 = t1;
			v2 = 0;
		}
		if(tk > fmax(t1, t2) || tk < fmin(t1, t2)) {
			printf("Case #%d: IMPOSSIBLE\n", i);	
			continue;	
		}
		double result = 0;
		if (t2 == t1) {
			result = vk / (v1 + v2);
		}
		else {
			double v = vk * (tk - t2) / (t1 - t2);
			double vr = vk - v;
			result = fmax(v / v1 , vr / v2);
		}
		printf("Case #%d: %.6lf\n", i, result);
	}
	return 0;
}