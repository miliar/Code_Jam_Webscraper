#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#define inf 1000000007
#define eps 1e-8
#define M 105
#define N 2505
#define For(i,a,b) for(int i=(a);i<(b);i++)
using namespace std;

struct Node {
    int c, x, y;
} q[M*M];

int cmp(Node a, Node b) {
    return a.c < b.c;
}

int n, m;
bool useda[M];
bool usedb[M];
int num;
int cap[M][M];

bool judge() {
    memset(useda, false, sizeof (useda));
    memset(usedb, false, sizeof (usedb));
    int c;
    int x, y;

    For(i, 0, num) {
        if (useda[q[i].x] || usedb[q[i].y])
            continue;
        c = q[i].c;
        x = q[i].x;
        y = q[i].y;
        bool ok = false;

        For(i, 0, m) {
            if (cap[x][i] > c)
                ok = 1;
        }
        if (!ok) {
            useda[x] = 1;
            continue;
        }
        ok = false;

        For(i, 0, n)
        if (cap[i][y] > c)
            ok = 1;
        if (!ok) {
            useda[y] = 1;
            continue;
        }
        return false;
    }
    return 1;
}

int main() {
    int T;
    scanf("%d", &T);
    freopen("123.txt", "w", stdout);
    int cs = 0;
    while (T--) {
        cs++;
        scanf("%d%d", &n, &m);
        num = 0;

        For(i, 0, n)
        For(j, 0, m) {
            int c;
            scanf("%d", &c);
            cap[i][j] = c;
            q[num].c = c, q[num].x = i, q[num].y = j, num++;
        }
        sort(q, q + num, cmp);
        if (judge()) {
            printf("Case #%d: YES\n", cs);
        } else {
            printf("Case #%d: NO\n", cs);
        }


    }

    return 0;
}