#include <cmath>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#ifdef _USE_GMP
#	include "gmpxx.h"
	//typedef mpz_class Int;
	typedef mpf_class Float;
	//typedef double Float;
#else
	typedef double Float;
#endif
using namespace std;
typedef long long ll;

#define ALL(c) (c).begin(),(c).end()
#define SORT(a) sort(a.begin(), a.end())
#define UNIQ(a) a.resize(unique(a.begin(), a.end()) - a.begin())

#define inf 1E9
#define eps 1E-9
#define MAXN 1024

int N, S;
int px[MAXN], py[MAXN], pz[MAXN];
int vx[MAXN], vy[MAXN], vz[MAXN];

Float mint[MAXN][MAXN];
Float maxt[MAXN][MAXN];

Float calc(Float dist)
{
	for(int v=0; v<N; ++v)
		for(int u=v+1; u<N; ++u)
		{
			int xo = px[v] - px[u];
			int yo = py[v] - py[u];
			int zo = pz[v] - pz[u];
			int dx = vx[v] - vx[u];
			int dy = vy[v] - vy[u];
			int dz = vz[v] - vz[u];
			Float a = dx*dx + dy*dy + dz*dz;
			Float b = 2*(xo*dx +yo*dy + zo*dz);
			Float c = xo*xo + yo*yo + zo*zo - dist*dist;
			
			Float d = (b*b - 4*a*c);
			if(d < 0)
			{
				mint[u][v] = maxt[u][v] = mint[v][u] = maxt[v][u] = inf;
			}
			else
			{
				Float t1;
				Float t2;
				if(dx == 0 && dy == 0 && dz == 0)
				{
					if(c < eps)
					{
						t1 = -inf;
						t2 = inf;
					}
					else
					{
						t1 = t2 = inf;
					}
				}
				else
				{
					t1 = (-b - sqrt(d))/(2.0*a);
					t2 = (-b + sqrt(d))/(2.0*a);
/*
					Float x1 = px[v] + vx[v]*t1;
					Float y1 = py[v] + vy[v]*t1;
					Float z1 = pz[v] + vz[v]*t1;
					Float x2 = px[u] + vx[u]*t1;
					Float y2 = py[u] + vy[u]*t1;
					Float z2 = pz[u] + vz[u]*t1;
					Float dd = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2));
					if( 0.1 < abs(dd-dist) )
					{
						print3(dd, dist, (a*t2*t2 + b*t2 + c));
					}
					//print(t1);
*/
				}
				mint[u][v] = mint[v][u] = max(Float(0), t1);
				maxt[u][v] = maxt[v][u] = max(Float(0), t2);
			}
		}
}

// return maxtime
bool solve()
{
	Float curr[MAXN];
	for(int i=1; i<N; ++i)
		curr[i] = inf;
	curr[0] = 0;
	
	stack<int> q;
	q.push(0);
	
	while(!q.empty())
	{
		int v = q.top();
		q.pop();
		for(int u=0; u<N; ++u) if(v!=u)
		{
			if(maxt[v][u]+eps < curr[v])
				continue;
				
			Float t2 = max(curr[v], mint[v][u]);
			if(S+eps < t2-curr[v])
				continue;
			
			if(t2 < curr[u])
			{
				curr[u] = t2;
				q.push(u);
			}
		}
	}
	return curr[1] < inf-eps;
}

int main()
{
	int t;
	
	cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		int n;
		cin >> n >> S;
		N = n;
		for(int i=0; i<n; ++i)
			cin >> px[i] >> py[i] >> pz[i] >> vx[i] >> vy[i] >> vz[i];
		
		//calc(4.0);
		//printa2(mint, N, N);
		//printa2(maxt, N, N);
		
		Float l=0, r = inf;
		while(eps < (r-l))
		{
			Float c = (l+r)/2;
			calc(c);
			bool ok = solve();
			if(ok)
				r = c;
			else
				l = c;
		}
		
		Float ans = l;
		
		//cout << "Case #" << tt << ": " << ans << "\n";
		//cout.flush();
		printf("Case #%d: %.9lf\n", tt, ans);
	}

	return 0;
}
