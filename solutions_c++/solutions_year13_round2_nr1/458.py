#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
const int N = 105;
typedef __int64 ll;
int a[N];
int main()
{
	int T,x,n,ca=1,i;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&x,&n);
		for(i=1;i<=n;i++)scanf("%d",&a[i]);
		sort(a+1,a+n+1);
		int r=n,cnt=0;
		if(x==1)r=n;
		else
		{
			for(i=1;i<=n;i++)
			{
				int j;
				for(;x<=a[i];)
				{
					x+=(x-1);
					cnt++;
				}
				x+=a[i];
				if(r>cnt+n-i)r=cnt+n-i;
			}
		}
		printf("Case #%d: %d\n",ca++,r);
	}
	return 0;
}