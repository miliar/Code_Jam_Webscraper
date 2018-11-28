#include<stdio.h>
using namespace std;

static char s[2005];
static int a[2005];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output1large.txt","w",stdout);
	int t,m,x,y;
	
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		scanf("%d",&m);
		scanf("%s",s);
		for(int i=0;i<m+1;i++)
		{
			a[i]=int(s[i])-48;
			
		}
		
		int pre=a[0];
		a[0]=0;
		for(int i=1;i<m+1;i++)
		{
			x=a[i];
			a[i]=pre;
			pre+=x;
		}
		for(int i=0;i<m+1;i++)
		{
			a[i]=i-a[i];
		}
		int max=0;
		for(int i=0;i<m+1;i++)
		{
			if(max<a[i])max=a[i];
		}
		printf("Case #%d: %d\n",k,max);
	}
}
