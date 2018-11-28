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
5
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i
*/

int table[5][5] = {
    {},
    {0, 1, 2, 3, 4},
    {0, 2, -1, 4, -3},
    {0, 3, -4, -1, 2},
    {0, 4, 3, -2, -1}
};

char str[11111];
void work() {
    int T;
    scanf("%d", &T);
    fff(cas, 1, T) {
        bool ok = false;
        while(1) {
            int l;
            LL x;
            cin >> l >> x;
            scanf("%s", str + 1);

            int now = 1;
            fff(i, 1, l)
                now = table[abs(now)][str[i] - 'i' + 2] * (now > 0 ? 1 : -1);

            if(now == 1) {
                break;
            } else if(now == -1) {
                if(x % 2 == 0) break;
            } else if(x % 4 != 2) {
                break;
            }

            int left = 0;
            now = 1;
            ff(t, 4) {
                fff(i, 1, l) {
                    now = table[abs(now)][str[i] - 'i' + 2] * (now > 0 ? 1 : -1);
                    if(now == 2) {
                        left = t * l + i;
                        t = 4;
                        break;
                    }
                }
            }
            if(left == 0) break;
            
            int right = 0;
            now = 1;
            reverse(str + 1, str + l + 1);
            ff(t, 4) {
                fff(i, 1, l) {
                    now = table[str[i] - 'i' + 2][abs(now)] * (now > 0 ? 1 : -1);
                    if(now == 4) {
                        right = t * l + i;
                        t = 4;
                        break;
                    }
                }
            }
            if(right == 0) break;

            if(x * l < left + right) break;
            
            ok = true;
            break;
        }
        printf("Case #%d: %s\n", cas, ok ? "YES" : "NO");
    }
}
