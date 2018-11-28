#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define maxn 102
int mp[maxn][maxn];
int tmp[maxn][maxn];
int queue[maxn*maxn];
int flag[maxn][maxn];
bool judge(int n,int m)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            if(flag[i][j] == 0)
                return false;
        }
    }
    return true;
}
int main()
{
    int T;
    int n,m;

     freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    while(scanf("%d",&T)!=EOF)
    {
        int csT = 1;
        while(T--)
        {
            scanf("%d%d",&n,&m);
            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < m; j++)
                {
                    tmp[i][j] = 100;
                }
            }
            int tt = 0;
            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < m ; j++){
                    scanf("%d",&mp[i][j]);
                    queue[tt++] = mp[i][j];
                }
            }
            sort(queue,queue+tt);
            int tk = 0;
            for(int i = 1; i < tt; i++)
            {
                if(queue[tk] != queue[i])
                    queue[++tk] = queue[i];
            }
            memset(flag,0,sizeof(flag));
            tt = tk;
            for(int t = tt; t >= 0; t--)
            {
                for(int i = 0;  i < n; i++)
                {
                    int ff = 0;
                    for(int j = 0; j < m; j++)
                    {
                        if(flag[i][j] != 0){
                            ff = 1;
                            break;
                        }
                    }
                    if(ff == 0)
                    {
                        for(int j = 0; j < m; j++)
                        {
                            tmp[i][j] = queue[t];
                        }
                    }
                }
                for(int i = 0; i < m; i++)
                {
                    int ff = 0;
                    for(int j = 0; j < n; j++)
                    {
                        if(flag[j][i] != 0)
                        {
                            ff = 1;
                            break;
                        }
                    }
                    if(ff == 0)
                    {
                        for(int j = 0; j < n; j++)
                            tmp[j][i] = queue[t];
                    }
                }
                for(int i = 0; i < n; i++)
                {
                    for(int j = 0; j < m; j++)
                    {
                        if(tmp[i][j] == mp[i][j])
                            flag[i][j] = 1;
                    }
                }

            }
            if(judge(n,m))
                printf("Case #%d: YES\n",csT++);
            else
                printf("Case #%d: NO\n",csT++);
        }
    }
    return 0;
}
