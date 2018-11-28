#include<stdio.h>
#include<conio.h>
int main()
{
	int i,t,n,j,k,s,l;
	long a[1000],b[1000];
	long long m=0;
	freopen("A-large-practice.in","rt",stdin);
	freopen("alarge.out","wt",stdout);
	scanf("%d",&t);
	for(l=0;l<t;l++)
	{
		scanf("%d",&n);
		for(j=0;j<n;j++)
			scanf("%d",&a[j]);
		for(j=0;j<n;j++)
			scanf("%d",&b[j]);
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(a[i]>a[j])
				{
					k=a[i];
					a[i]=a[j];
					a[j]=k;
				}
				if(b[i]<b[j])
				{
					s=b[i];
					b[i]=b[j];
					b[j]=s;
				}
			}
		}
		for(j=0;j<n;j++)
			m+=(long long)(a[j])*b[j];
		printf("case #%d: %lld",l+1,m);
		m=0;
		printf("\n");
	}
	return 0;
}
