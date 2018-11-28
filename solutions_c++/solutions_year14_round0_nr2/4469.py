#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define FOR(i, a, b) for (int i = int(a); i < int(b); i++)
#define REP(i, a) for (int i = 0; i < int(a); i++)
#define INF 1000000000
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef vector<bool> vb;

int n_casos, caso;

void solve()
{
    double t, c, f, x, no_f_t, acumulada=0.0;
    double tmp_t;

    cin >> c >> f >> x;

    no_f_t    =  x/(2.0);
    t = no_f_t;

    for(int i=0; true; i++)
    {
        acumulada += c/(2.0+i*f);
        no_f_t    =  x/(2.0+(i+1)*f);
        tmp_t = acumulada + no_f_t;
        if(tmp_t < t)
            t = tmp_t;
        else
            break;
    }

    printf("Case #%d: %.7lf\n", caso, t);

}

int main()
{
    freopen("CookieClickerAlpha.out", "w", stdout);
    freopen("CookieClickerAlpha.in", "r", stdin);
    cin >> n_casos;

    for(caso = 1; caso <= n_casos; caso++)
        solve();
    return 0;
}
