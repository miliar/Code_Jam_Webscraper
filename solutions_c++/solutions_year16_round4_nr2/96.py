#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:32000000")
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

double solve(const vector<double>& a)
{
	int n = SZ(a);
	static double d[256];
	CLEAR(d);
	d[0]=1.0;
	REP(j,n)
	{
		double p = a[j];
		REPD(x,n+1)
		{
			d[x] = d[x]*(1-p);
			if (x>0)
				d[x] += d[x-1]*p;
		}
	}
	return d[n/2];
}

int n,k;
double a[256];

int main(int argc, char **argv)
{
	string FN = "B-large";
	if (argc>1) FN = string(argv[1]);
	int shift = 0;
	if (argc>2) sscanf(argv[2],"%d",&shift);
	freopen((FN+".in").c_str(),"r",stdin);
	freopen((FN+".out").c_str(),"w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"=== %s : %d\n", FN.c_str(), test+shift);
		printf("Case #%d: ",test+shift);
		////////////////////////////////////////////////////////////
		scanf("%d%d",&n,&k);
		REP(i,n) scanf("%lf",a+i);
		sort(a,a+n);
		double r = 0;

		REP(pref,k+1)
		{
			vector<double> q;
			REP(i,pref) q.push_back(a[i]);
			REP(i,k-pref) q.push_back(a[n-1-i]);
			double t = solve(q);
			if (t>r) {
				r = t;
			}
		}
		if (false)
			REP(mask,1<<n)
			{
				vector<double> q;
				REP(i,n) if (mask&(1<<i)) q.pb(a[i]);
				if (SZ(q)!=k) continue;
				double t = solve(q);
				if (t>r) {
					if (t>r+1.0e-8)
						fprintf(stderr,"STRANGE %.12lf - %.12lf %.12lf\n",t-r,r,t);
					r = t;
				}
			}
		printf("%.12lf\n",r);
	}
	fprintf(stderr,"=== %s DONE\n", FN.c_str());
	return 0;
}