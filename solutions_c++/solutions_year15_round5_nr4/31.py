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

pair<vector<ll>, vector<ll> > ocisti(vector<ll> e, vector<ll> f, ll val)
{
	if(val == 0)
	{
		for(int i=0; i<f.size(); i++)f[i] /= 2;
		return pair<vector<ll>, vector<ll> > (e,f);
	}
	vector<ll> ne, nf;
	int druhy = 0;
	for(int i=0; i<e.size(); i++)
	{
		while(e[druhy] < e[i] + val)druhy++;
		if(f[i] > 0)
		{
			ne.push_back(e[i]);
			nf.push_back(f[i]);
			f[druhy] -= f[i];
		}
	}
	return pair<vector<ll>, vector<ll> >(ne, nf);
}

vector<ll> earliest(vector<ll> element, ll sum)
{
	int n = element.size();
	vector<set<ll> > da_sa(n);
	da_sa[0].insert(0);
	for(int i=1; i<n; i++)
	{
		for(set<ll>::iterator it = da_sa[i-1].begin(); it != da_sa[i-1].end(); it++)
		{
			da_sa[i].insert(*it + element[i-1]);
			da_sa[i].insert(*it - element[i-1]);
		}
	}
	vector<ll> res;
	for(int i = n-1; i>= 0; i--)
	{
		if(da_sa[i].find(sum + element[i]) != da_sa[i].end())
		{
			res.push_back(-element[i]);
			sum += element[i];
		}
		else
		{
			res.push_back(element[i]);
			sum -= element[i];
		}
	}
	db(da_sa.back().size());
	return res;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int test=0; test<t; test++)
	{
		int p;
		scanf("%d",&p);
		vector<ll> e(p),f(p);
		for(int i=0; i<p; i++)
		{
			scanf("%lld",&e[i]);
		}
		for(int i=0; i<p; i++)
		{
			scanf("%lld",&f[i]);
		}
		
		ll sum = e[0] + e.back();
		vector<ll> hodnota;
		while(e.size() > 1 || f[0] > 1)
		{
			ll nval;
			if(f.back() > 1)
			{
				nval = 0;
			}
			else
			{
				nval = e[e.size()-1] - e[e.size()-2];
			}
			hodnota.push_back(nval);
			pair<vector<ll>, vector<ll> > pom = ocisti(e,f,nval);
			e = pom.first;
			f = pom.second;
		}
		db(p);
		vector<ll> sol = earliest(hodnota, sum);
		sort(sol.begin(), sol.end());
		printf("Case #%d:",test+1);
		for(int i=0; i<sol.size(); i++)
		{
			printf(" %lld",sol[i]);
		}
		printf("\n");
	}
	return 0;
}