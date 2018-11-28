#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int T,n,a[1010],b[1010],ans;

int main()
{
	scanf("%d",&T);
	for (int tc=1;tc<=T;tc++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
			scanf("%d",&a[i]);
		int maxx=-1,maxpos=0;
		ans=0;
		int L=1,R=n;
		for (int i=1;i<=n;i++)
		{
			int minn=1100000000,minpos=0;
			for (int j=L;j<=R;j++)
				if (a[j]<minn) minn=a[j],minpos=j;
			if (minpos-L<=R-minpos)
			{
				for (int j=minpos;j>L;j--) a[j]=a[j-1],ans++;
				a[L++]=minn;
			}else
			{
				for (int j=minpos;j<R;j++) a[j]=a[j+1],ans++;
				a[R--]=minn;
			}
		}
		printf("Case #%d: %d\n",tc,ans);
	}

	return 0;
}