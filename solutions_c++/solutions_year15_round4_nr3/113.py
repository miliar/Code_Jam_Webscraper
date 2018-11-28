#include <bits/stdc++.h>
using namespace std;

struct Edge {
  int v, cap, flow;
  list<Edge>::iterator back;
  Edge(int v, int cap) : v(v), cap(cap), flow(0) {}
};

typedef vector<list<Edge>> Graph;

int64_t compute_flow(Graph& graph, int s, int t) {
  int n = graph.size();
  vector<int64_t> e(n, 0);
  vector<int> h(n, 0);
  vector<list<Edge>::iterator> cur(n);
  for (int i = 0; i < n; ++i)
    cur[i] = graph[i].begin();
  queue<int> q;
  for (Edge& edge : graph[s]) {
    edge.flow = edge.cap;
    edge.back->flow = -edge.flow;
    if (e[edge.v] == 0 && edge.v != t) q.push(edge.v);
    e[edge.v] += edge.flow;
  }
  h[s] = n;
  for(; !q.empty(); q.pop()) {
    int u = q.front();
    while (e[u] > 0) {
      if (cur[u] == graph[u].end()) {  // relabel
        h[u] = 2 * n + 1;
        for (const Edge& edge : graph[u])
          if(edge.flow < edge.cap) h[u] = min(h[u], 1 + h[edge.v]);
        cur[u] = graph[u].begin(); 
        continue; 
      }
      if (cur[u]->flow < cur[u]->cap && h[u] == h[cur[u]->v] + 1) {  // push
        int d = min(e[u], (int64_t)cur[u]->cap - cur[u]->flow);
        cur[u]->flow += d;
        cur[u]->back->flow -= d;
        e[u] -= d;
        e[cur[u]->v] += d;
        if (e[cur[u]->v] == d && cur[u]->v != t && cur[u]->v != s)
          q.push(cur[u]->v);
      } else {
        cur[u]++; 
      }
    }
  }
  return e[t];
}

void addedge(Graph& graph, int a, int b, int c) {
     graph[a].push_back(Edge(b, c));
      graph[b].push_back(Edge(a, 0));
      graph[a].back().back = --graph[b].end();
      graph[b].back().back = --graph[a].end();
 

}

int gi() {
  string temp;
  getline(cin, temp);
  istringstream iss(temp);
  int b;
  iss >> b;
  return b;
}

map<string, int> tokens;

vector<int> tokenize() {
  string temp;
  getline(cin, temp);
  istringstream iss(temp);
  string buf;
  vector<string> result;
  while (iss>>buf) {
    result.push_back(buf);
  }
  vector<int> ri;
  for (string s : result) {
    if (!tokens.count(s)) {
      int x=  tokens.size();
      tokens[s] = x;
    }
    ri.push_back(tokens[s]);
  }   
  return ri;
}

int main() {
  int Z;
  Z = gi();
  for (int z=1; z<=Z; ++z) {
    tokens.clear();
    int n=gi();
    vector<vector<int>> S(n);
    for (int i=0; i<n; ++i)
      S[i] = tokenize();
    assert(tokens.size() < 10000);
    
    Graph graph(n + 2 * tokens.size());
    for (int i = 0; i < tokens.size(); ++i)
      addedge(graph, n + i, n + tokens.size() + i, 1);
    for (int i = 0; i < n; ++i)
      for (int w : S[i]) {
        addedge(graph, i, n + w, 10000);
        addedge(graph, n + tokens.size() + w, i, 10000);
      }
    int result = compute_flow(graph, 0, 1);
    cout << "Case #" << z << ": " << result << endl;

  }
}
