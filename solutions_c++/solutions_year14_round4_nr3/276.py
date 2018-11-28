#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;

int maxflow(vector<multiset<int> >& graph, int s, int t)
{
    int N = (int)graph.size();
    for (int ans = 0; ; ++ans)
    {
        vector<int> prev(N, -1);
        queue<int> q;
        prev[s] = s;
        q.push(s);
        while (true)
        {
            if (q.empty())
                return ans;
            int u = q.front();
            q.pop();
            for (auto it = graph[u].begin(); it != graph[u].end(); ++it)
            {
                int v = *it;
                if (prev[v] != -1)
                    continue;
                prev[v] = u;
                if (v == t)
                    goto l_found;
                q.push(v);
            }
        }
    l_found:
        stack<int> path;
        for (int u = t; u != s; u = prev[u])
            path.push(u);
        int u = s;
        while (!path.empty())
        {
            int v = path.top();
            path.pop();
            auto it = graph[u].find(v);
            graph[u].erase(it);
            graph[v].insert(u);
            u = v;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int W, H, B;
        cin >> W >> H >> B;
        vector<int> X0(B);
        vector<int> Y0(B);
        vector<int> X1(B);
        vector<int> Y1(B);
        for (int i = 0; i < B; ++i)
        {
            cin >> X0[i] >> Y0[i] >> X1[i] >> Y1[i];
            ++X1[i];
            ++Y1[i];
        }
        vector<vector<bool> > grid(H);
        for (int i = 0; i < H; ++i)
            grid[i].assign(W, true);
        for (int i = 0; i < B; ++i)
        {
            for (int j = Y0[i]; j < Y1[i]; ++j)
            {
                for (int k = X0[i]; k < X1[i]; ++k)
                    grid[j][k] = false;
            }
        }
        int n = 0;
        int s = n++;
        vector<vector<int> > vs0(H);
        vector<vector<int> > vs1(H);
        for (int i = 0; i < H; ++i)
            vs0[i].assign(W, -1);
        for (int i = 0; i < H; ++i)
            vs1[i].assign(W, -1);
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                if (grid[i][j])
                {
                    vs0[i][j] = n++;
                    vs1[i][j] = n++;
                }
            }
        }
        int t = n++;

/*
        // DEBUG
        cerr << "n = " << n << endl;
        cerr << "s = " << s << endl;
        cerr << "t = " << t << endl;
        for (int i = H - 1; i >= 0; --i)
        {
            for (int j = 0; j < W; ++j)
            {
                cerr << " ";
                if (grid[i][j])
                    cerr << vs0[i][j];
                else
                    cerr << "-";
            }
            cerr << endl;
        }
        for (int i = H - 1; i >= 0; --i)
        {
            for (int j = 0; j < W; ++j)
            {
                cerr << " ";
                if (grid[i][j])
                    cerr << vs1[i][j];
                else
                    cerr << "-";
            }
            cerr << endl;
        }
*/

        vector<multiset<int> > graph(n);
        for (int j = 0; j < W; ++j)
        {
            if (grid[0][j])
                graph[s].insert(vs0[0][j]);
        }
        for (int j = 0; j < W; ++j)
        {
            if (grid[H - 1][j])
                graph[vs1[H - 1][j]].insert(t);
        }
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                if (grid[i][j])
                    graph[vs0[i][j]].insert(vs1[i][j]);
            }
        }
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W - 1; ++j)
            {
                if (grid[i][j] && grid[i][j + 1])
                {
                    graph[vs1[i][j]].insert(vs0[i][j + 1]);
                    graph[vs1[i][j + 1]].insert(vs0[i][j]);
                }
            }
        }
        for (int j = 0; j < W; ++j)
        {
            for (int i = 0; i < H - 1; ++i)
            {
                if (grid[i][j] && grid[i + 1][j])
                {
                    graph[vs1[i][j]].insert(vs0[i + 1][j]);
                    graph[vs1[i + 1][j]].insert(vs0[i][j]);
                }
            }
        }

/*
        // DEBUG
        for (int i = 0; i < n; ++i)
        {
            cerr << i << ":";
            for (auto it = graph[i].begin(); it != graph[i].end(); ++it)
                cerr << " " << *it;
            cerr << endl;
        }
*/

        int ans = maxflow(graph, s, t);
        cout << "Case #" << testcase << ": " << ans << "\n";
    }
    return 0;
}
