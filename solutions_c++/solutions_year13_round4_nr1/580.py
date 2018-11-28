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
typedef pair<LL, LL> PLL;
typedef vector<LL> VLL;
typedef vector<PLL> VPLL;
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
const int MOD = 1000002013;

LL Mod(LL a)
{
    while(a < MOD) a += MOD;
    return a % MOD;
}
LL Pay(int a, int b, int c)
{
    LL n = a, k = b, l = c;
    return Mod(l * Mod((2 * n * k - k * k + k) / 2));
}
int main()
{
    int o, n, m, b, e, l;
    LL should, payed;
    scanf("%d", &o);
    FOR(cs, 1, o)
    {
        scanf("%d%d", &n, &m);
        should = payed = 0;
        map<int, PLL> stop;
        VPLL tickets;
        REP(x, m)
        {
            scanf("%d%d%d", &b, &e, &l);
            if(stop.find(b) == stop.end()) stop.insert(MP(b, MP(l, 0)));
            else stop[b] = MP(stop[b].ST + l, stop[b].ND);
            if(stop.find(e) == stop.end()) stop.insert(MP(e, MP(0, l)));
            else stop[e] = MP(stop[e].ST, stop[e].ND + l);
            should = Mod(should + Pay(n, e - b, l));
        }
        FOREACH(it, stop)
        {
            if(it->ND.ST > 0) tickets.PB(MP(it->ST, it->ND.ST));
            b = it->ND.ND;
            while(b > 0)
            {
                if(b >= tickets.back().ND)
                {
                    payed = Mod(payed + Pay(n, it->ST - tickets.back().ST, tickets.back().ND));
                    b -= tickets.back().ND;
                    tickets.pop_back();
                }
                else
                {
                    payed = Mod(payed + Pay(n, it->ST - tickets.back().ST, b));
                    tickets.back().ND -= b;
                    b = 0;
                }
            }
        }
        printf("Case #%d: %lld\n", cs, Mod(should - payed));
    }
    return 0;
}
