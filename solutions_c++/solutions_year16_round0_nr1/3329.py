#include <bits/stdc++.h>
int allSet(long long flag[])
{
	for(int i=0;i<10;i++)
		if(!flag[i])
			return 0;
	return 1;
}
void setFlag(long long flag[],int x)
{
	while(x!=0)
	{
		flag[x%10]=1;
		x/=10;
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	long long t,n,i,T,flag[10],v;
	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%lld",&n);
		if(n==0)
			printf("Case #%lld: INSOMNIA\n",t);
		else
		{
			v=0;
			memset(flag,0,sizeof(long long)*10);
			do
			{
				v=v+n;
				setFlag(flag,v);
			}while(!allSet(flag));
			printf("Case #%lld: %lld\n",t,v);
		}
	}
	return 0;
}