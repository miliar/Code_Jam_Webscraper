#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <functional>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define ff(i, n) for(int i=0,END=(n);i<END;i++)
#define fff(i, n, m) for(int i=(n),END=(m);i<=END;i++)
#define mid ((l+r)/2)
#define bit(n) (1LL<<(n))
#define clr(a, b) memset(a, b, sizeof(a))

void work();

int main() {
    work();
    return 0;
}

/**************************Beautiful GEGE**********************************/

/* stdin
3
1
3
4
1 2 1 2
5
1000 1000 1000 1000 1000
*/

void work() {
    int T;
    scanf("%d", &T);
    fff(cas, 1, T) {
        int n;
        scanf("%d", &n);
        int d[2222], t;
        clr(d, 0);
        ff(i, n) scanf("%d", &t), d[t] ++;
        fff(i, 1, 2000) d[i] += d[i-1];

        int ans = 1000;
        fff(i, 1, 1000) {
            int count = 0;
            for(int j = 1; j * i <= 1000; j ++) {
                count += (d[(j + 1) * i] - d[j * i]) * j;
            }
            ans = min(ans, count + i);
        }

        printf("Case #%d: %d\n", cas, ans);
    }
}
