#include <iostream>
#include <cstdio>
#include <string>
#include <sstream> 
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <iomanip>
using namespace std;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define vi vector<int>
#define SZ(x) ((int)(x.size()))
#define fi first
#define se second
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define IN(x,y) ((y).find((x))!=(y).end())
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define DBG cerr << "debug here" << endl;
#define DBGV(vari) cerr << #vari<< " = "<< (vari) <<endl;

typedef long long ll;
typedef double fl;

ll boundary(double c, double f, double x)
{
    return ceil((x * f - 2.0 * c) / (f * c)) - 1LL;
}
double solve(double c, double f, double x, ll k)
{
    double s = 0.0;
    for(int i = 1; i <= k; ++i)
    {
        s += 1.0 / (2.0 + f * (i - 1));
    }
    return c * s + x / (2.0 + f * k);
}
int main()
{
    int tests;
    scanf("%d", &tests);
    for(int t = 1; t <= tests; ++t)
    {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double res = solve(c, f, x, max(0LL, boundary(c, f, x)));
        printf("Case #%d: %.10f\n", t, res);
    } 
    return 0;
}
