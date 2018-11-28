#include <cstdio>
#include <algorithm>
using namespace std;
int T;
int main(){
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double dp[100001];
		dp[0] = 0;
		double ans = 1e15;
		for(int i=0;i<100000;i++){
			ans = min(ans,dp[i]+(X/(2.0+i*F)));
			dp[i+1] = dp[i]+(C/(2.0+i*F));
		}
		printf("Case #%d: %.9f\n",t,ans);
	}
	return 0;
}

