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

pdd combine(vector<pdd >& a)
{
	if(a.size() == 0)
	{
		return pdd(0,0);
	}
	double v=0, st = 0;
	for(int i=0; i<a.size(); i++)
	{
		v += a[i].second;
		st += a[i].first * a[i].second;
	}
	return pdd(st/v, v);
}

int main()
{
	int t;
	cin >> t;
	for(int test=0; test<t; test++)
	{
		int n;
		double v,x;
		cin >> n >> v >> x;
		vector<pair<double, double> > tap(n);
		for(int i=0; i<n; i++)
		{
			cin >> tap[i].second >> tap[i].first;
			tap[i].first -= x;
		}
		sort(tap.begin(), tap.end());
		
		printf("Case #%d: ",test+1);
		if((tap[0].first * tap.back().first) > 0)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		
		pdd pom = combine(tap);
		
		if(pom.first < 0)
		{
			for(int i=0; i < n-1-i; i++)
			{
				swap(tap[i], tap[n-1-i]);
			}
			for(int i=0; i<n; i++)
			{
				tap[i].first *= -1;
			}
		}
		while(1)
		{
			pdd posl = tap.back();
			tap.pop_back();
			pom = combine(tap);
			if(pom.first <= 0)
			{
				double lo = 0, hi = 1;
				for(int i=0; i<60; i++)
				{
					double mid = (lo+hi)/2;
					pdd pomtap(posl.first, posl.second*mid);
					vector<pdd > pomv(2);
					pomv[0] = pom;
					pomv[1] = pomtap;
					if(combine(pomv).first <= 0)lo = mid;
					else hi = mid;
				}
				pdd pomtap(posl.first, posl.second*hi);
				tap.push_back(pomtap);
				pom = combine(tap);
				break;
			}
		}
		printf("%.20lf\n", v/pom.second);
	}
	return 0;
}