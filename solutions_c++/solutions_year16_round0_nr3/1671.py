#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<set>
#include<cstdlib>
#include<ctime>
#include<cmath>
using namespace std;
int prime[20]={2,3,5,7,11,13,17,19,23,29,31};
int a[100],ans[12];
int n,cnt,s;
set<long long> ss;
bool work(long long p,long long m)
{
	long long x = 0;
	for(int i=n-1;i>=0;i--)
	{
		x = (x * p + a[i]) % m;
	}
	if (x == 0) return 1;
	return 0;
}
int check(long long x)
{
	for(int i=1;i<=n-2;i++)
	{
		a[i] = x % 2;
		x/=2;
	}
	a[0] = 1;
	a[n-1] = 1;
	for(int p = 2;p<=10;p++)
	{
		bool flag = false;
		for(int k=0;k<=10;k++)
		{
			if(work(p,prime[k])) 
			{
				ans[p] = prime[k];
				flag = 1;
				break;
			}
		}
		if(flag == false) return 0;
	}
	for(int i=n-1;i>=0;i--) printf("%d",a[i]);
	for(int i=2;i<=10;i++) printf(" %d",ans[i]);
	puts("");
	return 1;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("ans_c_large.out","w",stdout);
	cin>>cnt;
	for(int e=1;e<=cnt;e++)
	{
		cin>>n>>s;
		printf("Case #%d:\n",e);
		ss.clear();
		for(int i=1;i<=s;i++)
		{
			for(;;)
			{
				long long t = rand() % (long long)(pow(2,n-2));
				if(ss.find(t) == ss.end())
				{
					ss.insert(t);
					if(check(t))  break;
				}
			}
		}
	}
}
