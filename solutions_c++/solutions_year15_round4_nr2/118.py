//*
#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <queue>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <functional>
#define MOD 1000000007
#define MAX ((1<<30)-1)
#define MAX2 ((1ll<<62)-1)
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef set<int>::iterator siit;

int n;
double v, x;
pdd a[200];
double b[200];

int param(double now)
{
	int i, j;
	double tmphab=0;
	double xmin=-1, xmax=-1;
	fill(b, b+n, 0);
	for(i=0;i<n;i++)
	{
		if(tmphab+a[i].second*now < v)
		{
			tmphab+=a[i].second*now;
			b[i]=now;
		}
		else
		{
			b[i]=(v-tmphab)/a[i].second;
			break;
		}
	}
	tmphab=0;
	for(i=0;i<n;i++)
	{
		tmphab+=a[i].first*a[i].second*b[i];
	}
	xmin=tmphab;
	tmphab=0;
	fill(b, b+n, 0);
	for(i=n-1;i>=0;i--)
	{
		if(tmphab+a[i].second*now < v)
		{
			tmphab+=a[i].second*now;
			b[i]=now;
		}
		else
		{
			b[i]=(v-tmphab)/a[i].second;
			break;
		}
	}
	tmphab=0;
	for(i=0;i<n;i++)
	{
		tmphab+=a[i].first*a[i].second*b[i];
	}
	xmax=tmphab;
	if(xmin/(v*x) <= 1.00000000000001 && v*x/xmax <= 1.00000000000001) return 1;
	return 0;
}

int main()
{
	int i, j, k;
	int t, tt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tt);
	for(t=0;t<tt;t++)
	{
		scanf("%d", &n);
		scanf("%lf%lf", &v, &x);
		v*=10000, x*=10000;
		if(t == 96)
		{
			t=t;
		}
		for(i=0;i<n;i++) scanf("%lf%lf", &a[i].second, &a[i].first), a[i].first*=10000, a[i].second*=10000;
		sort(a, a+n);
		double low=0, high=10000000, mid;
		while(high-low > 1e-9)
		{
			mid=(low+high)/2;
			if(param(mid)) high=mid;
			else low=mid;
		}
		printf("Case #%d: ", t+1);
		/*double rx2=(v*x-v*a[0].first)/(a[1].second)/(a[1].first-a[0].first);
		double rx1=(v*x-v*a[1].first)/(a[0].second)/(a[0].first-a[1].first);
		if(n == 2 && rx1 >= 0 && rx2 >= 0 && abs(max(rx1, rx2)-low) > 1e-6) printf("asdiofjweqoifjioewfewf");
		if(n == 1 && a[0].first == x && low > 9999999) printf("asdiofjweqoifjioewfewf");
		if(n == 2 && (a[0].first <= x && x <= a[1].first) && low > 9999999) printf("asdiofjweqoifjioewfewf");
		if(n == 2 && !(a[0].first <= x && x <= a[1].first) && low <= 9999999) printf("asdiofjweqoifjioewfewf");*/
		if(low > 9999999) printf("IMPOSSIBLE\n");
		else printf("%.10lf\n", low);
	}
	return 0;
}
//*/