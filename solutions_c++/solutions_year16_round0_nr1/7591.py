#include <stdio.h>
int ans[1000006];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,i;
	int a[10],c;
	//scanf("%d",&t);
	t=1000000;
	int cas;
	for(cas=1;cas<=t;cas++)
	{
		//scanf("%d",&n);
		n=cas;
		for(i=0;i<10;i++)a[i]=0;
		c=10;
		int N=n;
		while(c>0)
		{
			int m=n;
			while(m>0)
			{
				if(a[m%10]==0)
				{
					a[m%10]=1;
					c--;
				}
				m/=10;
			}
			if(c==0)break;
			n+=N;
		}
		ans[cas]=n;
	}
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		scanf("%d",&n);
		if(n==0)printf("Case #%d: INSOMNIA\n",cas);
		else
		printf("Case #%d: %d\n",cas,ans[n]);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
