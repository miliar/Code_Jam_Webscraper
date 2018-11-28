#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const ldb EPS = 1e-9;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(test, T) {
        printf("Case #%d: ", test + 1);

        ldb c, f, x;
        cin >> c >> f >> x;

        ldb v = 2.0L;
        ldb t = 0.0L;
        ldb fin = x / v;

        while (fin > t - EPS) {
            t += c / v;
            v += f;
            fin = min(fin, t + x / v);
        }

        printf("%.10lf\n", (double)fin);
    }
    return 0;
}
