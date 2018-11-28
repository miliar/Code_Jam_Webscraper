#include<iostream>
#include<cstdio>

using namespace std;

const int maxn=11000;
const long long mo=1000002013;

struct data
{
	long long x,y;
	bool operator < (const data a) const
	{
		return x<a.x;
	}
};

long long num,n,m,x,y,z,ans1,ans2;
data a[maxn],b[maxn];

long long calc(int x)
{
	long long tmp1=n,tmp2=n-x+1; 
	return (((tmp1+tmp2)*x/2)%mo);
}
void solve()
{
	ans2=0;
	sort(a+1,a+m+1);
	sort(b+1,b+m+1);

	int tt=0;
	int t1=0,t2=0;
	while ((t1!=m) || (t2!=m))
	{
		++t2;
		while ((t1+1<=m) && (a[t1+1].x<=b[t2].x)) ++t1;	
		
		for (int i=t1; i>=1; i--)
		{
			long long t=min(b[t2].y,a[i].y);
			a[i].y-=t; b[t2].y-=t;
			long long k=calc(b[t2].x-a[i].x+1);
			ans2=(ans2+(k*t)%mo)%mo;
			if (b[t2].y==0) break;
		}
	}

	cout<<(ans1-ans2+mo)%mo<<endl;
}	
void init()
{

	int ca=0;
	cin>>num;
	while (num--)
	{
		ans1=0;
		cin>>n>>m;
		printf("Case #%d: ", ++ca);
		for (int i=1; i<=m; i++)
		{
			cin>>x>>y>>z;
			a[i].x=x; a[i].y=z;
			b[i].x=y; b[i].y=z;
			long long k=calc(y-x+1);
			ans1=(ans1+(k*z)%mo)%mo;
		}
		solve();
	}
}
int main()
{
	freopen("a.out","w",stdout);
	init();
	return 0;
}
