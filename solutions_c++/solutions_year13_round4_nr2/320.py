#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
int n;
LL p;
LL calc1(LL now,LL w,int n){
	if(n==0)return now;
	n--;
	if(w==0){
		return calc1(now-(1LL<<n),0,n);
	}
	else{
		return calc1(now,(w-1)>>1,n);
	}
}
bool ok1(LL k)
{
	LL rank=calc1((1LL<<n),k,n);
	return rank > p;
}

LL calc2(LL now,LL b,int n){
	if(n==0)return now;
	n--;
	if(b==0){
		return calc2(now+(1LL<<n),0,n);
	}
	else{
		return calc2(now,(b-1)>>1,n);
	}
}
bool ok2(LL k)
{
	LL rank=calc2(1,(1LL<<n)-1-k,n);
	return rank <= p;
}
LL bs2()
{
	LL low=0,up=(1LL<<n)-1;
	while(low<=up)
	{
		LL mid=low+up>>1;
		if(ok2(mid))low=mid+1;
		else up=mid-1;
	}
	return up;
}
LL bs1()
{
	if(p==1)return 0;
	LL low=0,up=(1LL<<n)-1;
	while(low<=up)
	{
		LL mid=low+up>>1;
		if(ok1(mid))up=mid-1;
		else low=mid+1;
	}
	return low-1;
}
int main()
{
	int T,w=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%lld",&n,&p);
		LL ans1=bs1(),ans2=bs2();
		//for(int i=0;i<8;i++)
		//	printf("%lld\n",calc2(1,(1LL<<n)-i-1,n));
		printf("Case #%d: %lld %lld\n",w++,ans1,ans2);
	}
}
