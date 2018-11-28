#include <bits/stdc++.h>

using namespace std;

char color[3] = {'P', 'R', 'S'};

int opp[3] = {1, 2, 0};
int los[3] = {2, 0, 1};

int a[100005], kq[100005];
int f[5][20][5];
int *st[5][20];

bool cmp(int m, int *a, int *kq)
{
    for(int i=0; i<m; i++)
    if (a[i] < kq[i])
        return 1;
    return 0;
}

void ghep(int m, int *a, int *b)
{
    for(int i=0; i<m; i++)
        a[i] = b[i];
}

void prep()
{
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            if (i!=j)
                f[i][0][j] = 0;
            else f[i][0][j] = 1;
        }
        st[i][0] = new int[1];
        st[i][0][0] = i;
    }
    for(int k=1; k<=12; k++)
    {
        for(int i=0; i<3; i++)
        {
            int ip = opp[i];
            for(int j=0; j<3; j++)
            {
                f[i][k][j] = f[i][k-1][j] + f[ip][k-1][j];
            }
            st[i][k] = new int[(1<<k)];
            if (cmp(1<<(k-1), st[i][k-1], st[ip][k-1]))
            {
                ghep(1<<(k-1), st[i][k], st[i][k-1]);
                ghep(1<<(k-1), st[i][k]+(1<<(k-1)), st[ip][k-1]);
            } else
            {
                ghep(1<<(k-1), st[i][k], st[ip][k-1]);
                ghep(1<<(k-1), st[i][k]+(1<<(k-1)), st[i][k-1]);
            }
        }
    }
}


int main()
{
    freopen("al.in", "r", stdin);
    freopen("testAl.out", "w", stdout);
    prep();
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ", t);
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        bool found = 0;
        for(int i=0; i<3; i++)
        if (r == f[i][n][1] && p == f[i][n][0] && s == f[i][n][2])
        {
            if (!found)
            {
                found = 1;
                for(int j=0; j<(1<<n); j++)
                    kq[j] = st[i][n][j];
            } else
            {
                if (cmp(1<<n, st[i][n], kq))
                {
                    for(int j=0; j<(1<<n); j++)
                        kq[j] = st[i][n][j];
                }
            }
        }
        if (!found)
            printf("IMPOSSIBLE\n");
        else
        {
            for(int i=0; i<(1<<n); i++)
                printf("%c", color[kq[i]]);
            printf("\n");
        }
    }
    for(int k=0; k<=12; k++)
        for(int i=0; i<3; i++)
            delete[]st[i][k];
    return 0;
}
