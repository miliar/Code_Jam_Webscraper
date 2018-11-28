#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
const int MAXN = 1009, MAXM = 40009;
long long data[MAXM], p[MAXN], dist[MAXN];
int edge[MAXM], next[MAXM], head[MAXN], id, n, m, que[MAXM], q;
bool v[MAXN];
struct F
{
    int s, t;
    long long ans;
}f[20009];
inline void __add(int u, int v, long long val)
{
    data[id] = val;
    edge[id] = v;
    next[id] = head[u];
    head[u] = id++;
}
inline void add(int u, int v, long long val)
{
    __add(u, v, val);
    __add(v, u, val);
}
void init()
{
    id = 0;
    memset(head, -1, sizeof(head));
}
void spfa(int s)
{
    for (int i = 1; i <= n; ++i)
    {
        dist[i] = -1;
    }
    memset(v, 0, sizeof(v));
    dist[s] = 0;
    int top = 1, tail = 1;
    que[1] = s;
    v[s] = true;
    while (top <= tail)
    {
        int now = que[top++];
        for (int i = head[now]; ~i; i = next[i])
        {
            int to = edge[i];
            if (p[to] > p[s]) continue;
            if (dist[to] == -1 || dist[now] + data[i] < dist[to])
            {
                dist[to] = dist[now] + data[i];
                if (!v[to])
                {
                    que[++tail] = to;
                    v[to] = true;
                }
            }
        }
        v[now] = false;
    }
    for (int i = 1; i <= q; ++i)
    {
        int x = f[i].s, y = f[i].t;
        if (dist[x] != -1 && dist[y] != -1)
        {
            if (dist[x] + dist[y] + p[s] < f[i].ans || f[i].ans == -1)
            {
                f[i].ans = dist[x] + dist[y] + p[s];
            }
        }
    }
}
int main()
{
    //freopen("in.txt", "r", stdin);
    while (scanf("%d%d", &n, &m),n + m)
    {
        init();
        for (int i = 1; i <= n; ++i)
        {
           scanf("%lld", &p[i]);
        }
        for (int i = 1; i <= m; ++i)
        {
            int x, y;
            long long z;
            scanf("%d%d%lld", &x, &y, &z);
            add(x, y, z);
        }
        scanf("%d", &q);
        for (int i = 1; i <= q; ++i)
        {
            scanf("%d%d", &f[i].s, &f[i].t);
            f[i].ans = -1;
        }
        for (int i = 1; i <= n; ++i) spfa(i);
        for (int i = 1; i <= q; ++i)
        {
            printf("%lld\n", f[i].ans);
        }
        printf("\n");
    }
    return 0;
}