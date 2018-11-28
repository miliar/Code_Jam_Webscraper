#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    freopen("b1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int n,m;
    int map[105][105];
    scanf("%d",&T);
    for(int k = 0;k < T; ++k)
    {
        scanf("%d%d",&n,&m);
        for(int i = 0;i < n; ++i)
        {
            for(int j = 0;j < m; ++j)
            {
              scanf("%d",&map[i][j]);
            }
        }
        int ans = 0;
        for(int i = 0;i < n; ++i)
        {
            for(int j = 0;j < m; ++j)
            {
                ans = 0;
                for(int o = 0;o < m; ++o)
                {
                    if(map[i][o] > map[i][j])
                    {
                        //printf("aaaa\n");
                        ans++;break;
                    }
                }
                for(int o = 0;o < n; ++o)
                {
                    if(map[o][j] > map[i][j])
                    {
                        //printf("bbbb\n");
                        ans ++;break;
                    }
                }
                if(ans >= 2)
                    break;
            }
            if(ans >= 2)
                break;
        }
        printf("Case #%d: ",k+1);
        if(ans >= 2)
        printf("NO\n");
        else
        printf("YES\n");
    }
    return 0;
}
