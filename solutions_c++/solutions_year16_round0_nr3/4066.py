#include<bits/stdc++.h>
using namespace std;
long long m[100];
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.txt","w",stdout);
	long long a,b,c,d,e,f,g,sum,check,T,N,J;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	scanf("%lld %lld %lld",&T,&N,&J);
	printf("Case #1:\n");
	for(a=0,b=1<<(N-2),c=0;a<b&&c<J;a++)
	{
		for(d=2;d<11;d++)
		{
			
			f=1;
			g=a;
			for(e=1;e<N;e++)f*=d;
			sum=f+1;
			f=1;
			while(g)
			{
				f*=d;
				sum+=(g%2)*f;
				g/=2;
			}
			check=1;
			for(e=3;e<=int(sqrt(sum));e++)
			{
				if(sum%e==0)
				{
					m[d]=e;
					check=0;
					break;
				}
			}
			if(check)break;
		}
		if(check==0)
		{
			printf("1");
			for(d=1<<(N-3);d;d/=2)printf("%lld",d&a?1:0);
			printf("1 ");
			for(d=2;d<11;d++)printf("%lld ",m[d]);
			printf("\n");
			c++;
		}
	}
}
