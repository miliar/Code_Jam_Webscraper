#include <stdio.h>
#include <string.h>

int mp[110][110];
int n,m;

bool ok()
{
    int i,j,k;
    int p,q;
    int v;
    for (i = 0;i < n;i++)
    {
        v = -1;
        for (j = 0;j < m;j++)
        {
            if (mp[i][j] > v)
                v = mp[i][j];
        }
        for (j = 0;j < m;j++)
        {
            if (mp[i][j] != v)
            {
                for (k = 0;k < n;k++)
                {
                    if (mp[k][j] > mp[i][j])
                        return 0;
                }
            }
        }
    }
    for (j = 0;j < m;j++)
    {
        v = -1;
        for (i = 0;i < n;i++)
        {
            if (mp[i][j] > v)
                v = mp[i][j];
        }
        for (i = 0;i < n;i++)
        {
            if (mp[i][j] != v)
            {
                for (k = 0;k < m;k++)
                {
                    if (mp[i][k] > mp[i][j])
                        return 0;
                }
            }
        }
    }
    return 1;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k;
    int t;
    scanf("%d", &t);
    int p,q;
    for (k = 1;k <= t;k++)
    {
        scanf("%d%d", &n, &m);
        for (i = 0;i < n;i++)
        {
            for (j = 0;j < m;j++)
                scanf("%d", &mp[i][j]);
        }
        printf("Case #%d: ", k);
        if (ok())
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
