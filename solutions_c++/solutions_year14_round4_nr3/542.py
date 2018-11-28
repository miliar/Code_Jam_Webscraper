#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define all(o) (o).begin(), (o).end()
#define allr(o) (o).rbegin(), (o).rend()
const int INF = 2147483647;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> int size(T &x) { return x.size(); }

// assert or gtfo


#define MAXV 600 * 600 * 2 * 4 + 600
int q[MAXV], d[MAXV];
struct flow_network {
    struct edge {
        int v, cap, nxt;
        edge() { }
        edge(int _v, int _cap, int _nxt) : v(_v), cap(_cap), nxt(_nxt) { }
    };
    int n, ecnt, *head, *curh;
    vector<edge> e, e_store;
    flow_network(int _n, int m = -1) : n(_n), ecnt(0) {
        e.reserve(2 * (m == -1 ? n : m));
        head = new int[n], curh = new int[n];
        memset(head, -1, n * sizeof(int));
    }
    void destroy() { delete[] head; delete[] curh; }
    void reset() { e = e_store; }
    void add_edge(int u, int v, int uv, int vu = 0) {
        e.push_back(edge(v, uv, head[u])); head[u] = ecnt++;
        e.push_back(edge(u, vu, head[v])); head[v] = ecnt++;
    }
    int augment(int v, int t, int f) {
        if (v == t) return f;
        for (int &i = curh[v], ret; i != -1; i = e[i].nxt)
            if (e[i].cap > 0 && d[e[i].v] + 1 == d[v])
                if ((ret = augment(e[i].v, t, min(f, e[i].cap))) > 0)
                    return (e[i].cap -= ret, e[i^1].cap += ret, ret);
        return 0;
    }
    int max_flow(int s, int t, bool res = true) {
        if(s == t) return 0;
        e_store = e;
        int f = 0, x, l, r;
        while (true) {
            memset(d, -1, n * sizeof(int));
            l = r = 0, d[q[r++] = t] = 0;
            while (l < r)
                for (int v = q[l++], i = head[v]; i != -1; i = e[i].nxt)
                    if (e[i^1].cap > 0 && d[e[i].v] == -1)
                        d[q[r++] = e[i].v] = d[v]+1;
            if (d[s] == -1) break;
            memcpy(curh, head, n * sizeof(int));
            while ((x = augment(s, t, INF)) != 0) f += x;
        }
        if (res) reset();
        return f;
    }
};

bool empty[600][600];

int main()
{
    int ts;
    scanf("%d\n", &ts);

    for (int t = 0; t < ts; t++)
    {
        printf("Case #%d: ", t+1);

        int w, h, b;
        scanf("%d %d %d\n", &w, &h, &b);

        int source = 0,
            sink = 1,
            v_in = sink + 1,
            v_out = v_in + w * h,
            cnt = v_out + w * h;

        for (int i = 0; i < w; i++)
            for (int j = 0; j < h; j++)
                empty[i][j] = true;

        for (int i = 0; i < b; i++)
        {
            int x0, y0, x1, y1;
            scanf("%d %d %d %d\n", &x0, &y0, &x1, &y1);

            for (int x = x0; x <= x1; x++)
                for (int y = y0; y <= y1; y++)
                    empty[x][y] = false;
        }

        // printf("\n");
        // for (int i = 0; i < w; i++)
        // {
        //     for (int j = 0; j < h; j++)
        //     {
        //         if (empty[i][j])
        //         {
        //             if (j == 0)
        //                 printf("I");
        //             else if (j == h - 1)
        //                 printf("O");
        //             else
        //                 printf(" ");
        //         }
        //         else
        //         {
        //             printf("#");
        //         }
        //     }

        //     printf("\n");
        // }

        flow_network g(cnt);

        for (int i = 0; i < w; i++)
        {
            if (empty[i][0])
                g.add_edge(source, v_in + i * h + 0, 1);

            if (empty[i][h - 1])
                g.add_edge(v_out + i * h + (h - 1), sink, 1);
        }

        for (int i = 0; i < w; i++)
            for (int j = 0; j < h; j++)
                if (empty[i][j])
                    g.add_edge(v_in + i * h + j, v_out + i * h + j, 1);

        for (int i = 0; i < w; i++)
        {
            for (int j = 0; j < h; j++)
            {
                for (int di = -1; di <= 1; di++)
                {
                    for (int dj = -1; dj <= 1; dj++)
                    {
                        if ((di == 0) == (dj == 0))
                            continue;

                        int ni = i + di,
                            nj = j + dj;

                        if (0 <= ni && ni < w && 0 <= nj && nj < h)
                        {
                            g.add_edge(v_out + i * h + j, v_in + ni * h + nj, 1);
                        }
                    }
                }
            }
        }

        printf("%d\n", g.max_flow(source, sink));
    }

    return 0;
}

