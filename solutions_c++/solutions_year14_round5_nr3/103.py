#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

const int INF = 1000*1000*1000;

struct rib {
    int b, u, c, f;
    size_t back;
};

vector < vector<rib> > g;

int ef = 0;

void add_rib (int a, int b, int u, int c) {
    //cout << "add " << a << " " << b << endl;
    rib r1 = { b, u, c, 0, g[b].size() };
    rib r2 = { a, 0, -c, 0, g[a].size() };
    g[a].push_back (r1);
    g[b].push_back (r2);
}

int mincostflow(vector < vector<rib> > & g, int s, int t)
{
    int n = g.size();
    int k = 100500;

    int flow = 0,  cost = 0;
    while (flow < k) {
        vector<int> id (n, 0);
        vector<int> d (n, INF);
        vector<int> q (n);
        vector<int> p (n);
        vector<size_t> p_rib (n);
        int qh=0, qt=0;
        q[qt++] = s;
        d[s] = 0;
        while (qh != qt) {
            int v = q[qh++];
            id[v] = 2;
            if (qh == n)  qh = 0;
            for (size_t i=0; i<g[v].size(); ++i) {
                rib & r = g[v][i];
                if (r.f < r.u && d[v] + r.c < d[r.b]) {
                    d[r.b] = d[v] + r.c;
                    if (id[r.b] == 0) {
                        q[qt++] = r.b;
                        if (qt == n)  qt = 0;
                    }
                    else if (id[r.b] == 2) {
                        if (--qh == -1)  qh = n-1;
                        q[qh] = r.b;
                    }
                    id[r.b] = 1;
                    p[r.b] = v;
                    p_rib[r.b] = i;
                }
            }
        }
        if (d[t] == INF)  break;
        int addflow = k - flow;
        for (int v=t; v!=s; v=p[v]) {
            int pv = p[v];  size_t pr = p_rib[v];
            addflow = min (addflow, g[pv][pr].u - g[pv][pr].f);
        }
        for (int v=t; v!=s; v=p[v]) {
            int pv = p[v];  size_t pr = p_rib[v],  r = g[pv][pr].back;
            g[pv][pr].f += addflow;
            g[v][r].f -= addflow;
            cost += g[pv][pr].c * addflow;
        }
        flow += addflow;
    }

    if (flow != ef)
        cost = -1;

    return cost;
}

const int R = 50;

int result;

void readData()
{
    int nn;
    cin >> nn;
    vector<string> e(nn);
    vector<int> id(nn);

    int a = 0, b = 0;
    vector<int> index(nn);

    forn(i, nn)
    {
        cin >> e[i] >> id[i];
        if (e[i] == "E")
        {
            index[i] = a;
            a++;
        }
        else
        {
            index[i] = b;
            b++;
        }
    }

    int n = R + a + b + R + 2 + 2;
    int s = R + a + b + R;
    int t = R + a + b + R + 1;
    int S = R + a + b + R + 2;
    int T = R + a + b + R + 3;

    g = vector<vector<rib> >(n);

    forn(i, R)
    {
        add_rib(s, i, 1, 0);
        add_rib(R + a + b + i, t, 1, 1);
    }

    add_rib(t, s, 10 * n, 0);

    ef = 0;
    int x = 0, y = 0;

    forn(i, R)
    {
                set<int> u;
                for (int j = 0; j < nn; j++)
                {
                    if (e[j] == "L")
                    {
                        if (id[j] == 0)
                            add_rib(i, R + a + index[j], 1, 0);
                        else
                        {
                            if (u.count(id[j]) == 0)
                            {
                                add_rib(i, R + a + index[j], 1, 0);
                                u.insert(id[j]);
                            }
                        }
                    }
                    if (id[j] != 0)
                        u.insert(id[j]);
                }

                forn(j, R)
                    add_rib(i, R + a + b + j, 1, 0);
    }

    forn(i, nn)
        if (e[i] == "E")
        {
            set<int> u;
            if (id[i] == 0)
            {
                for (int j = i + 1; j < nn; j++)
                {
                    if (e[j] == "L")
                    {
                        if (id[j] == 0)
                            add_rib(R + index[i], R + a + index[j], 1, 0);
                        else
                        {
                            if (u.count(id[j]) == 0)
                            {
                                add_rib(R + index[i], R + a + index[j], 1, 0);
                                u.insert(id[j]);
                            }
                        }
                    }
                    if (id[j] != 0)
                        u.insert(id[j]);
                }
            }
            else
            {
                for (int j = i + 1; j < nn; j++)
                {
                    if (e[j] == "L")
                    {
                        if (id[j] == 0)
                        {
                            if (u.count(id[i]) == 0)
                                add_rib(R + index[i], R + a + index[j], 1, 0);
                        }
                        else
                        {
                            if (u.count(id[j]) == 0 && id[j] == id[i])
                            {
                                add_rib(R + index[i], R + a + index[j], 1, 0);
                                u.insert(id[j]);
                            }
                        }
                    }
                    if (id[j] != 0)
                        u.insert(id[j]);
                }
            }

            if (id[i] == 0 || u.count(id[i]) == 0)
               forn(j, R)
                    add_rib(R + index[i], R + a + b + j, 1, 0);

            add_rib(S, R + index[i], 1, 0);
            add_rib(s, T, 1, 0);
            ef++;
        }
        else
        {
            add_rib(R + a + index[i], T, 1, 0);
            add_rib(S, t, 1, 0);
            ef++;
        }

    result = mincostflow(g, S, T);
}

int main(int argc, char* argv[])
{
    //freopen("input.txt", "rt", stdin);
    int tt;
    cin >> tt;

    int fromTest = 1;
    int toTest = tt;

    if (argc == 3)
    {
        fromTest = atoi(argv[1]);
        toTest = atoi(argv[2]);
    }

    cerr << "Solving " << fromTest << " ... " << toTest << endl;

    for (int tx = 1; tx <= tt; tx++)
    {
        readData();
        if (tx >= fromTest && tx <= toTest)
        {
            if (result == -1)
                cout << "Case #" << (tx) << ": CRIME TIME" << endl;
            else
                cout << "Case #" << (tx) << ": " << result << endl;
        }
    }
}
