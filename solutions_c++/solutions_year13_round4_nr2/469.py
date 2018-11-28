#include<cstdio>

int T;

long long n,k;
long long l,r,ans;

long long chk_max(long long v){
	long long better=v;
	long long win=n,lose=0;
	while(better){
		win--; lose++;
		better=(better-1)/2;
	}
	long long res=0;
	for(int i=0;i<win;i++)
		res=res*2+1;
	return (1LL<<n)-res;
}
long long chk_min(long long v){
	long long worse=(1LL<<n)-1-v;
	long long win=0,lose=n;
	while(worse){
		win++; lose--;
		worse=(worse-1)/2;
	}
	long long res=0;
	for(int i=0;i<win;i++)
		res=res*2+1;
	for(int i=0;i<lose;i++)
		res=res*2;
	return (1LL<<n)-res;
}

int main(){
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%I64d%I64d",&n,&k);

		printf("Case #%d: ",_);

		l=0;r=(1LL<<n)-1;
		ans=0;
		while(l<=r){
			long long mid=(l+r)>>1;
			if(chk_max(mid)<=k){
				ans=mid;l=mid+1;
			}else r=mid-1;
		}
		printf("%I64d ",ans);

		l=0;r=(1LL<<n)-1;
		ans=1LL<<n;
		while(l<=r){
			long long mid=(l+r)>>1;
			if(chk_min(mid)>k){
				ans=mid;r=mid-1;
			}else l=mid+1;
		}
		printf("%I64d\n",ans-1);
	}

	return 0;
}