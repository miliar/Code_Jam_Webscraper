#include<bits/stdc++.h>
using namespace std;
int T;
int N,K;
double P[205];
double DP[205][205];
int main()
{
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%d%d",&N,&K);
		for(int i=0;i<N;i++)cin >> P[i];
		sort(P,P+N);
		double ans=0;
		for(int i=0;i<=K;i++){
			//[0,i),[N+i-K,N)
			for(int j=0;j<205;j++){
				for(int k=0;k<205;k++){
					DP[j][k]=0;
				}
			}
			DP[0][0]=1;
			for(int j=1;j<=K;j++){
				for(int k=0;k<=K;k++){
					//DP[j][k]
					if(k!=0){
						if(j-1<i)DP[j][k]+=DP[j-1][k-1]*P[j-1];
						else DP[j][k]+=DP[j-1][k-1]*P[N+j-K-1];
					}
					
					if(j-1<i)DP[j][k]+=DP[j-1][k]*(1-P[j-1]);
					else DP[j][k]+=DP[j-1][k]*(1-P[N+j-K-1]);
					
				}
			}
			//printf("%d %.14f\n",i,DP[K][K/2]);
			ans=max(ans,DP[K][K/2]);
		}
		printf("Case #%d: %.14f\n",cas,ans);
	}
	return 0;
}
