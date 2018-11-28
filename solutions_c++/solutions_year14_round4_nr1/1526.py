#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int a[10005];
bool chk[10005];
main()
{
	freopen("A-large.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int t;
	int n,x;
	int tcase=1;
	scanf("%d",&t);
	while(t--)
	{
		memset(chk,0,sizeof chk);
		scanf("%d %d",&n,&x);
		int i,j;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		int ans=0;
		sort(a,a+n);
		for(i=n-1;i>=0;i--)
		{
			if(chk[i]==true) continue;
			
			chk[i]=true;
			int *p=upper_bound(a,a+n,x-a[i]);
			
			int idx=p-a;
			if(idx==n) idx--;
			
			for(j=idx;j>=0;j--)
			{
				if(!chk[j] && a[i]+a[j]<=x) 
				{
					chk[j]=true;
					ans++;
					break;
				}
			}
			if(j == -1) ans++;
		}
		printf("Case #%d: %d\n",tcase++,ans);
	}
}

