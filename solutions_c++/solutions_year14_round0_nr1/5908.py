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
#define SA(a, i, n) For(i, n) SI(a[i])
#define SAA(a, i, n, j, m) For(i, n) For(j, m) SI(a[i][j])
#define PI(n) printf("%d\n", n)
#define PII(a, b) printf("%d %d\n", a, b)
#define PIII(a, b, c) printf("%d %d %d\n", a, b, c)
#define PA(a, i, n) For(i, n - 1) printf("%d ", a[i]); PI(a[n - 1])
#define PAA(a, i, n) For(i, n) PII(i, a[i])
#define PB push_back
#define MP make_pair
typedef pair<int, int> p2;
typedef pair<int, pair<int, int> > p3;
typedef vector<int>::iterator viter;
#define Fin(f) freopen(f, "r", stdin)
#define Fout(f) freopen(f, "w", stdout)
const int inf = 0x3f3f3f3f;
const double pi = acos(-1.0);
const double eps = 1e-8;

///请先检查头文件是否符合编译器

/**/



int a[5][5],b[5][5];

int main()
{
    Fin("A-small-attempt0.in");
    Fout("A-small-attempt0.out");
    int t,cas,x,y,i,j;
	SI(t);
	Forr(cas,1,t+1)
	{
	    printf("Case #%d: ",cas);
	    SI(x),--x;
	    SAA(a,i,4,j,4);
	    SI(y),--y;
	    SAA(b,i,4,j,4);
	    sort(a[x],a[x]+4);
	    sort(b[y],b[y]+4);
	    vector<int> v(10);
        v.resize(set_intersection (a[x], a[x]+4, b[y],b[y]+4, v.begin())-v.begin());
        if(v.size()==0) puts("Volunteer cheated!");
        else if(v.size()==1) PI(v[0]);
        else puts("Bad magician!");
	}
	return 0;
}
