#include <bits/stdc++.h>

#define ll long long

using namespace std;

const int INF = 1e9 + 7;
const int MXN = 1e5 + 7;

int t;
int row[2][20];

int main()
{
    //freopen("ss.in", "r", stdin);
    //freopen("ss.out", "w", stdout);
    scanf("%d", &t);
    for (int c = 0; c < t; c++) {
        int x, y;
        scanf("%d", &x);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int tmp;
                scanf("%d", &tmp);
                row[0][tmp] = i + 1;
            }
        }
        scanf("%d", &y);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int tmp;
                scanf("%d", &tmp);
                row[1][tmp] = i + 1;
            }
        }
        int cnt = 0, ans;
        for (int i = 1; i <= 16; i++) {
            if (row[0][i] == x && row[1][i] == y) {
                cnt++;
                ans = i;
            }
        }
        printf("Case #%d: ", c + 1);
        if (cnt > 1) puts("Bad magician!");
        else if (cnt == 0) puts("Volunteer cheated!");
        else printf("%d\n", ans);
    }
    return 0;
}
