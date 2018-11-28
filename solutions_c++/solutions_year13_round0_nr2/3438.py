#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
int mat[100][100], cut[100][100];
bool col(int c, int n,int h)
{
    for(int i = 0 ; i < n ; i ++)
    {
        if(mat[i][c] > h)
            return false;
    }
    return true;
}
bool row(int r, int n,int h)
{
    for(int i = 0 ; i < n ; i ++)
    {
        if(mat[r][i] > h)
            return false;
    }
    return true;
}
bool check(int n,int m)
{
    for(int i = 0 ;i < n ; i ++)
    {
        for(int j = 0 ; j < m ; j ++)
        {
            if(mat[i][j] != cut[i][j])
                return false;
        }
    }
    return true;
}
int main()
{
    freopen("C:/Users/v-y/Downloads/B-large.in","r",stdin);
    freopen("C:/Users/v-y/Downloads/B-large.out","w",stdout);
    int t, cas = 1;
    scanf("%d",&t);
    while(t--)
    {
        int n, m;
        scanf("%d %d",&n,&m);
        for(int i = 0 ; i < n ; i++)
        {
            for(int j = 0 ; j < m ; j ++)
            {
                scanf("%d",&mat[i][j]);
                cut[i][j] = 100;
            }
        }
        for(int h = 100 ; h >= 1 ; h --)
        {
            for(int i = 0 ; i < m ; i++)
            {
                if(col(i,n,h))
                {
                    for(int j = 0 ; j < n ; j ++)
                    {
                        cut[j][i] = h;
                    }
                }
            }
            for(int i = 0 ; i < n ; i++)
            {
                if(row(i,m,h))
                {
                    for(int j = 0 ; j < m ; j ++)
                    {
                        cut[i][j] = h;
                    }
                }
            }
        }

        if(check(n,m))
        {
            printf("Case #%d: YES\n",cas++);
        }
        else
        {
            printf("Case #%d: NO\n",cas++);
        }
    }
    return 0;
}
