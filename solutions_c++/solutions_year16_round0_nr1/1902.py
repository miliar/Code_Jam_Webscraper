#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int f[10];
long long n,tmp;
int work(long long x)
{
	while (x)
	{
		f[x % 10] = 1;
		x /= 10;
	}
	for(int i=0;i<10;i++)
		if(f[i]==0) return 0;
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ans_large.out","w",stdout);
	int cnt;
	cin>>cnt;
	for(int e=1;e<=cnt;e++)
	{
		memset(f,0,sizeof(f));
		cin>>n;
		long long ans = 0;
		for(int i=1;i<=100000;i++)
		{
			if(work(i*n))
			{
				ans = i * n;
				break;
			}
		}
		printf("Case #%d: ",e);
		if(!ans) puts("INSOMNIA");
		else cout<<ans<<endl;
	}
}
