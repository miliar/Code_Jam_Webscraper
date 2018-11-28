#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>


using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define epsilon 1e-6
#define ill long long
#define sz(a) int((a).size())
#define pb push_back
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define inf 100000000
#define si(x) scanf("%d", &(x));
#define pi(x) printf("%d\n", (x));
#define sill(x) scanf("%lld", &(x));
#define pill(x) printf("%lld\n", (x));


int main()
{
    double d, x, y, ans, sum, t1, t2, c, f;
    int t;
    freopen ("B-large.in", "r", stdin);
    freopen ("o.txt", "w", stdout);

    si(t);
    int cs = 1;

    while (cs <= t) {

        cin >> c >> f >> x;
       // cout << c << " " << f << " " << x << " " << endl;
        double tt = 0.0;
        double a = 0.0;
        double b = 2.0;

        double result = 10000000000.0;
        result = min (result, (x/b));
        for (int i = 1; i <= 100000; i++) {
            if (a >= c) {
                b = b + f;
                a = a-c;
                result = min (result, tt+(x/b));
                continue;
            }

            double rr = c-a;
            tt = tt + double(rr/b);
            a = 0.0;
            b = b + f;
            result = min (result, tt+(x/b));
        }
        printf ("Case #%d: %.7f\n", cs, result);        cs++;

    }

    return 0;
}



