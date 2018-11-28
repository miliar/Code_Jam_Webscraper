#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define INF 1000000000
double a[1005],b[1005];
bool chk[1005];
main()
{
 	freopen("D-large.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int t;
	scanf("%d",&t);
	int i,j,st,ed;
	int n;
	int win1,win2;
	int tcase=1;
	while(t--)
	{
		memset(chk,0,sizeof chk);
		
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%lf",&a[i]);
		for(i=0;i<n;i++) scanf("%lf",&b[i]);
		
		sort(a,a+n);
		sort(b,b+n);
		
		/*for(i=0;i<n;i++) printf("%.3lf ",a[i]);
		printf("\n");
		for(i=0;i<n;i++) printf("%.3lf ",b[i]);
		printf("\n");*/
		
		win2=n;
		for(i=n-1;i>=0;i--)
		{
			for(j=0;j<n;j++)
			{
				if(b[j]>a[i] && chk[j]==0)
				{ 
					chk[j]=1;
					win2--; 
					break; 
				}
			}
			if(j==n)
			{
				for(j=0;j<n;j++) 
				{
					if(chk[j]==0){ chk[j]=1; break; }
				}
			}
		}
		
		st=0;
		ed=n-1;
		win1=n;
		for(i=0;i<n;i++)
		{
			if(a[i] < b[st]){ win1--; ed--; }
			else st++;
		}
		printf("Case #%d: %d %d\n",tcase++,win1,win2);
	}
}

