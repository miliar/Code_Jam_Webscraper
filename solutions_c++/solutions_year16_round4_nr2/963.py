#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <utility>
#include <iostream>
using namespace std;
double dp[222],dp2[222];
double nilai[999];
int N,K;

void kasih(double v){
	memset(dp2,0,sizeof dp2);
	for (int i=0;i<=K/2;i++){
		
		dp2[i] += dp[i] * (1.0 - v);
		dp2[i+1] += dp[i] * v;

		dp[i] = dp2[i];
	}
	//cout<<" --"<<dp[K/2]<<endl;
}

int main() {
	int T = 0;
	int tt = 1;
	scanf("%d",&T);
	
	
	while (T--){
		printf("Case #%d: ",tt++);
		scanf("%d%d",&N,&K);
		for (int i=0;i<N;i++)
			scanf("%lf",&nilai[i]);

		sort(nilai,nilai + N);

		double res = 0.0;
		for (int i=0;i<=K;i++){
			//cout<<"TES "<<i<<endl;
			memset(dp,0,sizeof dp);
			dp[0] = 1.0;
			for (int j=0;j<i;j++){
			//	cout<<j<<endl;
				kasih(nilai[j]);
			}
			for (int j=N-1;j>(N - 1 - (K-i) );j--) {
			//	cout<<j<<endl;
				kasih(nilai[j]);
			}
			res = max(res,dp[K/2]);
		}

		printf("%.9lf\n",res);


	}
}