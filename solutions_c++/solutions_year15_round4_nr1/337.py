#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <tuple>

using namespace std;

typedef long long int64;

class Edge {
 public:
  int u, v, capacity, cost, flow;

  Edge() {}

  Edge(const int _u, const int _v, const int _capacity, const int _cost):
   u(_u),
   v(_v),
   capacity(_capacity),
   cost(_cost),
   flow(0) {}

  bool saturated() const {
    return capacity == flow;
  }
};

class Graph {
 public:
  static const int NIL = -1;
  static const int oo = 0x3f3f3f3f;

  Graph(const int _V = 0):
   V(_V),
   E(0),
   G(vector< vector<int> >(_V, vector<int>())),
   edges(vector<Edge>()) {}

  void addEdge(const Edge &edge) {
    edges.push_back(edge);
    G[edge.u].push_back(E);
    ++E;
  }

  tuple<int, int> maximumFlow(const int source, const int sink) {
    initializeFlowNetwork();
    vector<int> father = vector<int>(V, NIL), distance = vector<int>(V, oo);
    int maxFlow = 0, minCost = 0;
    while (BellmanFord(source, sink, father, distance)) {
      int flow = oo;
      for (int x = sink; x != source; x = edges[father[x]].u)
        flow = min(flow, edges[father[x]].capacity - edges[father[x]].flow);
      for (int x = sink; x != source; x = edges[father[x]].u) {
        edges[father[x]].flow += flow;
        edges[nonEdge(father[x])].flow -= flow;
      }
      maxFlow += flow;
      minCost += distance[sink] * flow;
    }
    clearResidualNetwork();
    return tie(maxFlow, minCost);
  }

 private:
  int V, E;
  vector< vector<int> > G;
  vector<Edge> edges;

  int nonEdge(const int edgeIndex) const {
    if (edgeIndex < E)
      return edgeIndex + E;
    return edgeIndex - E;
  }

  bool BellmanFord(const int start, const int end, vector<int> &father, vector<int> &distance) {
    for (int x = 0; x < V; ++x) {
      father[x] = NIL;
      distance[x] = oo;
    }
    father[start] = start;
    distance[start] = 0;
    queue<int> q;
    vector<bool> inQ = vector<bool>(V, false);
    q.push(start);
    inQ[start] = true;
    for (q.push(start); !q.empty(); q.pop()) {
      int x = q.front();
      inQ[x] = false;
      if (x == end)
        continue;
      for (const auto &e: G[x]) {
        if (!edges[e].saturated() && distance[edges[e].u] + edges[e].cost < distance[edges[e].v]) {
          father[edges[e].v] = e;
          distance[edges[e].v] = distance[edges[e].u] + edges[e].cost;
          if (!inQ[edges[e].v]) {
            q.push(edges[e].v);
            inQ[edges[e].v] = true;
          }
        }
      }
    }
    return father[end] != NIL;
  }

  void initializeFlowNetwork() {
    edges.resize(2 * E);
    for (int e = 0; e < E; ++e) {
      edges[e].flow = 0;
      edges[nonEdge(e)] = Edge(edges[e].v, edges[e].u, -edges[e].cost, 0);
      G[edges[e].v].push_back(nonEdge(e));
    }
  }

  void clearResidualNetwork() {
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
  for (int t = 1; t <= testCount; ++t) {
    int rows, columns;
    cin >> rows >> columns;
    vector<string> board = vector<string>(rows, "");
    for (int x = 0; x < rows; ++x)
      cin >> board[x];
    vector< vector<int> > index(rows, vector<int>(columns, Graph::NIL));
    vector<int> firstRow(rows, Graph::NIL), firstColumn(columns, Graph::NIL);
    vector<int> lastRow(rows, Graph::NIL), lastColumn(columns, Graph::NIL);
    int vertexCount = 0;
    for (int x = 0; x < rows; ++x) {
      for (int y = 0; y < columns; ++y) {
        if (board[x][y] != '.') {
          index[x][y] = vertexCount++;
          if (firstRow[x] == Graph::NIL)
            firstRow[x] = index[x][y];
          lastRow[x] = index[x][y];
          if (firstColumn[y] == Graph::NIL)
            firstColumn[y] = index[x][y];
          lastColumn[y] = index[x][y];
        }
      }
    }
    string directions = "^>v<";
    Graph graph = Graph(vertexCount + 6);
    int source = vertexCount + 4, sink = vertexCount + 5;
    int solved = 0;
    for (int x = 0; x < rows; ++x) {
      for (int y = 0; y < columns; ++y) {
        if (index[x][y] == Graph::NIL)
          continue;
        if (index[x][y] != firstColumn[y] && index[x][y] != lastRow[x] && index[x][y] != lastColumn[y] && index[x][y] != firstRow[x]) {
          ++solved;
          continue;
        }
        graph.addEdge(Edge(source, index[x][y], 1, 0));
        for (int d = 0; d < 4; ++d) {
          if (d == 0 && index[x][y] == firstColumn[y])
            continue;
          if (d == 1 && index[x][y] == lastRow[x])
            continue;
          if (d == 2 && index[x][y] == lastColumn[y])
            continue;
          if (d == 3 && index[x][y] == firstRow[x])
            continue;
          int cost = 1;
          if (board[x][y] == directions[d])
            cost = 0;
          graph.addEdge(Edge(index[x][y], vertexCount + d, 1, cost));
        }
      }
    }
    for (int d = 0; d < 4; ++d)
      graph.addEdge(Edge(vertexCount + d, sink, Graph::oo, 0));
    int maxFlow, minCost;
    tie(maxFlow, minCost) = graph.maximumFlow(source, sink);
    cout << "Case #" << t << ": ";
    if (maxFlow < vertexCount - solved)
      cout << "IMPOSSIBLE\n";
    else
      cout << minCost << "\n";
  }
  cin.close();
  cout.close();
  return 0;
}
