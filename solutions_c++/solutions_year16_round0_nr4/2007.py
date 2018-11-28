#include<cstdio>
#include<iostream>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

typedef long long LL;

int k,c,s;

int T;
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	scanf("%d",&T);
	for(int Ti=1; Ti<=T; Ti++)
	{
		printf("Case #%d: ",Ti);
		
		scanf("%d %d %d",&k,&c,&s);
		if (k>c*s) {printf("IMPOSSIBLE\n"); continue;}
		
		LL ans=0;
		fo(i,1,k)
		{
			ans=max(ans-1,(LL)0)*k+i;
			if (i%c==0)
			{
				printf("%I64d ",ans);
				ans=0;
			}
		}
		if (ans) printf("%I64d ",ans);
		printf("\n");
	}
}