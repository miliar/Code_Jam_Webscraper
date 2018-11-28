#include <stdio.h>
int GCD(long long a, long long b)
{
	while(b!=0)
	{
		long long tmp=a%b;
		a=b;
		b=tmp;
	}
	return a;
}
int main()
{
	long long table[1+40];
	table[0]=1;
	for(int t=1;t<=40;t++)
		table[t]=table[t-1]*2;

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		long long P,Q,R;
		int k=-1,x;
		scanf("%lld/%lld",&P,&Q);
		R=GCD(P,Q);
		P/=R;
		Q/=R;
		for(int i=0;table[i]<=Q;i++)
			if(table[i]==Q)
				k=i;
		if(k==-1)
		{
			printf("Case #%d: impossible\n",t);
			continue;
		}
		for(int i=0;i<=40;i++)
			if(P&table[i])
				x=i;
		printf("Case #%d: %d\n",t,k-x);
	}
	return 0;
}
