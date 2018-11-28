#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
using namespace std;
bool ans, b[102][102];
int a[102][102];

int main()
{
  //  freopen("B.in", "r", stdin);
  //  freopen("B.out", "w", stdout);
    int ts, ks, i, j, n, m, most;
    scanf("%d", &ts);
    for (ks = 0; ks < ts; ks++){
        scanf("%d %d", &n, &m);
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)
                scanf("%d", &a[i][j]);
        memset(b, false, sizeof(b));
        for (i = 0; i < n; i++){
            most = 0;
            for (j = 0; j < m; j++)
                if (a[i][j] > most) most = a[i][j];
            for (j = 0; j < m; j++)
                if (a[i][j] >= most) b[i][j] = true;
        }
        for (i = 0; i < m; i++){
            most = 0;
            for (j = 0; j < n; j++)
                if (a[j][i] > most) most = a[j][i];
            for (j = 0; j < n; j++)
                if (a[j][i] >= most) b[j][i] = true;
        }
        ans = true;
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)
                if (b[i][j] == false) ans = false;
        if (ans)
           printf("Case #%d: YES\n", ks + 1);
        else printf("Case #%d: NO\n", ks + 1);
    }
    return 0;
}
