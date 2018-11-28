#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
#define LL long long
int p[6][6];
int o[6][6];
int in[6][6];
int r,c;
int a[8] = {0,0,1,1,1,-1,-1,-1};
int b[8] = {-1,1,0,1,-1,0,1,-1};
void judge(int x,int y)
{
    int i;
    for(i = 0; i < 8; i ++)
    {
        if(x+a[i] >= 0&&x+a[i] < r&&y+b[i] >= 0&&y+b[i] < c)
        {
            o[x][y] += p[x+a[i]][y+b[i]];
        }
    }
}
void dfs(int x,int y)
{
    int i;
    for(i = 0; i < 8; i ++)
    {
        if(x+a[i] >= 0&&x+a[i] < r&&y+b[i] >= 0&&y+b[i] < c)
        {
            if(o[x+a[i]][y+b[i]] == 0&&in[x+a[i]][y+b[i]] == 0)
            {
                in[x+a[i]][y+b[i]] = 1;
                dfs(x+a[i],y+b[i]);
            }
            else if(o[x+a[i]][y+b[i]] > 0)
            in[x+a[i]][y+b[i]] = 1;
        }
    }
}
int main()
{
    int t,cas = 1,i,m,j,k,u,sr,sc;
    freopen("C-small-attempt3.in","r",stdin);
    freopen("C-small-attempt3.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&r,&c,&m);
        printf("Case #%d:\n",cas++);
        if(m == 0)
        {
            for(i = 1; i <= r; i ++)
            {
                for(j = 1; j <= c; j ++)
                {
                    if(i == r&&j == c)
                        printf("C");
                    else
                        printf(".");
                }
                printf("\n");
            }
        }
        else if(m == r*c-1)
        {
            for(i = 1; i <= r; i ++)
            {
                for(j = 1; j <= c; j ++)
                {
                    if(i == r&&j == c)
                        printf("C");
                    else
                        printf("*");
                }
                printf("\n");
            }
        }
        else if(r == 1)
        {
            if(c-m <= 1)
                printf("Impossible\n");
            else
            {
                for(i = 1; i <= m; i ++)
                    printf("*");
                for(; i < c; i ++)
                    printf(".");
                printf("C\n");
            }
        }
        else if(c == 1)
        {
            if(r-m <= 1)
                printf("Impossible\n");
            else
            {
                for(i = 1; i <= m; i ++)
                    printf("*\n");
                for(; i < r; i ++)
                    printf(".\n");
                printf("C\n");
            }
        }
        else
        {
            int n = r*c;
            for(i = 1; i < (1<<n); i ++)
            {
                int num = 0;
                for(j = 0; j < n; j ++)
                {
                    if(i&(1<<j)) num ++;
                }
                if(num == m)
                {
                    memset(o,0,sizeof(o));
                    memset(in,0,sizeof(in));
                    j = 0;
                    for(k = 0; k < r; k ++)
                    {
                        for(u = 0; u < c; u ++)
                        {
                            if(i&(1<<j))
                                p[k][u] = 1;
                            else
                                p[k][u] = 0;
                            j ++;
                        }
                    }
                    for(k = 0; k < r; k ++)
                    {
                        for(u = 0; u < c; u ++)
                        {
                            if(p[k][u] == 1)
                                o[k][u] = -1;
                            else
                                judge(k,u);
                        }
                    }
                    int z = 1;
                    for(k = 0; k < r&&z; k ++)
                    {
                        for(u = 0; u < c&&z; u ++)
                        {
                            if(o[k][u] == 0)
                            {
                                z = 0;
                                sr = k;
                                sc = u;
                                in[k][u] = 1;
                                dfs(k,u);
                            }
                        }
                    }
                    if(z) continue;
                    int s = 0;
                    for(k = 0; k < r; k ++)
                    {
                        for(u = 0; u < c; u ++)
                        {
                            if(p[k][u] == 0)
                            {
                                if(!in[k][u]) s = 1;
                            }
                        }
                    }
                    if(s) continue;
                    else
                    {
                        s = 1;
                        for(k = 0; k < r; k ++)
                        {
                            for(u = 0; u < c; u ++)
                            {
                                if(k == sr&&u == sc)
                                    printf("C");
                                else if(p[k][u] == 0)
                                {
                                    printf(".");
                                }
                                else
                                {
                                    printf("*");
                                }
                            }
                            printf("\n");
                        }
                        break;
                    }
                }
            }
            if(i == (1<<n)) printf("Impossible\n");
        }
    }
    return 0;
}
