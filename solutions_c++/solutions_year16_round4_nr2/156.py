#include <bits/stdc++.h>
using namespace std;
int Test,N,K;
double ans,P[210];
double f[210][410];
bool b[210];
double calc(){
	memset(f,0,sizeof(f));
	f[0][K]=1;
	for (int i=1;i<=N;i++)
		for (int j=1;j<2*K;j++)
			if (b[i]){
				f[i][j+1]+=f[i-1][j]*P[i];
				f[i][j-1]+=f[i-1][j]*(1-P[i]);
			}else f[i][j]=f[i-1][j];
	return f[N][K];
}
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&Test);
	for (int tt=1;tt<=Test;tt++){
		scanf("%d%d",&N,&K);
		for (int i=1;i<=N;i++)
			scanf("%lf",&P[i]);
		sort(P+1,P+N+1);
		ans=0;
		memset(b,0,sizeof(b));
		for (int i=1;i<=K;i++)b[N-i+1]=1;
		ans=max(ans,calc());
		for (int l=1;l<=K;l++){
			b[N-K+l]=0;
			b[l]=1;
			ans=max(ans,calc());
		}
		printf("Case #%d: %.10lf\n",tt,ans);
	}
}