#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
#define re(i,s,t) for(int i=s;i<=t;i++)

const int inf=~0u>>2;
int t,n;
double a[1001],b[1001];

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);int tt=0;
	while(t--)
	{
		tt++;
		scanf("%d",&n);
		re(i,1,n) scanf("%lf",a+i);
		re(i,1,n) scanf("%lf",b+i);
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);
	    int dw=0,w=0,tmp=1;
		re(i,1,n) 
		{
			bool f=false;
			re(j,tmp,n)
			 if(b[j]>a[i])
			 {
			 	tmp=j+1;f=true;break;
			 }
			if(!f)w++;
		}
        int a1=1,an=n,b1=1,bn=n;
        while(an-a1>=0&&bn-b1>=0)
        {
       	        while(a[an]<b[bn]&&(an-a1>=0&&bn-b1>=0))a1++,bn--;
       	        while(a[an]>b[bn]&&(an-a1>=0&&bn-b1>=0))an--,bn--,dw++;
        }
		printf("Case #%d: %d %d\n",tt,dw,w);
	}
}
