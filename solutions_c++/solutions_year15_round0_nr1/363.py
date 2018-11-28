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
1
5 110011
*/

void work() {
    int T;
    scanf("%d", &T);
    fff(cas, 1, T) {
        int n;
        scanf("%d", &n);
        char str[1111];
        scanf("%s", str);

        int sum = 0;
        int ans = 0;
        fff(i, 0, n) if(sum < i)
        {
            ans ++;
            sum ++;
            sum += str[i] - '0';
        } else {
            sum += str[i] - '0';
        }
        printf("Case #%d: %d\n", cas, ans);
    }
}
