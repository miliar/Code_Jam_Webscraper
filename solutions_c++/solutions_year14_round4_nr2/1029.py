#include "stdio.h"
#include "string.h"
#define M 500100
int n;
__int64 c[M],a[M],b[M];
__int64 ans;
void Merge(int i,int p,int q)
{
	int j,k;
	for(j=p,k=i;i<=p-1 && j<=q-1;k++)
	{
		if(a[i]<a[j]) b[k]=a[i++];
		else {ans+=p-i;b[k]=a[j++];}
	}
	for(;i<=p-1;i++) b[k++]=a[i];
	for(;j<=q-1;j++) b[k++]=a[j];
}
int main()
{
	while(scanf("%d",&n)==1)
	{
		if(!n) break;
		ans=0;
		int i,j;
		for(i=1;i<=n;i++)
			scanf("%I64d",&a[i]);
		int k=1,p,q;
		int lim=0;
		while(1)
		{
			i=1;
			lim=0;
			while(i<=n)
			{
				p=i+k;
				q=i+2*k;
				if(i==n) {b[i]=a[i];lim++;break;}
				if(q>n) q=n+1;
				Merge(i,p,q);
				lim++;
				i=q;
			}
			memcpy(a,b,sizeof(a));
			k=2*k;
			if(lim==1) break;
		}
		printf("%I64d\n",ans);
	}
	return 0;
}
