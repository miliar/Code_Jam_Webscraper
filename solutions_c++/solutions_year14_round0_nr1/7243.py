#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <queue>
#include <map>
#define mem(x,val) memset (x, val, sizeof (x))
#define MAXN 1000005
using namespace std;
typedef long long ll;
const double eps = 1e-8;
int f[20];

int main () {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int _, i, j, k, l, x, cnt, an, T = 0;
    scanf ("%d", &_);
    while (_ --) {
        mem(f, 0);
        for (l = 1; l <= 2; l ++) {
            scanf ("%d", &k);
            for (i = 1; i <= 4; i ++)
                for (j = 1; j <= 4; j ++) {
                    scanf ("%d", &x);
                    if (i == k)  f[x] ++;
                }
        }
        for (i = 1, cnt = 0; i <= 16; i ++)
            if (f[i] == 2)  an = i, cnt ++;
        printf("Case #%d: ", ++ T);
        if (cnt == 1)  printf("%d\n", an);
        else if (cnt == 0)  printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}

