#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

int a[11][11], b[11][11];

int main()
{
    int testcase;
    int row1, row2, ans;
    freopen("magic.in", "r", stdin);
    freopen("magic.out", "w", stdout);
    scanf("%d", &testcase);
    for (int test = 1; test <= testcase; test++) {
        scanf("%d", &row1);
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
            scanf("%d", &a[i][j]);
        scanf("%d", &row2);
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
            scanf("%d", &b[i][j]);
        int p = 0;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
            if (a[row1][i] == b[row2][j]) {
                p++;
                ans = a[row1][i];
            }
        printf("Case #%d: ", test);
        if (p == 1) printf("%d\n", ans);
        if (p == 0) printf("Volunteer cheated!\n");
        if (p > 1) printf("Bad magician!\n");
    }
    return 0;
}
