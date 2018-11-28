#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
int p[5][5];
int o[20];
int main()
{
    int t,cas = 1,i,j,r;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        memset(o,0,sizeof(o));
        scanf("%d",&r);
        for(i = 1;i <= 4;i ++)
        {
            for(j = 1;j <= 4;j ++)
            {
                scanf("%d",&p[i][j]);
                if(r == i)
                o[p[i][j]] ++;
            }
        }
        scanf("%d",&r);
        for(i = 1;i <= 4;i ++)
        {
            for(j = 1;j <= 4;j ++)
            {
                scanf("%d",&p[i][j]);
                if(r == i)
                o[p[i][j]] ++;
            }
        }
        int flag = 0,ans;
        for(i = 1;i <= 16;i ++)
        {
            if(o[i] == 2)
            {
                ans = i;
                flag ++;
            }
        }
        printf("Case #%d: ",cas++);
        if(flag == 0)
        printf("Volunteer cheated!\n");
        else if(flag == 1)
        printf("%d\n",ans);
        else
        printf("Bad magician!\n");
    }
    return 0;
}
