#include<stdio.h>
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long int t,i=1;
	scanf("%lld",&t);
	while(i<=t)
	{
		long long int s,j,T=0,e=0;
		char a;
		scanf("%lld",&s);
		a=getchar();
		for(j=0;j<=s;j++)
		{
			a=getchar();
			if(j<=T)
			{
				T=T+(a-'0');
			}
			else
			{
				e=e+(j-T);
				T=T+(j-T);
				T=T+(a-'0');
			}
		}
		printf("Case #%lld: %lld\n",i,e);
		i++;
	}
	return 0;
}
