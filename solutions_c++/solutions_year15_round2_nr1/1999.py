#include<bits/stdc++.h>

int main()
{
	int t,i,j,k,n,p,u,T,m;
	int a[1000001]={0};
	a[0]=0;
	char c[1000000],e;
	for(i=1;i<1000001;++i)
	{
		if(!a[i])
		{
			a[i]=1+a[i-1];
			p=i;
			u=0;
			while(p)
			{
				u=u*10+p%10;
				p=p/10;
			}	
			if(u>i)
			{
				a[u]=a[i]+1;

			}
		}
		else
		{
			p=a[i-1]+1;
			if(p<a[i])
				a[i]=p;
		}
	}
	scanf("%d",&t);
	for(T=1;T<=t;++T)
	{
		scanf("%d",&n);
		
		printf("Case #%d: %d\n",T,a[n]);
	}
	return 0;
}
