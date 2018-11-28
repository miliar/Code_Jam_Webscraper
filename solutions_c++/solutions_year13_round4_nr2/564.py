#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;
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

void Perm(VI& team, int k)
{
    VI buf = team;
    int n = SIZE(team), i = 0;
    k >>= 1;
    while(i < n)
    {
        REP(x, k) team[x + i] = buf[2 * x + i];
        REP(x, k) team[k + x + i] = buf[2 * x + 1 + i];
        i += 2 * k;
    }
}
int main()
{
    int o;
    LL n, p, k, w, i, j;
    scanf("%d", &o);
    FOR(cs, 1, o)
    {
        scanf("%lld%lld", &n, &p);
        i = 1;
        REP(x, n) i *= 2;
        n = i;
//        cout << n << endl;
        if(p == n)
        {
            printf("Case #%d: %lld %lld\n", cs, n - 1, n - 1);
            continue;
        }
        if(p == 1)
        {
            printf("Case #%d: %d %d\n", cs, 0, 0);
            continue;
        }
        i = 2;
        k = j = n >> 1;
        while(2 * i <= p)
        {
//            cout << i << " " << k << endl;
            k += (j >>= 1);
            i <<= 1;
        }
//        cout << k << endl;
        w = n;
//        cout << n << " " << p << endl;
        p = n - p;
        i = 1;
        while(2 * i <= p)
        {
//            cout << i << " " << w << endl;
            i <<= 1;
            w >>= 1;
        }
//        cout << w - 1 << endl;
        printf("Case #%d: %lld %lld\n", cs, w - 2, k);
    }
}
