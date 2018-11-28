#pragma warning(disable:4996)

#include <stdio.h>

int r,c;
int m[400];

int d[100][100];
bool found;

int dm[400];
int shoot(int x, int y, int dx, int dy)
{
    if (y==-1) return c+r+c+r-x-1;
    if (x==-1) return y;
    if (x==r) return c+r+c-y-1;
    if (y==c) return c+x;

    if (d[x][y]==0)
    {
        if (dx==1)
            return shoot(x, y-1, 0, -1);
        else if (dx==-1)
            return shoot(x, y+1, 0, 1);
        else if (dy==1)
            return shoot(x-1, y, -1, 0);
        else
            return shoot(x+1, y, 1, 0);
    }
    else
    {
        if (dx==1)
            return shoot(x, y+1, 0, 1);
        else if (dx==-1)
            return shoot(x, y-1, 0, -1);
        else if (dy==1)
            return shoot(x+1, y, 1, 0);
        else
            return shoot(x-1, y, -1, 0);
    }
}

bool isans()
{
    for (int i=0; i<c; i++)
    {
        if (m[i] != shoot(0, i, 1, 0))
            return false;
    }
    for (int i=0; i<r; i++)
    {
        if (m[c+i] != shoot(i, c-1, 0, -1))
            return false;
    }
    for (int i=0; i<c; i++)
    {
        if (m[c+r+c-i-1] != shoot(r-1, i, -1, 0))
            return false;
    }
    for (int i=0; i<r; i++)
    {
        if (m[c+r+c+r-i-1] != shoot(i, 0, 0, 1))
            return false;
    }
    return true;
}

void dfs(int x, int y)
{
    if (x==r)
    {
        if (isans())
        {
            found = true;

            for (int i=0; i<r; i++)
            {
                for (int j=0; j<c; j++)
                    printf("%c", d[i][j]==0 ? '/' : '\\');
                printf("\n");
            }
        }

        return;
    }
    if (y==c)
        dfs(x+1, 0);

    else
    {
        d[x][y] = 0;
        dfs(x, y+1);
        if (found) return;

        d[x][y] = 1;
        dfs(x, y+1);
        if (found) return;
    }
}

int main()
{
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &r, &c);
        for (int i=0; i<r+c; i++)
        {
            int x,y;
            scanf("%d%d", &x, &y); x--; y--;
            m[x] = y;
            m[y] = x;
        }

        printf("Case #%d:\n", ++tt);
        found = false;
        dfs(0, 0);
        if (!found)
            printf("IMPOSSIBLE\n");
    }

    return 0;
}
