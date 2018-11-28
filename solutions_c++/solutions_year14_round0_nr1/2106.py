/*
ID: wuqi9395@126.com
PROG:
LANG: C++
*/
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<ctype.h>
#include<iostream>
#include<algorithm>
#define maxn 1000
#define INF (1<<30)
#define PI acos(-1.0)
#define mem(a, b) memset(a, b, sizeof(a))
#define For(i, n) for (int i = 0; i < n; i++)
typedef long long ll;
using namespace std;
int a[20], b[20];
int main ()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t;
    int n, m, cnt = 1, x;
    int ans[6], tot = 0;
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        mem(a, 0);
        mem(b, 0);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &x);
                if (i == n) a[x] = 1;
            }
        }
        scanf("%d", &m);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &x);
                if (i == m) b[x] = 1;
            }
        }
        tot = 0;
        for (int i = 1; i <= 16; i++) if (a[i] && b[i]) {
            ans[tot++] = i;
        }
        if (tot == 1) {
            printf("Case #%d: %d\n", cnt++, ans[0]);
        }
        else if (tot > 1) {
            printf("Case #%d: Bad magician!\n", cnt++);
        }
        else {
            printf("Case #%d: Volunteer cheated!\n", cnt++);
        }
    }
    return 0;
}
