#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define MAXN 1001

bool cmp(double a,double b)
{
	return a<b;
}

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int T;
	int n,i,j,t;
	int W_sum,D_sum;
	double N[MAXN];
	double K[MAXN];
	bool tmp_K[MAXN];
	bool tmp_N[MAXN];
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		W_sum=0;
		D_sum=0;
		memset(tmp_K,false,sizeof(tmp_K));
		memset(tmp_N,false,sizeof(tmp_N));
		for(i=0;i<n;i++){
			scanf("%lf",&N[i]);
		} 
		for(i=0;i<n;i++){
			scanf("%lf",&K[i]);
		} 
		sort(N,N+n,cmp);
		sort(K,K+n,cmp);
		for(i=0;i<n;i++){
			j=0;
			while(j<n){
				if(K[j]>N[i] && !tmp_K[j]){
					W_sum++;
					tmp_K[j]=true;
					break;
				}
				j++;
			}
			j=0;
			while(j<n){
				if(K[j]<N[i] && !tmp_N[j]){
					D_sum++;
					tmp_N[j]=true;
					break;
				}
				j++;
			}
		}
		W_sum=n-W_sum;
		printf("Case #%d: %d %d\n",t,D_sum,W_sum);
	}
	return 0;
}