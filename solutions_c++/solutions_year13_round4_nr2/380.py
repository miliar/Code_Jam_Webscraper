#include<iostream>
#include<cstdio>

using namespace std;

const int maxn=10000;
long long n,m,x,y,xx,yy,num;
long long e[maxn];
void prepare()
{
	e[0]=1;
	for (int i=1; i<=50; i++) e[i]=e[i-1]*2;
	e[0]=1;
}
void solve()
{
	xx=x; yy=y;
	if (y==e[x])
	{
		cout<<e[x]-1<<" ";
	} 
	else
	{
		long long ans1=0;
		int tt=x-1;
		while (y>e[tt])
		{
			ans1+=e[x-tt-1];
			y-=e[tt--];
		}
		ans1+=e[x-tt-1];
		ans1-=1;
		cout<<ans1<<" ";
	}
	
	long long ans2=0;

	ans2 = 0;  long long tmp = e[x - 1];
	for (long long i = 1; i + i <= yy; i += i) {
		ans2 += tmp; tmp /= 2;
	}

	cout<<ans2<<endl;
}
void init()
{
	int ca=0;
	prepare();
	cin>>num;
	while (num--)
	{
		printf("Case #%d: ",++ca);
		cin>>x>>y;
		solve();
	}
}
int main()
{
	freopen("a.out","w",stdout);
	init();
	return 0;
}
