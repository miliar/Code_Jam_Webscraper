#include<stdio.h>
int tcn,tc;
long long int ans;
long long int n,m;
long long int sum[1010];
long long int dat[1010];
long long int mv[1010];
long long int mx[1010];
int main(){
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		scanf("%lld%lld",&n,&m);
		for(i=0;i<n-m+1;i++){
			scanf("%lld",&sum[i]);
		}
		for(i=0;i<m;i++){
			dat[i]=0;
			mv[i]=0;
			mx[i]=0;
		}
		for(i=m;i<n;i++){
			dat[i]=sum[i-m+1]-sum[i-m]+dat[i-m];
			if(mv[i%m]>dat[i])mv[i%m]=dat[i];
			if(mx[i%m]<dat[i])mx[i%m]=dat[i];
		}
		ans=0;
		sum[0]+=m*100000;
		sum[0]%=m;
		for(i=0;i<m;i++){
			sum[0]+=mv[i];
			sum[0]+=m*1000000000;
			sum[0]%=m;
			mx[i]-=mv[i];
			if(mx[i]>ans)ans=mx[i];
		}
		sum[0]+=m*1000000000;
		sum[0]%=m;
		for(i=0;i<m;i++){
			sum[0]-=ans-mx[i];
			if(sum[0]<=0)break;
		}
		if(sum[0]>0)ans++;
		printf("Case #%d: %lld\n",tc,ans);
	}
}