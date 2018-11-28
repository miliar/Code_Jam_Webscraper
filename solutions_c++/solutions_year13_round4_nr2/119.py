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

int n;
ll p;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d", &T);
    forn(t, T) {
        printf("Case #%d: ", t + 1);

        cin >> n >> p;

        if (p == (1ll << n)) {
            printf("%lld %lld\n", (1ll << n) - 1ll, (1ll << n) - 1ll);
            continue;
        }
        if (p == 1ll) {
            printf("0 0\n");
            continue;
        }
        p--;

        int k = 0;
        forba(i, n, 0)
            if ((p & (1ll << i)) != 0ll)
                k++;
            else {
                k++;
                break;
            }
        printf("%lld ", (1ll << k) - 2ll);

        k = 0;
        forba(i, n, 0)
            if ((p & (1ll << i)) == 0ll)
                k++;
            else {
                forn(j, i)
                    if ((p & (1ll << j)) == 0ll) {
                        k++;
                        break;
                    }
                break;
            }
        printf("%lld\n", (1ll << n) - (1ll << k));

    }
    return 0;
}
