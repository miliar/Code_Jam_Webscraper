#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

class Edge
{
public:
    int to, cap, rev;
    Edge(){};
    Edge(int to0, int cap0){to = to0; cap = cap0;}
    Edge(int to0, int cap0, int rev0){to = to0; cap = cap0; rev = rev0;}
};

int maxFlow(const vector<vector<Edge> >& edges0, int source, int sink)
{
    static vector<vector<Edge> > edges;
    static vector<bool> used;

    class Func{
    public:
        static int dfs(int s, int t, int f){
            if(s == t)
                return f;
            used[s] = true;
            for(unsigned i=0; i<edges[s].size(); ++i){
                Edge& e = edges[s][i];
                if(!used[e.to] && e.cap > 0){
                    int g = dfs(e.to, t, min(f, e.cap));
                    if(g > 0){
                        e.cap -= g;
                        edges[e.to][e.rev].cap += g;
                        return g;
                    }
                }
            }
            return 0;
        }
    };

    int n = edges0.size();
    edges.assign(n, vector<Edge>());
    for(int i=0; i<n; ++i){
        for(unsigned j=0; j<edges0[i].size(); ++j){
            const Edge& e = edges0[i][j];
            edges[i].push_back(Edge(e.to, e.cap, edges[e.to].size()));
            edges[e.to].push_back(Edge(i, 0, edges[i].size()-1));
        }
    }

    int ret = 0;
    for(;;){
        used.assign(n, false);
        int f = Func::dfs(source, sink, INT_MAX);
        if(f == 0)
            return ret;
        ret += f;
    }
}

int dy[] = {0, 0, 1, -1};
int dx[] = {-1, 1, 0, 0};

int solve()
{
    int w, h, b;
    cin >> w >> h >> b;

    vector<vector<bool> > building(h, vector<bool>(w, false));
    for(int i=0; i<b; ++i){
        int x0, y0, x1, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        for(int x=x0; x<=x1; ++x){
            for(int y=y0; y<=y1; ++y){
                building[y][x] = true;
            }
        }
    }

    vector<vector<Edge> > edges(h*w*2+2);
    int source = h * w * 2;
    int sink = h * w * 2 + 1;
    for(int x=0; x<w; ++x){
        edges[source].push_back(Edge(x*2, 1));
        edges[((h-1)*w+x)*2+1].push_back(Edge(sink, 1));
    }
    for(int y=0; y<h; ++y){
        for(int x=0; x<w; ++x){
            if(!building[y][x]){
                int i = y * w + x;
                edges[i*2].push_back(Edge(i*2+1, 1));
            }
        }
    }

    for(int y=0; y<h; ++y){
        for(int x=0; x<w; ++x){
            for(int i=0; i<4; ++i){
                int y2 = y + dy[i];
                int x2 = x + dx[i];
                if(0 <= y2 && y2 < h && 0 <= x2 && x2 < w){
                    int j = y * w + x;
                    int k = y2 * w + x2;
                    edges[j*2+1].push_back(Edge(k*2, 1));
                }
            }
        }
    }

    return maxFlow(edges, h*w*2, h*w*2+1);
}

int main()
{
    int T;
    cin >> T;

    for(int tc=1; tc<=T; ++tc){
        int ret = solve();
        cout << "Case #" << tc << ": " << ret << endl;
    }

    return 0;
}