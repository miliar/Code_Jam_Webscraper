#include<bits/stdc++.h>

int main()
{
	int t,i,j,k,n,p,u,T,m;
	int a[1000000];
	char c[1000000],e;
	scanf("%d",&t);
	for(T=1;T<=t;++T)
	{
		scanf("%s",c);
		n=strlen(c);
		k=0;
		for(i=0;i<(n-1);++i)
		{
			if(c[i]!=c[i+1])
				k++;
		}
		if(c[n-1]=='-')
			k++;
		printf("Case #%d: %d\n",T,k);
	}
	return 0;
}
