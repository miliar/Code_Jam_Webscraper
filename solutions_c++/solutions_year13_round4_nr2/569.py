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

ll n,p;
ll dd;

bool test(int t)
{
	cin>>n>>p;
	//p;
	ll a=1,b=1;
	ll d =(ll)1<<n;
	while(d>p)
	{
		d/=2;
		b*=2;
	}
	d =(ll)1<<n;
	b = d-b;
	
	p = d - p;
	while(d>p)
	{
		d/=2;
		a*=2;
	}
	d =(ll)1<<n;
	a = a-2;
	if(p==0)
		a = d-1;
	printf("Case #%d: %lld %lld\n",t,a,b);
	return true;
}

int main()
{
	freopen("b.in","r",stdin);freopen("b.out","w",stdout);
	int n;
	cin>>n;
	for(int i=1; i<=n; ++i)
		test(i);
	return 0;
}