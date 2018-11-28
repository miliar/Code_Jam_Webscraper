#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 102;
int mp[MAX][MAX];
int num[MAX * MAX], ncnt;
int n, m;

bool check(int x)
{
    int k;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (mp[i][j] <= x) {
                for (k = 0; k < n; ++k)
                    if (mp[k][j] > x)
                        break;
                if (k == n)
                    continue;
                for (k = 0; k < m; ++k)
                    if (mp[i][k] > x)
                        break;
                if (k == m)
                    continue;
                return false;
            }
    return true;
}

bool work()
{
    for (int i = 0; i < ncnt; ++i) {
        if (check(num[i]) == false)
            return false;
    }
    return true;
}

int main()
{
    freopen("blarge.in", "r", stdin);
   freopen("blarge.out", "w", stdout);

    int flag[MAX * MAX];
    int cas;
    scanf("%d", &cas);
    for (int icase = 1; icase <= cas; ++icase) {
        scanf("%d%d", &n, &m);
        ncnt = 0;
        memset(flag, 0, sizeof(flag));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                scanf("%d", &mp[i][j]);
                if (flag[mp[i][j]] == 0) {
                    num[ncnt++] = mp[i][j];
                    flag[mp[i][j]] = 1;
                }
            }
        sort(num, num + ncnt);

        printf("Case #%d: ", icase);
        if (work())
            puts("YES");
        else
            puts("NO");
    }

}
