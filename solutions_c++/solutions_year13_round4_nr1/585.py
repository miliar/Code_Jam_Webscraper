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
typedef map<int,vpi> miv;

#define sq(x) (x)*(x)
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
#define LL "%I64d"
#define RLL(x) scanf(LL,&(x))

ll mod = 1000002013;

ll calc(int n, int k)
{
	return (k*(2*n-k+1)/2) % mod;
}

struct sss
{
	int a,b,p;
	sss(){}
	sss(int A,int B,int P)
	{
		a=A;
		b=B;
		p=P;
	}
};

bool test(int t)
{
	ll n,m;
	RLL(n),RLL(m);
	ll sum = 0;
	ll answ = 0;;
	vector<pii> v;
	for(int i=0; i<m; ++i)
	{
		int a,b,p;
		scanf("%d%d%d",&a,&b,&p);
		sum = (sum + calc(n,b-a)*p%mod)%mod;
		for(int j=0; j<p; ++j)
			v.push_back(pii(a,b));
	}
	sort(all(v));
	for(int i=0; i<v.size(); ++i)
	{
		int last = i+1;
		int win = i;
		while(true)
		{
			win = i;
			for(; last<v.size() && v[last].first<=v[i].second; ++last)
				if(v[last].second > v[win].second)
					win = last;
			if(win == i)
				break;
			swap(v[i].second,v[win].second);
		}
	}
	for(int i=0; i<v.size(); ++i)
		answ = (answ+calc(n,v[i].second-v[i].first))%mod;
	answ = (sum-answ+mod)%mod;
	printf("Case #%d: %lld\n",t,answ);
	return true;
}

int main()
{
	freopen("a.in","r",stdin);freopen("a.out","w",stdout);
	int n;
	cin>>n;
	for(int i=1; i<=n; ++i)
		test(i);
	return 0;
}