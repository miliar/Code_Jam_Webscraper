#include <bits/stdc++.h> 

using namespace std;
 
#define sz(c) (int)(c).size()
 
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
 
#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef unsigned int uint;

#ifdef WIN32
#define I64 "%I64d"
#else
#define I64 "%lld"
#endif

#define FNAME "1"

const int MAXN = 305;
const double INF = 1e18;

int N;
double V, X;
pair <double, double> a[MAXN];

bool cmp1(pair <double, double> k, pair <double, double> l)
{
    return k.second < l.second;
}

bool cmp2(pair <double, double> k, pair <double, double> l)
{
    return k.second > l.second;
}

bool check(double M, double EPS)
{
    sort(a, a + N, cmp1);
    double curV = 0, curL = INF;
    for (int i = 0; i < N; i++)
    {
        double newV = min(curV + a[i].first * M, V), newL = 0;
        if (curL < a[i].second)
        {
            newL = (curL * curV + (newV - curV) * a[i].second) / newV;    
        }
        else
        {
            double myV = min(a[i].first * M, V);
            newL = (myV * a[i].second + (newV - myV) * curL) / newV;
        }
        curV = newV;
        curL = newL;
    }

    sort(a, a + N, cmp2);
    curV = 0;
    double curR = -INF;
    for (int i = 0; i < N; i++)
    {
        double newV = min(curV + a[i].first * M, V), newR = 0;
        if (curR > a[i].second)
        {
            newR = (curR * curV + (newV - curV) * a[i].second) / newV;    
        }
        else
        {
            double myV = min(a[i].first * M, V);
            newR = (myV * a[i].second + (newV - myV) * curR) / newV;
        }
        curV = newV;
        curR = newR;
    }



    //printf("%.20f %.20f %.20f %.20f %.20f %.20f\n", M, curV, curL, curR, V, X);
    //printf("%d %d %d\n", abs(curV - V) < EPS, curL <= X + EPS, curR + EPS >= X);
    if (abs(curV - V) <= EPS && curL <= X + EPS && curR + EPS >= X)
        return 1;
    return 0;
}

int main() 
{
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout); 
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++)
    {
        scanf("%d%lf%lf", &N, &V, &X);
        for (int i = 0; i < N; i++)
            scanf("%lf%lf", &a[i].first, &a[i].second);
        double L = 0, R = INF;
        for (int q = 0; q < 300; q++)
        {
            double M = (L + R) / 2;
            if (check(M, 1e-12))
                R = M;
            else
                L = M;
        }
        printf("Case #%d: ", t + 1);
        if (check(L, 1e-8))
            printf("%.20f\n", L);
        else
            puts("IMPOSSIBLE");
    } 
    return 0;
}