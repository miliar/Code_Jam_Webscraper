#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int T,a[5][5],num[20];

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for (int kase = 1;kase <= T; kase++) {
        memset(num,0,sizeof(num));
        int u; scanf("%d",&u);
        for (int i = 1;i <= 4; i++)
            for (int j = 1;j <= 4; j++) {
                scanf("%d",&a[i][j]);
                if (i == u) num[a[i][j]]++;
            }
        scanf("%d",&u);
        for (int i = 1;i <= 4; i++)
            for (int j = 1;j <= 4; j++) {
                scanf("%d",&a[i][j]);
                if (i == u) num[a[i][j]]++;
                }
        int ans = 0,cnt = 0;
        for (int i = 1;i <= 16; i++)
        if (num[i] >= 2) { ans = i; cnt++; }
        printf("Case #%d: ",kase);
        if (cnt == 0) printf("Volunteer cheated!\n");
        else if (cnt > 1) printf("Bad magician!\n");
        else printf("%d\n",ans);
    }
    return 0;
}
