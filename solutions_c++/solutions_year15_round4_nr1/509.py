#include <cstdio>

int  mn[1000][2];
int mx[1000][2];
char mat[1000][1000];
char s[1000];
void solve(int tp)
{
    int n,m;
    scanf("%d %d",&n,&m);
    for(int i = 0; i < 1000; i++)
        mn[i][0] = mn[i][1] = 10000;
    for(int i = 0; i < 1000; i++)
        mx[i][0] = mx[i][1] = -1;
    for(int i = 0; i < n; i++)
    {
        scanf("%s",mat[i]);
    }
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            if (mat[i][j] == '.')
                continue;
            if (i < mn[j][0])
                mn[j][0] = i;
            if (j < mn[i][1])
                mn[i][1] = j;
        }
    }
    for(int i = n-1; i >= 0; i--)
    {
        for(int j = m-1; j >= 0; j--)
        {
            if (mat[i][j] == '.')
                continue;
            if (i > mx[j][0])
                mx[j][0] = i;
            if (j > mx[i][1])
                mx[i][1] = j;
        }
    }
    bool pos = true;
    int sol = 0;
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            if (mat[i][j] == '.')
                continue;
            if (mn[j][0] == i && mn[i][1] == j &&
                mx[j][0] == i && mx[i][1] == j)
                pos = false;
            if (mat[i][j] == '^')
                if (i == mn[j][0])
                    sol++;
            if (mat[i][j] == 'v')
                if (i == mx[j][0])
                    sol++;
            if (mat[i][j] == '<')
                if (j == mn[i][1])
                    sol++;
            if (mat[i][j] == '>')
                if (j == mx[i][1])
                    sol++;
        }
    }
    printf("Case #%d: ",tp);
    if (pos)
        printf("%d\n",sol);
    else
        printf("IMPOSSIBLE\n");
}

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int n;
    scanf("%d",&n);
    for(int i = 1 ; i<= n;  i++)
        solve(i);
    return 0;
}
