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
    int t;
    double c, f, w, i, r, b, temp;
    scanf("%d", &t);
    FOR(o, 1, t)
    {
        scanf("%lf%lf%lf", &c, &f, &w);
        i = 2.0;
        r = w / i;
        b = 0.0;
        while(1)
        {
            b += c / i;
            i += f;
            temp = w / i + b;
            if(temp > r) break;
            r = temp;
        }
        printf("Case #%d: %.7lf\n", o, r);
    }
    return 0;
}
