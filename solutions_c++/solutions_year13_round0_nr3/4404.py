#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int map[1001];
bool check(int n)
{
	int a[10];
	int len=0;
	bool ans=true;
	while(n)
	{
		a[len++]=n%10;
		n/=10;
	}
	for(int i=0;i<=len/2;++i)
	{
		if(a[i]!=a[len-1-i]){ans=false;break;}
	}
	return ans;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	memset(map,0,sizeof(map));
	for(int i=1;i*i<=1000;++i)
	{
		map[i*i]=i;
	}
	int c,cas,a,b;
	while(~scanf("%d",&cas))
	{
		c=1;
		while(cas--)
		{
			scanf("%d%d",&a,&b);
			int ans=0;
			for(int i=a;i<=b;++i)
			{
				if(map[i]!=0&&check(i)&&check(map[i]))
				{
					
					++ans;
				}
	//			if(map[i]!=0){cout<<i<<' '<<map[i]<<endl;}
			}
			printf("Case #%d: %d\n",c,ans);
			++c;
		}
	}
	return 0;
}
