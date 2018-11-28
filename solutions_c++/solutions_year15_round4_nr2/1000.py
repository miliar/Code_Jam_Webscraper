//azariamuh

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <cassert>
using namespace std;

int inf = 1000000000;
typedef long long LL;

#define forn(a,b,c) for (int (a)=(b);(a)<=(c);++(a))
#define reset(a,b) memset(a,b,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()

int T,n;
double v,x;
double r[2],c[2];
double eps = 1e-9;

int main()
{
	scanf("%d",&T);
	forn(cases,1,T)
	{
		printf("Case #%d: ",cases);
		scanf("%d %lf %lf",&n,&v,&x);
		forn(i,0,n-1) scanf("%lf %lf",&r[i],&c[i]);
		if (n == 1) {
			if (fabs(x-c[0]) < eps) printf("%.9lf\n",v / r[0]);
			else puts("IMPOSSIBLE");
		} else if (n == 2) {
			if (fabs(c[0]-c[1]) < eps) {
				if (fabs(c[0]-x) < eps) printf("%.9lf\n",v / (r[0] + r[1]));
				else puts("IMPOSSIBLE");
			} else {
				double b = (x * v - c[0] * v) / (r[1] * c[1] - r[1] * c[0]);
				double a = (v - r[1] * b) / r[0];
				//printf("%.9lf %.9lf\n",a,b);
				//assert(fabs(b * r[1] + a * r[0] - v) < eps);
				//assert(fabs((b * r[1] * c[1] + a * r[0] * c[0]) / (b * r[1] + a * r[0]) - x) < eps);
				if (a < -eps || b < -eps) puts("IMPOSSIBLE");
				else printf("%.9lf\n",max(a,b));
			}
		}
	}
	return 0;
}













