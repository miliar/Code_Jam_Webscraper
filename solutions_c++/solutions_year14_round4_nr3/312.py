#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
using namespace std;

#define eps 1e-9
#define PB push_back
#define LL long long
#define INF 0x3f3f3f3f

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}
const int MAXN = 100005;
const int MAXM = MAXN * 10;

struct FlowNetwork
{
    struct Edge {
        int from, to, val, next;
        void init(int _from, int _to, int _val, int _next)
        {
            from = _from, to = _to, val = _val;
            next = _next;
        }
    } e[MAXM];

    int v[MAXN], que[MAXN], dis[MAXN], cnt, cur[MAXN];

    void insert(int from, int to, int val)
    {
        //cout << from << " " << to << " " << val << endl;
        e[cnt].init(from, to, val, v[from]);
        v[from] = cnt++;
        e[cnt].init(to, from, 0, v[to]);
        v[to] = cnt++;
    }
    void init()
    {
        cnt = 0; //初始化
        memset(v, -1, sizeof(v)); //初始化
    }
    bool bfs(int n, int s, int t)
    {
        int head, tail, id;
        head = tail = 0;
        que[tail++] = s;
        fill(dis, dis + n, -1);
        dis[s] = 0;
        while(head < tail) // bfs,得到顶点i的距s的最短距离dis[i]
        {
            for(id = v[que[head++]]; id != -1; id = e[id].next)
                if(e[id].val > 0 && dis[e[id].to] == -1)
                {
                    dis[e[id].to] = dis[e[id].from] + 1;
                    que[tail++] = e[id].to;
                    if(e[id].to == t) return true;
                }
        }
        return false;
    }

    int maxflow(int n, int s, int t)
    {
        int ret = 0, tmp, i;
        while(bfs(n, s, t))
        {
            int u = s, tail = 0;
            for(i = 0; i < n; i++) cur[i] = v[i];
            while(cur[s] != -1)
            {
                if (u != t && cur[u] != -1 && e[cur[u]].val > 0 && dis[u] + 1 == dis[e[cur[u]].to])
                {
                    que[tail++] = cur[u];
                    u = e[cur[u]].to;
                }
                else if (u == t)
                {
                    for(tmp = INF, i = tail - 1; i >= 0; i--) tmp = min(tmp, e[que[i]].val);
                    if(tail == 0)  break;
                    for(ret += tmp, i = tail - 1; i >= 0; i--)
                    {
                        e[que[i]].val -= tmp;
                        e[que[i] ^ 1].val += tmp;
                        if(e[que[i]].val == 0) tail = i;
                    }
                    u = e[que[tail]].from;
                }
                else
                {
                    while(tail > 0 && u != s && cur[u] == -1)
                        u = e[que[--tail]].from;
                    cur[u] = e[cur[u]].next;
                }
            }
        }
        return ret;
    }
}flowNetwork;
/*
1 ≤ T ≤ 100.
0 ≤ X0 ≤ X1 < W.
0 ≤ Y0 ≤ Y1 < H.
Small dataset

3 ≤ W < 100.
3 ≤ H < 500.
0 ≤ B < 10.

*/
const int N = 105;
int w, h, g[N][5 * N];
int mv[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
int in(int x, int y)
{
    return 2 * (x * h + y);
}
int out(int x, int y)
{
    return 2 * (x * h + y) + 1;
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int t, cas = 1, b, i, j, k;
    int x1, x2, y1, y2;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d", &w, &h, &b);
        memset(g, 0, sizeof(g));
        for(i = 0; i < b; i++)
        {
             scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
             for(j = x1; j <= x2; j++)
                for(k = y1; k <= y2; k++)
                    g[j][k] = 1;
        }
        int s = 2 * w * h;
        int t = 2 * w * h + 1;
        flowNetwork.init();
        for(i = 0; i < w; i++)
        {
            if(!g[i][0])        flowNetwork.insert(s, in(i, 0), 1);
            if(!g[i][h - 1])    flowNetwork.insert(out(i, h - 1), t, 1);
        }
        for(i = 0; i < w; i++)
        {
            for(j = 0; j < h; j++)
            {
                if(g[i][j])    continue;
                flowNetwork.insert(in(i, j), out(i, j), 1);
                for(k = 0; k < 4; k++)
                {
                    int tx = i + mv[k][0];
                    int ty = j + mv[k][1];
                    if(tx >= 0 && tx < w && ty >= 0 && ty < h && !g[tx][ty])
                        flowNetwork.insert(out(i, j), in(tx, ty), 1);
                }
            }
        }
        printf("Case #%d: %d\n", cas++, flowNetwork.maxflow(2 * w * h + 2, s, t));

    }
    return 0;
}
/*
2
3 3 2
2 0 2 0
0 2 0 2
5 6 4
1 0 1 0
3 1 3 3
0 2 1 3
1 5 2 5
*/
