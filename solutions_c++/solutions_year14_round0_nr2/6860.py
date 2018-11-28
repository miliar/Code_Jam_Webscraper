#include <bits/stdc++.h>
using namespace std;
#define pdd pair<double,double>
double c,f,x;
double dp[1000000];
int main()
{
	int t;
	int cs = 1;
	scanf("%d",&t);
	while (t--) {
		scanf("%lf%lf%lf",&c,&f,&x);
		double pre = x/2;
		double r = 2;
		dp[0] = 0;
		int i = 1;
		double ans;
		while (1) {
			dp[i] = dp[i-1] + c/r;
			r += f;
			double curr = dp[i] + x/r;
			if (curr > pre) {
				ans = pre;
				break;
			}
			else {
				pre = curr;
			}
			i++;
		}
		printf("Case #%d: %.8lf\n",cs++,ans);
	}
	return 0;
}
