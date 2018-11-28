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

const int MAXN = 3333;
int vis[MAXN];

int main ()
{
//    freopen("C:/Users/ywy/Desktop/large.in", "r", stdin);
//    freopen("C:/Users/ywy/Desktop/in.txt", "r", stdin);
//    freopen("C:/Users/ywy/Desktop/large-out.txt", "w", stdout);
//    freopen("C:/Users/ywy/Desktop/out.txt", "w", stdout);
    int t, cas = 1, n;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        int m = 2 * n - 1;
        clr(vis, 0);
        for (int i = 0, tmp; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                scanf("%d", &tmp);
                vis[tmp] += 1;
            }
        }
        printf("Case #%d:", cas++);
        for (int i = 1; i < MAXN; ++i) {
            if (vis[i] & 1) {
                printf(" %d", i);
            }
        }
        printf("\n");
    }
    return 0;
}


