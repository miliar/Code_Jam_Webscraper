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
4
2 2 2
2 1 3
4 4 1
3 2 3
*/

void work() {
    int T;
    scanf("%d", &T);
    fff(cas, 1, T) {
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);

        bool ans = false;
        while(true) {
            if(r * c % x) break;

            r = min(r, c);
            if(x == 3 && r <= 1) break;
            if(x == 4 && r <= 2) break;
            if(x == 5 && r <= 3) break;
            if(x == 6 && r <= 3) break;
            if(x >= 7) break;

            ans = true;
            break;
        }
        printf("Case #%d: %s\n", cas, ans ? "GABRIEL" : "RICHARD");
    }
}

