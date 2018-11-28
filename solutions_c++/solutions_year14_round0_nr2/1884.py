#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
#define LL long long

double c,f,x;

double calc(int num) {
	double ret = 0,rate = 2.0;
	for (int i=0; i<num; i++) {
		ret += c/rate;
		rate += f;
	}
	ret += x/rate;
	return ret;
}

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%lf%lf%lf",&c,&f,&x);
		int mi = 0,mx = (int)(x*2),mid;
		double r1,r2;
		double ans = 1e20;
		while (mi < mx) {
			mid = (mi+mx)/2;
			r1 = calc(mid);
			r2 = calc(mid+1);
			if (r1 < r2) {
				ans = min(ans,r1);
				mx = mid;
			}
			else {
				ans = min(ans,r2);
				mi = mid+2;
			}
		}
		printf("Case #%d: %.9f\n",t,ans);
	}
	return 0;
}
