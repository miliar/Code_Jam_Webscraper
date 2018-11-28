#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define MP make_pair
#define F first
#define S second

struct MaximalFlow
{
    struct edge
    {
        int to, capacity, flow, rev;

        edge() {}
        edge(int _to, int _capacity, int _rev)
        {
            to = _to;
            capacity = _capacity;
            flow = 0;
            rev = _rev;
        }

        void pushFlow(int addFlow)
        {
            flow += addFlow;
        }

        bool isOpen(int minimum)
        {
            return capacity - flow >= minimum;
        }
    };

    vector<int> good;
    vector<vector<edge> > graph;
    vector<int> distance;
    int currentMinimum;
    int start;
    int fin;
    const static long long inf = 1000 * 1000 * 1000;

    bool dfs(int v)
    {
        if (v == fin)
            return true;
        if (distance[v] >= distance[fin])
            return false;
        for (; good[v] < graph[v].size(); ++good[v])
            if (graph[v][good[v]].isOpen(currentMinimum) && distance[graph[v][good[v]].to] == distance[v] + 1 &&
                dfs(graph[v][good[v]].to))
                return true;
        return false;
    }

    bool bfs()
    {
        int n = graph.size();
        distance.assign(n, inf);
        distance[start] = 0;
        queue<int> q;
        q.push(start);

        while (!q.empty())
        {
            int v = q.front();
            if (v == fin)
                break;
            q.pop();
            for (int i = 0; i < graph[v].size(); ++i)
            {
                int to = graph[v][i].to;
                if (graph[v][i].isOpen(currentMinimum) && distance[to] > distance[v] + 1)
                {
                    distance[to] = distance[v] + 1;
                    q.push(to);
                }
            }
        }
        return distance[fin] != inf;
    }

    void pushFlow()
    {
        int addFlow = inf;
        for (int i = start; i != fin; i = graph[i][good[i]].to)
            addFlow = min(addFlow, graph[i][good[i]].capacity - graph[i][good[i]].flow);

        for (int i = start; i != fin; i = graph[i][good[i]].to)
        {
            graph[i][good[i]].pushFlow(addFlow);
            int to = graph[i][good[i]].to;
            int id = graph[i][good[i]].rev;
            graph[to][id].pushFlow(-addFlow);
        }
    }

    void initialize(int n)
    {
        graph.resize(n);
        for (int i = 0; i < n; ++i)
            graph[i].clear();
    }

    void addEdge(int from, int to, int capactiy)
    {
        //cerr << from << " " << to << " " << capactiy << endl;
        int sizeFrom = graph[from].size();
        int sizeTo = graph[to].size();
        graph[from].push_back(edge(to, capactiy, sizeTo));
        graph[to].push_back(edge(from, 0, sizeFrom));
    }

    long long getMaximalFlow(int _start, int _fin, int maxCapacity)
    {
        start = _start;
        fin = _fin;
        currentMinimum = 1;
        int n = graph.size();
        for (;currentMinimum > 0; currentMinimum /= 2)
            while (bfs())
            {
                good.assign(n, 0);
                while (dfs(start))
                    pushFlow();
            }
        long long flow = 0;
        for (int i = 0; i < graph[start].size(); ++i)
            flow += (long long)graph[start][i].flow;
        return flow;
    }

};

const int N = 505;

bool used[N][N];
int id[N][N];
int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

void solve(int test)
{
    int w, h;
    cin >> w >> h;
    for (int i = 0; i < w; i++)
        for (int j = 0; j < h; j++)
        {
            used[i][j] = false;
            id[i][j] = 0;
        }
    int b;
    cin >> b;
    for (int i = 0; i < b; i++)
    {
        int xl, yl, xr, yr;
        cin >> xl >> yl >> xr >> yr;
        for (int x = xl; x <= xr; x++)
            for (int y = yl; y <= yr; y++)
                used[x][y] = true;
    }
    int tot = 1;
    for (int x = 0; x < w; x++)
        for (int y = 0; y < h; y++)
            if (!used[x][y])
            {
                id[x][y] = tot;
                tot += 2;
            }
    /*for (int x = 0; x < w; x++)
    {
        for (int y = 0; y < h; y++)
        {
            cout << id[x][y] << " ";
        }
        cout << endl;
    }*/
    tot++;
    int res = 0;
    if (tot > 2)
    {
        MaximalFlow g;
        g.initialize(tot);
        for (int x = 0; x < w; x++)
            if (id[x][0] > 0)
            {
                //cerr << id[x][0] << endl;
                g.addEdge(0, id[x][0], 1);
            }
        for (int x = 0; x < w; x++)
            if (id[x][h - 1] > 0)
            {
                //cerr << id[x][h - 1] + 1 << endl;
                g.addEdge(id[x][h - 1] + 1, tot - 1, 1);
            }
        for (int x = 0; x < w; x++)
            for (int y = 0; y < h; y++)
                if (id[x][y])
                {
                    //cerr << id[x][y] << " " << id[x][y] + 1 << endl;
                    g.addEdge(id[x][y], id[x][y] + 1, 1);
                }
        for (int x = 0; x < w; x++)
            for (int y = 0; y < h; y++)
                if (id[x][y])
                    for (int d = 0; d < 4; d++)
                    {
                        int nx = x + dx[d];
                        int ny = y + dy[d];
                        if (nx < 0 || ny < 0)
                            continue;
                        if (nx >= w || ny >= h)
                            continue;
                        if (!id[nx][ny])
                            continue;
                        g.addEdge(id[x][y] + 1, id[nx][ny], 1);
                    }
        res = g.getMaximalFlow(0, tot - 1, 1);
    }
    cerr << test << endl;
    cout << "Case #" << test << ": ";
    cout << res << "\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    #ifdef TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    cout.setf(ios::fixed);
    cout.precision(10);
    cerr.setf(ios::fixed);
    cerr.precision(10);

    int t;
    cin >> t;
    for (int q = 1; q <= t; q++)
        solve(q);

    return 0;
}
