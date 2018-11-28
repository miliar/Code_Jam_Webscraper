#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 1000;
int T;
int vis[MAXN];

int num;
int main()
{
    scanf("%d",&T);
    for (int tt = 1; tt <= T; ++tt)
    {
        int r;
        scanf("%d",&r);
        for (int i = 1; i <= 4; ++i)
        {
            for (int j = 1; j <= 4; ++j)
            {
                scanf("%d",&num);
                if(i == r)
                    vis[num] ++;
            }
        }

        int ans = 0;
        int cnt = 0;
        scanf("%d",&r);
        for (int i = 1; i <= 4; ++i)
        {
            for (int j = 1; j <= 4; ++j)
            {
                scanf("%d",&num);
                if(i == r)
                {
                    vis[num] ++;
                    if(vis[num] == 2)
                    {
                        cnt ++;
                        ans = num;
                    }
                }
            }
        }


        printf("Case #%d: ",tt);
        if(cnt > 1)
        {
            printf("Bad magician!\n");
        }
        else if (cnt < 1)
        {
            printf("Volunteer cheated!\n");
        }
        else
            printf("%d\n",ans);
        memset(vis,0,sizeof(vis));
    }

    
    return 0;
}