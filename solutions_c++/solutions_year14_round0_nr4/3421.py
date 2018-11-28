#include <cstdio>
#include <algorithm>

#define eps 1e-7

using namespace std;

double ken [1001],naomi[1001];
long n,tc,i,j;

bool cmp (double a, double b)
{
	return a-b>eps;
}

int main () {
	
	freopen("war.in","r",stdin);
	freopen("war.out","w",stdout);
	
	scanf("%ld",&tc);
	long k=0;
	while(tc--)
	{
		k++;
		scanf("%ld",&n);
		
		for(i=1;i<=n;i++)
			scanf("%lf",&naomi[i]);
		for(i=1;i<=n;i++)
			scanf("%lf",&ken[i]);
		sort(naomi+1,naomi+n+1);
		sort(ken+1,ken+n+1,cmp);
		long un=n,pn=1,uk=n,pk=1;
		long nrw=0;
		
		while(1)
		{
			
			
			if(naomi[un]-ken[pk]>eps)
			{
				nrw++;
				un--;
				pk++;
			}
			else if(ken[pk]-naomi[pn]>eps)
			{
				pn++,pk++;
			}
			if(pk>uk)
				break;
			if(pn>un)
				break;
		}
		
		sort(ken+1,ken+n+1);
		
		long nrp=0;
		long fk[1001];
		memset(fk,0,sizeof(fk));
		for(i=1;i<=n;i++)
			for(j=i;j<=n;j++)
				if(ken[j]-naomi[i]>eps && fk[j]==0){
					fk[j]=1;
					break;
				}
		for(i=1;i<=n;i++)
			if(fk[i]==0)
				nrp++;
		printf("Case #%ld: %ld %ld\n",k,nrw,nrp);
	}
	return 0;
}
