#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <list>
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

int main()
{
    int t, a, b;
    VI numbf(16), numbs(16);
    VVI first(4, VI(4)), second(4, VI(4));
    scanf("%d", &t);
    FOR(o, 1, t)
    {
        scanf("%d", &a);
        REP(y, 4) REP(x, 4) scanf("%d", &first[y][x]);
        scanf("%d", &b);
        REP(y, 4) REP(x, 4) scanf("%d", &second[y][x]);

        REP(x, SIZE(numbf)) numbf[x] = 0;
        REP(x, 4) numbf[first[a - 1][x] - 1] = 1;
        REP(x, SIZE(numbs)) numbs[x] = 0;
        REP(x, 4) numbs[second[b - 1][x] - 1] = 1;
        REP(x, 16) numbf[x] &= numbs[x];
        b = 0;
        REP(x, SIZE(numbf)) if(numbf[x])
        {
            a = x + 1;
            b++;
        }
        if(b == 0) printf("Case #%d: Volunteer cheated!\n", o);
        else if(b == 1) printf("Case #%d: %d\n", o, a);
        else printf("Case #%d: Bad magician!\n", o);
    }
    return 0;
}
