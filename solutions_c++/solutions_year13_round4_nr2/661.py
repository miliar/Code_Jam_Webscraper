#include<stdio.h>

long long bit[100],n;

void set()
{
	bit[0]=1;
	for(int i=1;i<=60;i++)bit[i]=bit[i-1]*2;
}

long long rev(int x)
{
	long long tmp=0;
	for(int i=n;i>=1;i--){
		if(x%2==1){
			tmp+=bit[i-1];
		}
		x/=2;
	}
	return tmp;
}

void solve()
{
	long long p,su,ans1=0,ans2=0;
	scanf("%lld%lld",&n,&p);
	su=p;
	if(bit[n]==p){
		printf("%lld %lld\n",bit[n]-1,bit[n]-1);
		return;
	}
	for(int i=n-1;i>=0;i--){
		if(bit[i]<su){
			ans1+=bit[n-i];
			su-=bit[i];
		}
		else break;
	}
	for(int i=1;i<=n;i++){
		if(p<bit[i]){
			ans2=bit[i-1]-1;
			ans2=rev(ans2);
			break;
		}
	}
	printf("%lld %lld\n",ans1,ans2);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t;
	set();
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}