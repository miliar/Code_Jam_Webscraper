#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

#define N 5
#define M 4
#define LL __int64
#define INF 0x3f7f7f7f

int f[N][N], v[20];

void in()
{
    int i, j;
    for(i = 1; i <= M; i++)
    {
        for(j = 1; j <= M; j++)
            scanf("%d", &f[i][j]);
    }

}
int main(void)
{
    //freopen("A-small-attempt2.in", "r", stdin);
    //freopen("A-small-attempt2.out", "w", stdout);
    int TC, tc, n, i, tp, ans, r;
    scanf("%d", &TC);
    for(tc = 1; tc <= TC; tc++)
    {
        memset(v, 0, sizeof(v));
        scanf("%d", &r);
        in();
        for(i = 1; i <= M; i++) v[f[r][i]] = 1;
        scanf("%d",&r);
        in();
        ans = 0;
        for(i = 1; i <= M; i++)
        {
            if(!v[f[r][i]]) continue;
            ans ++; tp = f[r][i];
        }
        printf("Case #%d: ", tc);
        if(ans > 1)    printf("Bad magician!\n");
        else if(ans == 0)    printf("Volunteer cheated!\n");
        else printf("%d\n", tp);
    }
    return 0;
}
