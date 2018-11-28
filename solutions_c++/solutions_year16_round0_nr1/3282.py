#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <string>
#include <time.h>
#define clr(x,c) memset(x, c, sizeof(x))
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define psi pair<string, int>
#define LLD_MAX 9223372036854775807LL
#define LLD_MIN (-LLD_MAX - 1LL)
#define inf 0x3f3f3f3f
typedef long long lld;
typedef unsigned long long ulld;
using namespace std;
bool vis[10];
unordered_set<lld> nums;

bool visit(lld num)
{
    do {
        vis[num%10] = true;
        num /= 10;
    } while (num) ;

    for (int i = 0; i < 10; ++i) {
        if (!vis[i]) return 0;
    }

    return 1;
}

int main ()
{
//    freopen("C:/Users/ywy/Desktop/A-large.in", "r", stdin);
//    freopen("C:/Users/ywy/Desktop/out.txt", "w", stdout);
    int t, cas = 1, n;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        clr(vis, false);
        nums.clear();

        int m = 1;
        lld ans = 0;

        while (1) {
            lld num = 1L * n * m;
            if (visit(num)) {
                ans = num;
                break;
            }
            if (nums.find(num) != nums.end()) {
                break;
            } else {
                nums.insert(num);
            }
            m += 1;
        }

        if (ans > 0) {
            printf("Case #%d: %lld\n", cas++, ans);
        } else {
            printf("Case #%d: INSOMNIA\n", cas++);
        }
    }
    return 0;
}
