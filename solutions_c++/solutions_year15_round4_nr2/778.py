#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <cassert>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef pair<int,P> P1;
typedef pair<P,P> P2;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-12
#define INF 1000000000
#define fi first
#define sc second
#define rep(i,x) for(int i=0;i<x;i++)
#define SORT(x) sort(x.begin(),x.end())
#define ERASE(x) x.erase(unique(x.begin(),x.end()),x.end())
#define POSL(x,v) (lower_bound(x.begin(),x.end(),v)-x.begin())
#define POSU(x,v) (upper_bound(x.begin(),x.end(),v)-x.begin())
#define double long double
int main()
{
	int t; cin >> t;
	for(int q=1;q<=t;q++)
	{
		printf("Case #%d: ",q);
		int n; double c,x;
		cin >> n >> c >> x; 
		double v[105],r[105];
		pair<double,double>hoge[105];
		for(int i=0;i<n;i++)
		{
			cin >> v[i] >> r[i];
			hoge[i] = make_pair(r[i],i);
		}
		if(n == 1)
		{
			if(r[0] != x) cout << "IMPOSSIBLE" << endl;
			else cout << fixed << setprecision(9) << c/v[0] << endl;
		}
		else
		{
			double lb = 0.0;
			double ub = 1e8;
			double mid;
			sort(hoge,hoge+n);
			for(int t=0;t<1000;t++)
			{
				mid = (lb+ub)/2;
				double suma=0,sumb=0;
				for(int i=0;i<2;i++)
				{
					if(suma+v[i]*mid <= c)
					{
						suma += v[i]*mid;
						sumb += v[i]*r[i]*mid;
					}
					else
					{
						double zan = c-suma;
						suma += zan;
						sumb += zan*r[i];
					}
				}
				sumb /= c;
				double sumc=0,sumd=0;
				for(int i=1;i>=0;i--)
				{
					if(sumc+v[i]*mid <= c)
					{
						sumc += v[i]*mid;
						sumd += v[i]*r[i]*mid;
					}
					else
					{
						double zan = c-sumc;
						sumc += zan;
						sumd += zan*r[i];
					}
				}
				sumd /= c;
				if(min(sumd,sumb) <= eps+x && x-eps <= max(sumd,sumb)) ub = mid;
				else lb = mid;
				
			}
			
			if(mid < 9e7) cout << fixed << setprecision(9) << mid << endl; else cout << "IMPOSSIBLE" << endl;
		}
	}
}