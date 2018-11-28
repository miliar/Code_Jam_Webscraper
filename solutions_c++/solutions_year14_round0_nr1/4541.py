#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <map>
#include <math.h>
#include <time.h>
#include <string>
using namespace std;
typedef long long LL;
const int INF = 0x3f3f3f3f;
const int N = 105;
const int M = 1605;
const int MOD = 1000000007;
LL n, m;

int a[N][N], b[N][N];
int vis[20];

int main () {
    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small-attempt1.out", "w", stdout);
    n = 4;
    int cases;
    scanf ("%d", &cases);

    for (int t = 1; t <= cases; t++) {
        int x, y;
        memset(vis, 0, sizeof(vis));
        scanf("%d", &x);
        for (int i = 1; i <= n; i ++){
            for (int j = 1; j <= n; j++) {
                scanf ("%d", &a[i][j]);
                if(i == x) {
                    vis[a[i][j]] ++;
                }
            }
        }
        scanf ("%d", &y);
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                scanf("%d", &b[i][j]);
                if(i == y) {
                    vis[b[i][j]] ++;
                }
            }
        }
        int flag = 0;
        int ans = 0;
        for (int i = 1; i <= 16; i++) {
            if(vis[i] >= 2) {
                flag++;
                ans = i;
            }
        }

        printf("Case #%d: ", t);
        if (flag == 0) {
            puts("Volunteer cheated!");
        }
        else {
            if (flag == 1) {
                printf("%d\n", ans);
            }
            else {
                puts("Bad magician!");
            }
        }
    }

    return 0;
}
