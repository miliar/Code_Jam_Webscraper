#pragma comment(linker, "/STACK:65000000")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef vector<pii> vpi;

#define sq(x) (x)*(x)
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
#define LL "%I64d"
#define RLL(x) scanf(LL,&(x))

ll rev(ll a)
{
	ll b=0;
	while(a)
	{
		b=10*b+a%10;
		a/=10;
	}
	return b;
}

bool ispal(ll a)
{
	return a==rev(a);
}

void test(ll t)
{
	ll a,b;
	cin>>a>>b;
	ll answ = 0;
	for(ll x = 0; x*x<=b; ++x)
		if(x*x>=a)
		{
			if(ispal(x) && ispal(x*x))
				++answ;
		}
	printf("Case #%lld: %lld\n",t,answ);
}

int main()
{
	freopen("c.in","r",stdin);freopen("c.out","w",stdout);
	int n;
	cin>>n;
	for(int i=0; i<n; ++i)
		test(i+1);
	return 0;
}