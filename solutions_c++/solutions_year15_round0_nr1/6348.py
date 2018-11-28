#include<cstdio>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("OutputA.out","w",stdout);
	int t,n,i,j,ans,tot,max;
	scanf("%d",&t);
	for (j=1;j<=t;j++)
	{
		scanf("%d",&n);
		char a[n+2];
		scanf("%s",a);
		max=0;
		tot=a[0]-48;
		for (i=1;a[i];i++)
		{
			if (tot<=i)
				if (max<i-tot)
					max=i-tot;
			tot+=a[i]-48;
		}
		printf("Case #%d: %d\n",j,max);
	}
	return 0;
}
