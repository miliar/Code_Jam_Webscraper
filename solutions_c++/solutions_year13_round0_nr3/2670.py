#include <stdio.h>
#include <math.h>
int T;
long long a,b,ans;
int num[100];
int Check(long long x)
{
	int m=0;
	long long tx,i;
	for(tx=x;tx;tx/=10)
		num[++m]=tx%10;
	for(i=1;i+i<=m;++i)
		if(num[i]!=num[m-i+1])
			return 0;
	m=0;
	for(tx=x*x;tx;tx/=10)
		num[++m]=tx%10;
	for(i=1;i+i<=m;++i)
		if(num[i]!=num[m-i+1])
			return 0;
	return 1;
}
int main()
{
	long long i,j;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(int Ti=1;Ti<=T;++Ti)
	{
		#ifdef WIN32
			scanf("%I64d%I64d",&a,&b);
		#else
			scanf("%lld%lld",&a,&b);
		#endif
		ans=0;
		for(i=(long long)sqrt((double)(a-1));i*i<=b;++i)
		if(a<=i*i && i*i<=b)
			if(Check(i))
				++ans;
		#ifdef WIN32
			printf("Case #%d: %I64d\n",Ti,ans);
		#else
			printf("Case #%d: %lld\n",Ti,ans);
		#endif
	}
	return 0;
}
