#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<set>
#include<cstdlib>
#include<ctime>
using namespace std;
typedef long long LL;
char ch[10000];
int p[100]={2,3,5,7,11,13,17,19,23,29,31,37,41};
int a[100],ans[12];
int n,numcase,num;
set<LL> ss;
bool MOD(LL jz,LL mod)
{
	LL tmp = 0;
	for(int i=n-1;i>=0;i--)
	{
		tmp = (tmp * jz + a[i]) % mod;
	}
	return tmp == 0;
}
bool check(LL x)
{
	LL bak = x;
	a[0] = 1;
	a[n-1] = 1;
	for(int i=1;i<=n-2;i++)
	{
		a[i] = x % 2;
		x/=2;
	}
	for(LL jz = 2;jz<=10;jz++)
	{
		ans[jz] = -1;
		for(int k=0;k<=12;k++)
		{
			if(MOD(jz,p[k])) ans[jz] = p[k];
		}
		if(ans[jz] == -1) return 0;
	}
	for(int i=n-1;i>=0;i--) cout<<a[i];
	for(int i=2;i<=10;i++) cout<<' '<<ans[i];
	cout<<endl;
	return 1;
}
int main()
{
	srand(time(NULL));
	freopen("cc.in","r",stdin);
	freopen("cc.out","w",stdout);
	cin>>numcase;
	for(int ii=1;ii<=numcase;ii++)
	{
		scanf("%d%d",&n,&num);
		printf("Case #%d:\n",ii);
		ss.clear();
		for(int i=1;i<=num;i++)
		{
			while (true)
			{
				LL tmp = rand() % (1LL<<(LL)(n-2));
				if(ss.find(tmp) == ss.end())
				{
					ss.insert(tmp);
					if(check(tmp))  break;
				}
			}
		}
	}
}
