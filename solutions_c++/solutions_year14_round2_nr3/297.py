#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 70;
int zip[N], order[N], n;

bool edge[N][N];

struct town { int z, i; } towns[N];
bool operator<(town a, town b) { return a.z < b.z; }

bool markn[N];
bool mark[N];

bool dfs_nr(int x, int o)
{
    markn[x] = true;
    for(int i = 0; i < n; i++)
        if(edge[x][i] && mark[i] && i != o) return false;
    for(int i = 0; i < n; i++)
        if(edge[x][i] && !markn[i])
            if(!dfs_nr(i, o)) return false;
    return true;
}

bool noreturn(int origin, int x)
{
    for(int i = 0; i < N; i++) markn[i] = mark[i];
    return dfs_nr(x, origin);
}

void dfs(int curr)
{
    printf("%i", zip[curr]);
    mark[curr] = true;

    int must[N];
    for(int i = 0; i < n; i++)
        if(!mark[i] && edge[curr][i] && noreturn(curr, i)) must[i] = true;
        else must[i] = false;

    int l = -1;
    for(int i = 0; i < n; i++)
        if(must[i]) l = i;

    bool been = false;

    bool skip = false;
    for(int i = 0; i < n; i++)
    {
        for(int ii = 0; ii < n; ii++)
        if(!mark[ii] && edge[curr][ii] && noreturn(curr, ii)) must[ii] = true;
        else must[ii] = false;

        for(int ii = 0; ii < n; ii++) if(must[ii]) l = max(ii, l);

        if(!mark[i])
            if(edge[curr][i])
                {if(must[i] || i < l || !skip) { been = true; dfs(i);}
                else skip = true;}
    }

}

int ok(int x, int a[], int p)
{
    if(p >= n) return p;
    if(x != a[p]) return p;
    p++;
    while(p < n && edge[x][a[p]])
        p = ok(a[p], a, p);
    return p;
}

void do_brute()
{
    int a[N];
    for(int i = 0; i < n; i++) a[i] = i;
    do
    {
        int b[N];
        for(int i = 0; i < n; i++) b[i] = towns[a[i]].i;

        //printf("%i", ok(towns[0].i, b, 0));
        if(ok(towns[0].i, b, 0) == n)
        {
            for(int i = 0; i < n; i++) printf("%i", zip[b[i]]); return;
        }
    } while(next_permutation(a, a + n));
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    scanf("%i", &t);

    for(int te = 1; te <= t; te++)
    {
        printf("Case #%i: ", te);

        int m;
        scanf("%i %i", &n, &m);

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                edge[i][j] = false;

        for(int i = 0; i < n; i++) scanf("%i", &zip[i]);
        for(int i = 0; i < m; i++)
        {
            int u, v;
            scanf("%i %i", &u, &v); u--; v--;
            edge[u][v] = edge[v][u] = true;
        }

        for(int i = 0; i < n; i++) { towns[i].z = zip[i]; towns[i].i = i; }
        sort(towns, towns + n);
        for(int i = 0; i < n; i++)
            order[towns[i].i] = i;

        //dfs(towns[0].i);

        do_brute();
        printf("\n");
    }
    return 0;
}
