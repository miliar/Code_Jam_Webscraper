#pragma warning(disable:4996)

#include <stdio.h>
#include <algorithm>
using namespace std;

int n;
int d[25][25];

int ans;
int v[25][25];

int c[25];
bool possible(int* s, int x)
{
    if (x==n) return true;

    bool t = false;
    for (int i=0; i<n; i++)
    {
        if (v[s[x]][i] && !c[i])
        {
            t = true;
            c[i] = true;
            bool r = possible(s, x+1);
            c[i] = false;

            if (!r) return false;
        }
    }

    return t;
}

void dfs(int x, int y)
{
    if (x==n)
    {
        int c=0;
        for (int i=0; i<n; i++) for (int j=0; j<n; j++)
        {
            if (d[i][j] && !v[i][j]) return;
            if (!d[i][j] && v[i][j]) c++;
        }

        int s[25];
        for (int i=0; i<n; i++) s[i]=i;
        do
        {
            if (!possible(s, 0))
                return;
        } while (next_permutation(s, s+n));

        if (ans==-1 || ans > c)
            ans=c;

        return;
    }
    if (y==n) {dfs(x+1,0); return;}
    v[x][y] = 0; dfs(x, y+1);
    v[x][y] = 1; dfs(x, y+1);
}

int main()
{
    freopen("D-small.in", "r", stdin);
    freopen("D-small.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for (int i=0; i<n; i++)
        {
            char s[100];
            scanf("%s", s);

            for (int j=0; j<n; j++)
                d[i][j] = s[j]-'0';
        }

        ans=-1;
        dfs(0,0);
        printf("Case #%d: %d\n", ++tt, ans);
    }
    return 0;
}
