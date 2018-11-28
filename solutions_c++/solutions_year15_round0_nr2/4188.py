#include <stdio.h>
#include <stdlib.h>
using namespace std;

int Case,T,n,m,i,j,k,ans;
int a[1005];

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&T);
	for(Case=1;Case<=T;++Case)
	{
		scanf("%d",&n);
		ans=0x7fffffff;
		for(i=1;i<=n;++i)scanf("%d",&a[i]);
		for(i=1;i<=1000;++i)
		{
			k=i;
			for(j=1;j<=n;++j)if(a[j]>i)k+=(a[j]-i)/i+((a[j]-i)%i>0);
			if(k<ans)ans=k;
		}
		printf("Case #%d: %d\n",Case,ans);
	}
}
