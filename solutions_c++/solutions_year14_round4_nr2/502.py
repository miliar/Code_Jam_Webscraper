#include<cstdio>
int que[1010];
int a[1010];
int ans=0,tmp,n,left,right;
int main()
{
	freopen("gcjr2t2.in","r",stdin);freopen("gcjr2t2_3.out","w",stdout);
	int i,j,k,s;
	int t,tt,cnt,maxx,maxp;
	scanf("%d",&tt);
	for(t=1;t<=tt;++t)
	{
		scanf("%d",&n);
		for(i=1;i<=n;++i)
			scanf("%d",a+i);
		left=0;
		right=n+1;
		ans=0;
		for(i=1;i<=n;++i)
		{
			maxx=2000000000;
			for(j=left+1;j<right;++j)
				if(a[j]<maxx)
				{
					maxx=a[j];
					maxp=j;
				}
			if(maxp-left>right-maxp)
			{
				ans+=right-maxp-1;
				for(j=maxp;j<right-1;++j)
				{
					tmp=a[j];
					a[j]=a[j+1];
					a[j+1]=tmp;
				}
				--right;
			}
			else
			{
				ans+=maxp-left-1;
				for(j=maxp;j>left+1;--j)
				{
					tmp=a[j];
					a[j]=a[j-1];
					a[j-1]=tmp;
				}
				++left;
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	//while(1);
	return 0;
}
