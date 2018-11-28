#include <stdio.h>
#include <cstring>
int a, b;
int ma[4][4], mb[4][4];
void in(int m[4][4])
{
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            scanf("%d", &m[i][j]);
        }
    }
}
int main()
{
//    freopen("C:\\Users\\lijian\\Desktop\\A-small-attempt3.in", "r", stdin);
//    freopen("C:\\Users\\lijian\\Desktop\\A-small-attempt3.out", "w", stdout);
    int t, kase=0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &a);
        in(ma);
        scanf("%d", &b);
        in(mb);
        a--, b--;
        int same = 0, ans;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(ma[a][i]==mb[b][j])
                {
                    same++;
                    ans = ma[a][i];
                }
            }
        }
        if(same==1) printf("Case #%d: %d\n", ++kase, ans);
        else    printf("Case #%d: %s\n", ++kase, same>1 ? "Bad magician!" : "Volunteer cheated!");
    }
    return 0;
}
