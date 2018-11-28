#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#define pb push_back
#define mp make_pair
#define ST begin()
#define ED end()
#define XX first
#define YY second
#define elif else if 
#define foreach(i,x) for (__typeof((x).ST) i=(x).ST;i!=(x).ED;++i) 
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vci;
typedef vector<string> vcs;
typedef pair<int,int> PII;

const int N = 2005;
const int mo = 1000002013;

int n;
ll m,u;

int check1(ll x)
{
	ll p1=x-1,p2=u-x,s=0;
	if (s>=u-m) return 1;
	for (int i=1;i<=n;++i)
	{
		if (!p2) return 0;
		s+=1LL<<(n-i);
		if (s>=u-m) return 1;
		if (p1&1) --p2;
		p1=(p1+1)/2;
		p2/=2;
	}
	return 0;
}

int check2(ll x)
{
	ll p1=x-1,p2=u-x,s=0;
	if (s>=m) return 1;
	for (int i=1;i<=n;++i)
	{
		if (!p1) return 0;
		s+=1LL<<(n-i);
		if (s>=m) return 1;
		if ((p1&1)==0) --p2;
		p1=(p1-1)/2;
		p2/=2;
	}
	return 0;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int task;
	scanf("%d", &task);
	for (int _i=1;_i<=task;++_i)
	{
		cin>>n>>m;
		u=1LL<<n;
		ll l=1,r=u;
		while (l<r)
		{
			ll x=(l+r+1)>>1;
			if (check1(x))
				l=x;
			else
				r=x-1;
		}
		ll ans1=l-1;
		l=1,r=u;
		while (l<r)
		{
			ll x=(l+r+1)>>1;
			if (check2(x))
				r=x-1;
			else
				l=x;
		}
		ll ans2=l-1;
		
		cout<<"Case #"<<_i<<": "<<ans2<<" "<<ans1<<endl;
	}

	return 0;
}
