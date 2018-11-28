#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

#define INSTR "B-large.in"

int T, n, m, s[200][200], x[200], y[200];
bool h;

int main(){
    freopen(INSTR, "r", stdin);
    freopen("b.txt", "w", stdout);

    cin >> T;
    for (int cas = 1; cas <= T; cas ++){
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i ++)
            for (int j = 1; j <= m; j ++)
                scanf("%d", &s[i][j]);
        memset(x, 0, sizeof(x));
        memset(y, 0, sizeof(y));
        for (int i = 1; i <= n; i ++)
            for (int j = 1; j <= m; j ++){
                if (s[i][j] > x[i]) x[i] = s[i][j];
                if (s[i][j] > y[j]) y[j] = s[i][j];
                }
        h = true;
        for (int i = 1; i <= n; i ++)
            for (int j = 1; j <= m; j ++)
                if (s[i][j] < x[i] && s[i][j] < y[j]) h = false;
        if (h == true) printf("Case #%d: YES\n", cas);
                  else printf("Case #%d: NO\n", cas);
        }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
