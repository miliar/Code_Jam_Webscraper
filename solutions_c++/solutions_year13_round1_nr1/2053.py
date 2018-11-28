#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PI;
typedef long long LL;
typedef vector<LL> VLL;
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
const int INF = 1000000001;
const double EPS = 10e-9;
const double MAX = 1500000000;

LL nieparzyste(LL n)
{
    return 2 * n * n + n;
}
LL parzyste(LL n)
{
    return 2 * n * n + 3 * n;
}
LL nieparzyste(LL i, LL r)
{
    LL n = (r + 1) >> 1;
    return nieparzyste(n + i - 1) - nieparzyste(n - 1);
}
LL parzyste(LL i, LL r)
{
    LL n = r >> 1;
    return parzyste(n + i - 1) - parzyste(n - 1);
}
int main()
{
    int test, p, k, s;
    LL r, t;
    scanf("%d", &test);
    FOR(cs, 1, test)
    {
        scanf("%lld%lld", &r, &t);
        p = 0;
        k = MAX;
        if((r & 1) == 1)
        {
            while(p != k)
            {
                s = (p + k + 1) >> 1;
                if(nieparzyste(s, r) > t) k = s - 1;
                else p = s;
                //cout << s << " " << nieparzyste(s, r) << endl;
                //cout << p << ' ' << k << endl;
            }
        }
        else
        {
            while(p != k)
            {
                s = (p + k + 1) >> 1;
                if(parzyste(s, r) > t) k = s - 1;
                else p = s;
                //cout << s << " " << parzyste(s, r) << endl;
                //cout << p << ' ' << k << endl;
            }
        }
        //cout << p << ' ' << k << endl;
        printf("Case #%d: %d\n", cs, p);
    }
    return 0;
}
