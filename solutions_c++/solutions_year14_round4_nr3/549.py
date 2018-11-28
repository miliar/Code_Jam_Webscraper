#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <stdint.h>

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <bitset>
#include <deque>
#include <list>
#include <stack>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define foreach(it, v) for(__typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define sz(v) int((v).size())

struct Edge
{
    int to, cap, flow;
    Edge * rev;

    Edge(int to, int cap)
        : to(to), cap(cap), flow(0), rev(0)
    { }
};

const int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, 1, -1};

int max_flow(int vertexes, int from, int to, vector < vector < Edge * > > & edges)
{
    int result = 0;
    vector < bool > used(vertexes);
    vector < int > came_from(vertexes);
    vector < Edge * > edge_used(vertexes);
    queue < int > q;
    while(true)
    {
        q.push(from);
        fill(used.begin(), used.end(), false);
        used[from] = true;
        while(!q.empty())
        {
            int u = q.front();
            q.pop();
            foreach(it, edges[u])
            {
                Edge * e = *it;
                if(e->flow < e->cap && !used[e->to])
                {
                    used[e->to] = true;
                    came_from[e->to] = u;
                    edge_used[e->to] = e;
                    q.push(e->to);
                }
            }
        }
        if(!used[to])
            break;
        ++result;
        int cursor = to;
        while(cursor != from)
        {
            Edge * e = edge_used[cursor];
            e->flow += 1;
            e->rev->flow -= 1;
            cursor = came_from[cursor];
        }
    }
    return result;
}

void add_edge(vector < vector < Edge * > > & edges, int from, int to)
{
    Edge * first = new Edge(to, 1);
    Edge * second = new Edge(from, 0);
    first->rev = second;
    second->rev = first;
    edges[from].pb(first);
    edges[to].pb(second);
}

void solve()
{
    int width, height, buildings_count;
    cin >> width >> height >> buildings_count;
    vector < vector < bool > > taken(width, vector < bool > (height, false));
    for(int i = 0; i < buildings_count; i++)
    {
        int x0, y0, x1, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        if(x0 > x1)
            swap(x0, x1);
        if(y0 > y1)
            swap(y0, y1);
        for(int x = x0; x <= x1; x++)
            for(int y = y0; y <= y1; y++)
                taken[x][y] = true;
    }
    vector < vector < int > > ids(width, vector < int > (height));
    int last_id = 0;
    for(int i = 0; i < width; i++)
    {
        for(int j = 0; j < height; j++)
        {
            ids[i][j] = last_id;
            last_id += 2;
        }
    }
    int total_vertexes = 2 * width * height + 2;
    int from = total_vertexes - 2, to = total_vertexes - 1;
    vector < vector < Edge * > > edges(total_vertexes);
    for(int i = 0; i < width; i++)
    {
        for(int j = 0; j < height; j++)
        {
            if(!taken[i][j])
            {
                if(j == 0)
                    add_edge(edges, from, ids[i][j]);
                add_edge(edges, ids[i][j], ids[i][j] + 1);
                for(int k = 0; k < 4; k++)
                {
                    int ni = i + dx[k], nj = j + dy[k];
                    if(min(ni, nj) >= 0 && ni < width && nj < height && !taken[ni][nj])
                        add_edge(edges, ids[i][j] + 1, ids[ni][nj]);
                }
                if(j == height - 1)
                    add_edge(edges, ids[i][j] + 1, to);
            }
        }
    }
    int result = max_flow(total_vertexes, from, to, edges);
    if(buildings_count == 0)
        assert(result == width);
    cout << result << endl;
}

int main()
{
    int tests;
    cin >> tests;
    for(int test = 1; test <= tests; test++)
    {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}