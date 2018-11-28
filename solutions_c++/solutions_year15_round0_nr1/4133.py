#include<bits/stdc++.h>
int main()
{
	int t,i,j,k,l,a,b;
	char c[10000],d;
	scanf("%d",&t);
	int T;
	for(T=1;T<=t;++T)
	{
		scanf("%d%c",&k,&d);
		scanf("%s",c);
		a=c[0]-48;
		b=0;
		for(i=1;i<=k;++i)
		{
			if(a<i)
			{
				b+=i-a;
				a=i+c[i]-48;
			}
			else
				a+=c[i]-48;
		}
		printf("Case #%d: %d\n",T,b);
	}
	return 0;
}
