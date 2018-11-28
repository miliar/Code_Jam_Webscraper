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
typedef vector<double> VD;
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
    int t, n, i, j;
    scanf("%d", &t);
    FOR(o, 1, t)
    {
        scanf("%d", &n);
        VD naomi(n), ken(n);
        REP(x, n) scanf("%lf", &naomi[x]);
        REP(x, n) scanf("%lf", &ken[x]);
        sort(ALL(naomi));
        sort(ALL(ken));
        i = j = 0;
        while(1)
        {
            while(i < n && naomi[i] < ken[j]) i++;
            if(i >= n) break;
            j++;
            i++;
        }
        printf("Case #%d: %d ", o, j);
        i = j = 0;
        while(1)
        {
            while(j < n && ken[j] < naomi[i]) j++;
            if(j >= n) break;
            j++;
            i++;
        }
        printf("%d\n", n - i);
    }
    return 0;
}
