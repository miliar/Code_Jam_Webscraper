#include<cstdio>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstdlib>
using namespace std;

#define inf 1023456789
#define linf 1023456789123456789ll
#define pii pair<int,int>
#define pipii pair<int, pii >
#define pll pair<long long,long long>
#define vint vector<int>
#define vvint vector<vint >
#define ll long long
#define pdd pair<double, double>

#define DEBUG
#ifdef DEBUG
#define db(x) cerr << #x << " = " << x << endl
#else
#define db(x)
#endif

ll d;
vector<ll> s, otec, m;
vector<vector<int> > syn;

vector<pll > event;

vector<ll> ministack, maxistack;

void dfs(int a)
{
	bool namini = 0, namaxi = 0;
	if(s[a] < ministack.back())
	{
		ministack.push_back(s[a]);
		namini = 1;
	}
	if(s[a] > maxistack.back())
	{
		maxistack.push_back(s[a]);
		namaxi = 1;
	}
	if(maxistack.back()-d <= ministack.back())
	{
		event.push_back(pll(maxistack.back() - d, -1));
		event.push_back(pll(ministack.back(), 1));
	}
	for(int i=0; i<syn[a].size(); i++)
	{
		dfs(syn[a][i]);
	}
	if(namaxi)maxistack.pop_back();
	if(namini)ministack.pop_back();
}

int main()
{
	ministack.push_back(linf);
	maxistack.push_back(-linf);
	int t;
	scanf("%d",&t);
	for(int test=0; test<t; test++)
	{
		ll n;
		scanf("%lld %lld",&n,&d);
		s = vector<ll> (n);
		otec = vector<ll> (n,-1);
		m = vector<ll> (n);
		syn = vvint(n);
		ll s0, as, cs, rs;
		scanf("%lld %lld %lld %lld",&s0, &as, &cs, &rs);
		s[0] = s0;
		for(int i=1; i<n; i++)
		{
			s[i] = (s[i-1] * as + cs) % rs;
		}
		ll m0, am, cm, rm;
		scanf("%lld %lld %lld %lld",&m0, &am, &cm, &rm);
		m[0] = m0;
		for(int i=1; i<n; i++)
		{
			m[i] = (m[i-1] * am + cm) % rm;
			otec[i] = m[i] % i;
			syn[otec[i]].push_back(i);
		}
		otec[0] = -1;
		event.clear();
		dfs(0);
		db(event.size());
		sort(event.begin(), event.end());
		int poc = 0, res = 0;
		for(int i=0; i<event.size(); i++)
		{
			poc += event[i].second;
			
			res = max(res, -poc);
		}
		printf("Case #%d: %d\n",test+1, res);
	}
	return 0;
}