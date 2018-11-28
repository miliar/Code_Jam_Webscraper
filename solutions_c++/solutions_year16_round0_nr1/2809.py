#include<bits/stdc++.h>
using namespace std;

int T,t,n,i,j,k,l,p;
bool v[11];

int main()
{ 
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int ca=0;
	for(scanf("%d",&T);T;T--)
	{
		scanf("%d",&n);
		printf("Case #%d: ",++ca);
		if(n==0)printf("INSOMNIA\n");
		else
		{
			bool ok=0;
			p=0;memset(v,0,sizeof(v));
			for(int i=1;i<=100000;i++)
			{
				int g=n*i;
				for(;g;g/=10)
				if(!v[g%10])v[g%10]=1,p++;
				if(p==10)
				{
					printf("%d\n",n*i);ok=1;break;
				}
			}
			if(!ok)printf("INSOMNIA\n");
		}
				
	}
	return 0;
} 
