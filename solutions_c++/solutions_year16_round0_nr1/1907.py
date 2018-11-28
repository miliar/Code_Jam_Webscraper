#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long LL;
bool f[10];
LL n,tmp;
bool check(LL x)
{
	while (x)
	{
		f[x % 10] = 1;
		x /= 10;
	}
	for(int i=0;i<10;i++)
		if(!f[i]) return 0;
	return 1;
}
int main()
{
	freopen("aa.in","r",stdin);
	freopen("aa.out","w",stdout);
	int numcase;
	cin>>numcase;
	for(int ii=1;ii<=numcase;ii++)
	{
		memset(f,0,sizeof(f));
		cin>>n;
		LL ans = -1;
		for(int i=1;i<=100000;i++)
		{
			if(check(i*n))
			{
				ans = i * n;
				break;
			}
		}
		printf("Case #%d: ",ii);
		if(ans == -1) puts("INSOMNIA");
		else cout<<ans<<endl;
	}
}
