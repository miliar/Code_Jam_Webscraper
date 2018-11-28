#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

const int MAX_D = 4;
const int DX[MAX_D] = {-1, 0, 1, 0};
const int DY[MAX_D] = {0, 1, 0, -1};

class Edge {
  public:
    int u, v, capacity, flow;

    Edge() {}

    Edge(const int _u, const int _v, const int _capacity):
      u(_u),
      v(_v),
      capacity(_capacity),
      flow(0) {}

    bool Saturated() const {
        return capacity == flow;
    }
};

class Graph {
  public:
    static const int NIL = -1;
    static const int oo = 0x3f3f3f3f;

    int V, E;
    vector< vector<int> > G;
    vector<Edge> edges;

    Graph(const int _V = 0):
      V(_V),
      E(0),
      G(vector< vector<int> >(_V, vector<int>())),
      edges(vector<Edge>()) {}

    void AddEdge(const Edge &edge) {
        edges.push_back(edge);
        G[edge.u].push_back(E);
        ++E;
    }

    int MaximumFlow(const int source, const int sink) {
        InitializeFlowNetwork();
        vector<int> father = vector<int>(V, NIL);
        int maxFlow = 0;
        while (BFS(source, sink, father)) {
            for (const auto &e: G[sink]) {
                if (edges[NonEdge(e)].Saturated() || father[edges[e].v] == NIL)
                    continue;
                father[sink] = NonEdge(e);
                int flow = oo;
                for (int x = sink; x != source; x = edges[father[x]].u)
                    flow = min(flow, edges[father[x]].capacity - edges[father[x]].flow);
                for (int x = sink; x != source; x = edges[father[x]].u) {
                    edges[father[x]].flow += flow;
                    edges[NonEdge(father[x])].flow -= flow;
                }
                maxFlow += flow;
            }
        }
        ClearResidualNetwork();
        return maxFlow;
    }

  private:
    int NonEdge(const int edgeIndex) const {
        if (edgeIndex < E)
            return edgeIndex + E;
        return edgeIndex - E;
    }

    bool BFS(const int start, const int end, vector<int> &father) {
        for (int x = 0; x < V; ++x)
            father[x] = NIL;
        father[start] = start;
        queue<int> q;
        for (q.push(start); !q.empty(); q.pop()) {
            int x = q.front();
            if (x == end)
                continue;
            for (const auto &e: G[x]) {
                if (!edges[e].Saturated() && father[edges[e].v] == NIL) {
                    father[edges[e].v] = e;
                    q.push(edges[e].v);
                }
            }
        }
        return father[end] != NIL;
    }

    void InitializeFlowNetwork() {
        edges.resize(2 * E);
        for (int e = 0; e < E; ++e) {
            edges[e].flow = 0;
            edges[NonEdge(e)] = Edge(edges[e].v, edges[e].u, 0);
            G[edges[e].v].push_back(NonEdge(e));
        }
    }

    void ClearResidualNetwork() {
        edges.resize(E);
        for (int e = E - 1; e >= 0; --e)
            G[edges[e].v].pop_back();
    }
};

int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int testCount;
    cin >> testCount;
    for (int test = 1; test <= testCount; ++test) {
        int w, h, blocks;
        cin >> w >> h >> blocks;
        vector< vector<bool> > free = vector< vector<bool> >(w, vector<bool>(h, true));
        for (; blocks > 0; --blocks) {
            int x0, y0, x1, y1;
            cin >> x0 >> y0 >> x1 >> y1;
            for (int x = x0; x <= x1; ++x)
                for (int y = y0; y <= y1; ++y)
                    free[x][y] = false;
        }
        Graph G = Graph(2 * w * h + 2);
        for (int x = 0; x < w; ++x) {
            for (int y = 0; y < h; ++y) {
                if (!free[x][y])
                    continue;
                G.AddEdge(Edge(2 * (y * w + x), 2 * (y * w + x) + 1, 1));
                for (int d = 0; d < MAX_D; ++d) {
                    int nx = x + DX[d], ny = y + DY[d];
                    if (0 <= nx && nx < w && 0 <= ny && ny < h && free[nx][ny])
                        G.AddEdge(Edge(2 * (y * w + x) + 1, 2 * (ny * w + nx), 1));
                }
            }
        }
        for (int x = 0; x < w; ++x) {
            if (free[x][0])
                G.AddEdge(Edge(2 * w * h, 2 * (0 * w + x), 1));
            if (free[x][h - 1])
                G.AddEdge(Edge(2 * ((h - 1) * w + x) + 1, 2 * w * h + 1, 1));
        }
        cout << "Case #" << test << ": " << G.MaximumFlow(2 * w * h, 2 * w * h + 1) << "\n";
    }
    cin.close();
    cout.close();
    return 0;
}
