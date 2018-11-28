#include<bits/stdc++.h>
using namespace std;
#define sq(x) x * x
#define all(a) a.begin(), a.end()
#define lowpos(a, x) (lower_bound(all(a), x) - a.begin())
#define For(i, n) for (i = 0; i < n; ++i)
#define Forr(i, start, n) for (i = start; i < n; ++i)
#define Forrr(i, start, n, step) for (i = start; i < n; i += step)
#define rFor(i, n) for (i = n; i >= 0; --i)
#define rForr(i, end, n) for (i = n; i >= end; --i)
#define rForrr(i, end, n, step) for (i = n; i >= end; i -= step)
#define loop(a) for (it = a.begin(); it != a.end(); ++it)
typedef long long ll;
#define mem(a, num) memset(a, num, sizeof(a))
#define cpy(a, b) memcpy(a, b, sizeof(a))
typedef unsigned long long ull;
#define SI(n) scanf("%d", &n)
#define SII(a, b) scanf("%d%d", &a, &b)
#define SIII(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define SD(n) scanf("%lf", &n)
#define SDD(a, b) scanf("%lf%lf", &a, &b)
#define SDDD(a, b, c) scanf("%lf%lf%lf", &a, &b, &c)
#define SA(a, i, n) For(i, n) SI(a[i])
#define SAA(a, i, n, j, m) For(i, n) For(j, m) SI(a[i][j])
#define PI(n) printf("%d\n", n)
#define PII(a, b) printf("%d %d\n", a, b)
#define PIII(a, b, c) printf("%d %d %d\n", a, b, c)
#define PD(n) printf("%f\n", n)
#define PDD(a, b) printf("%f %f\n", a, b)
#define PDDD(a, b, c) printf("%f %f %f\n", a, b, c)
#define PA(a, i, n) For(i, n - 1) printf("%d ", a[i]); PI(a[n - 1])
#define PAA(a, i, n) For(i, n) PII(i, a[i])
#define PB push_back
#define MP make_pair
typedef vector<int>::iterator viter;
#define Diff(v, a, n, b, m) v.resize(set_difference(a, a + n, b, b + m, v.begin()) - v.begin());
#define SDiff(v, a, n, b, m) v.resize(n + m); sort(a, a + n); sort(b, b + m); Diff(v, a, n, b, m)
#define Inter(v, a, n, b, m) v.resize(set_intersection(a, a + n, b, b + m, v.begin()) - v.begin());
#define SInter(v, a, n, b, m) v.resize(n + m); sort(a, a + n); sort(b, b + m); Inter(v, a, n, b, m)
#define Sym(v, a, n, b, m) v.resize(set_symmetric_difference(a, a + n, b, b + m, v.begin()) - v.begin());
#define SSym(v, a, n, b, m) v.resize(n + m); sort(a, a + n); sort(b, b + m); Sym(v, a, n, b, m)
#define Union(v, a, n, b, m) v.resize(set_union(a, a + n, b, b + m, v.begin()) - v.begin());
#define SUnion(v, a, n, b, m) v.resize(n + m); sort(a, a + n); sort(b, b + m); Union(v, a, n, b, m)
typedef pair<int, int> p2;
typedef pair<int, pair<int, int> > p3;
#define Fin(f) freopen(f, "r", stdin)
#define Fout(f) freopen(f, "w", stdout)
const int inf = 0x3f3f3f3f;
const double pi = acos(-1.0);
const double eps = 1e-8;

///请先检查头文件是否符合编译器

/**/


int main()
{
	Fin("B-large.in");
	Fout("B-large.out");
	int T,cas,i;
	double c,f,x,ans,t;
	SI(T);
	Forr(cas, 1, T + 1)
	{
		printf("Case #%d: ", cas);
		SDDD(c,f,x);
		ans=x/2.0;
		if(c<x)
        {
            t=c/2.0,i=1;
            while(t<ans)
            {
                ans=min(ans,t+x/(2.0+f*i));
                t+=c/(2.0+f*i);
                ++i;
            }
        }
        printf("%.7f\n",ans);
	}
	return 0;
}
