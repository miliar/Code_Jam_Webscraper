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

const int MAXN = 100000; // число вершин
const int INF = 1000000000; // константа-бесконечность
 
struct edge {
	int a, b, cap, flow;
};
 
int n, s, t, d[MAXN], ptr[MAXN], q[MAXN];
vector<edge> e;
vector<int> g[MAXN];
 
void add_edge (int a, int b, int cap) {
    // cout << "add " << a << " " << b << endl;
	edge e1 = { a, b, cap, 0 };
	edge e2 = { b, a, 0, 0 };
	g[a].push_back ((int) e.size());
	e.push_back (e1);
	g[b].push_back ((int) e.size());
	e.push_back (e2);
}
 
bool bfs() {
	int qh=0, qt=0;
	q[qt++] = s;
	memset (d, -1, n * sizeof d[0]);
	d[s] = 0;
	while (qh < qt && d[t] == -1) {
		int v = q[qh++];
		for (size_t i=0; i<g[v].size(); ++i) {
			int id = g[v][i],
				to = e[id].b;
			if (d[to] == -1 && e[id].flow < e[id].cap) {
				q[qt++] = to;
				d[to] = d[v] + 1;
			}
		}
	}
	return d[t] != -1;
}
 
int dfs (int v, int flow) {
	if (!flow)  return 0;
	if (v == t)  return flow;
	for (; ptr[v]<(int)g[v].size(); ++ptr[v]) {
		int id = g[v][ptr[v]],
			to = e[id].b;
		if (d[to] != d[v] + 1)  continue;
		int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
		if (pushed) {
			e[id].flow += pushed;
			e[id^1].flow -= pushed;
			return pushed;
		}
	}
	return 0;
}
 
int dinic() {
	int flow = 0;
	for (;;) {
		if (!bfs())  break;
		memset (ptr, 0, n * sizeof ptr[0]);
		while (int pushed = dfs (s, INF))
			flow += pushed;
	}
	return flow;
}

int r;
vector<string> lines[MAXN];

int main(int argc, char* argv[])
{
    string c;
    int tt;
    getline(cin, c);
    sscanf(c.c_str(), "%d", &tt);

    forn(test, tt)
    {
        getline(cin, c);
        sscanf(c.c_str(), "%d", &r);
        forn(i, MAXN)
            lines[i].clear();
        set<string> wds;
        forn(i, r)
        {
            stringstream ss;
            string s;
            getline(cin, s);
            ss << s;
            while (ss >> s)
            {
                lines[i].push_back(s);
                wds.insert(s);
            }
        }
        
        n = s = t = 0;
        forn(i, MAXN)
        {
            d[i] = ptr[i] = q[i] = 0;
            g[i].clear();
        }
        e.clear();

        map<string, set<int> > f;
        forn(i, r)
            forn(j, lines[i].size())
                f[lines[i][j]].insert(i);

        n = r + wds.size();
        
        int nxt = r - 1;
        for (set<string>::iterator i = wds.begin(); i != wds.end(); i++)
        {
            string s = *i;
            nxt++;
            //cout << s << endl;
            for (set<int>::iterator j = f[s].begin(); j != f[s].end(); j++)
            {
                add_edge(nxt, *j, 1), add_edge(*j, nxt, 1);
            }
        }
        

        //cout << "ok " << endl;
        //cout << "n=" << n << endl;
        s = 0;
        t = 1;
        cout << "Case #" << (test + 1) << ": " << dinic() << endl;
    }

    return 0;
}
