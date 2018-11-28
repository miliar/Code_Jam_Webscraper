#include<iostream>
#include<stdio.h>
#define maxn 10000
using namespace std;
int main()
{
    int a[maxn];
    FILE *op=fopen("output.in","w");
   FILE *ip=fopen("B-small-attempt3.in","rt");
	int t,cas=0;
	fscanf(ip,"%d",&t);
	while(t--)
	{
		int max_x=0,n;
		fscanf(ip,"%d",&n);
		for(int i=1;i<=n;i++)
		{
			fscanf(ip,"%d",&a[i]);
			max_x=max(max_x,a[i]);
		}
		int ans=max_x;
		for(int i=1;i<=max_x;i++)
		{
			int now=0,maxx=0;
			for(int j=1;j<=n;j++)
			{
				if(a[j]>i)
				{
					now += (a[j] / i)+((a[j]%i==0)?0:1)-1;
					maxx=max(maxx,i);
				}
				else maxx=max(maxx,a[j]);
			}
			now+=maxx;
			if(now<ans)ans=now;
		}
		fprintf(op,"Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
