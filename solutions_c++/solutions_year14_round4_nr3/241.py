#include <cstdio>
#include <climits>
#include <cstring>
#include <algorithm>
using namespace std;

const int SIZE = 500 * 100 * 3;
const int EDGE_SIZE = SIZE * 10;
const int INF = INT_MAX;

struct Edge
{
    int c;
    int f;
    int to;
    Edge* rev;
    Edge* next;
    
    Edge* get(int cc, int ff, int tt, Edge* rr, Edge* nn)
    {
        c = cc;
        f = ff;
        to = tt;
        rev = rr;
        next = nn;
        return this;
    }
}nodes[EDGE_SIZE];

int loc;
int mf_source;
int mf_sink;

Edge* adj[SIZE];

bool pass[SIZE];


int aug(int n, int minf)
{
    pass[n] = true;

    if(n == mf_sink)
            return minf;
    else
    {
        for(Edge* p = adj[n]; p; p = p->next)
            if(!pass[p->to] && p->c - p->f > 0)
            {
                int t = aug(p->to, min(minf, p->c - p->f));
                if(t)
                {
                    p->f += t;
                    p->rev->f -= t;
                    return t;
                }
            }

        return 0;
    }
}
int maxf(int S, int T)
{
    mf_source = S;
    mf_sink = T;
     
    int ans = 0;
    int t = 0;

    do
    {
        memset(pass, 0, sizeof(pass));
        t = aug(mf_source, INF);
        ans += t;
    }
    while(t);

    return ans;
}

void init()
{
    memset(adj, 0, sizeof(adj));
    loc = 0;
}

void add_edge(int a, int b, int c)
{
    adj[a] = nodes[loc].get(c, 0, b, nodes + loc + 1, adj[a]);
    adj[b] = nodes[loc + 1].get(0, 0, a, nodes + loc, adj[b]);
    loc += 2;
}

#include <cstdio>
using namespace std;



int gg[600][600];
int W, H, B;

int node(int x, int y, int o)
{
    return ((x - 1) * H + y - 1) * 2 + o;
}

int main()
{
    memset(gg, -1, sizeof(gg));
    int T;
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++)
    {
        printf("Case #%d: ", tt);
    memset(gg, -1, sizeof(gg));

init();
        scanf("%d%d%d", &W, &H, &B);
        for(int i = 1; i <= W; i++)
        for(int j = 1; j <= H; j++)
        gg[i][j] = 0;
        for(int i = 0; i < B; i++)
        {
            int x0, y0, x1, y1;
            scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
            for(int x = x0 + 1; x <= x1 + 1; x++)
                for(int y = y0 + 1; y <= y1 + 1; y++)
                    gg[x][y] = -1;
        }
        for(int i = 1; i <= W; i++)
            for(int j = 1; j <= H; j++)
              if(gg[i][j] != -1)
              {
                add_edge(node(i, j, 0), node(i, j, 1), 1);
                for(int d = 0; d < 4; d++)
                {
                    int x = i + "0121"[d] - '1';
                    int y = j + "1210"[d] - '1';
                    if(gg[x][y] != -1)
                        add_edge(node(i, j, 1), node(x, y, 0), 1);
                }
              }

        for(int i = 1; i <= W; i++)
        {
            add_edge(H * W * 2,node(i, 1, 0), 1);
            add_edge(node(i, H, 1), H * W * 2 + 1, 1);
}

        printf(" %d\n", maxf(H * W * 2, H * W * 2 + 1));
    }
    return 0;
}
