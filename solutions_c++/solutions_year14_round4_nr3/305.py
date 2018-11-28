#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;

vector<int> esource, esink, ecapacity, eflow;
vector<vector<int> > adj;


#define DOLOG 0
#define LOG(...) (DOLOG ? fprintf(stderr, __VA_ARGS__) : 0)


void add_edge(int u, int v, int w) {
  int id = esource.size();
  int rid = esource.size() + 1;
  LOG("add_edge(%d, %d, %d) -> %d, %d\n", u, v, w, id, rid);

  esource.push_back(u);
  esink.push_back(v);
  ecapacity.push_back(w);
  eflow.push_back(0);

  esource.push_back(v);
  esink.push_back(u);
  ecapacity.push_back(0);
  eflow.push_back(0);

  adj[u].push_back(id);
  adj[v].push_back(rid);
}


bool find_path(int source, int sink, vector<int>& path) {
  vector<int> back(adj.size(), -1);
  queue<int> Q;
  Q.push(source);
  back[source] = -2;

  while (!Q.empty()) {
    int v = Q.front(); Q.pop();
    for (int i = 0; i < adj[v].size(); i++) {
      int e = adj[v][i];
      if (ecapacity[e] - eflow[e] <= 0) continue;
      if (back[esink[e]] != -1) continue;
      back[esink[e]] = e;
      Q.push(esink[e]);
    }
  }

  if (back[sink] == -1) return false;

  int v = sink;
  while (v != source) {
    path.push_back(back[v]);
    v = esource[back[v]];
  }
  reverse(path.begin(), path.end());
  return true;


#if 0
  if (source == sink) return true;
  for (int i = 0; i < adj[source].size(); i++) {
    int e = adj[source][i];
    int residual = ecapacity[e] - eflow[e];
    if (residual > 0 && !count(path.begin(), path.end(), e)) {
      int s = path.size();
      path.push_back(e);
      if (find_path(esink[e], sink, path)) return true;
      path.resize(s);
    }
  }
  return false;
#endif
}


int max_flow(int source, int sink) {
  vector<int> path;
  while (true) {
    path.clear();
    if (!find_path(source, sink, path)) break;
    LOG("path:");
    int myflow = 123456789;
    for (int i = 0; i < path.size(); i++) {
      int e = path[i];
      LOG(" %d->%d:%d", esource[e], esink[e], ecapacity[e]);
      myflow = min(myflow, ecapacity[e] - eflow[e]);
    }
    LOG(" (myflow %d)\n", myflow);
    for (int i = 0; i < path.size(); i++) {
      eflow[path[i]] += myflow;
      eflow[path[i] ^ 1] -= myflow;
    }
  }
  int total = 0;
  for (int i = 0; i < adj[source].size(); i++) {
    total += eflow[adj[source][i]];
  }
  return total;
}


#define FREE(y, x) ((y) >= 0 && (x) >= 0 && (y) < H && (x) < W && nmap[y].second[x])


int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    printf("Case #%d: ", tc);

    int W, H;
    int b;
    scanf("%d%d%d", &W, &H, &b);

    vector<vector<bool> > map(H, vector<bool>(W, true));

    for (int i = 0; i < b; i++) {
      int x0, y0, x1, y1;
      scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
      for (int y = y0; y <= y1; y++) for (int x = x0; x <= x1; x++) map[y][x] = false;
    }

    vector<pair<int,vector<bool> > > nmap;

    for (int y = 0; y < H; y++) {
      if (y && map[y] == map[y-1] && false) {   // COMPRESSION WIP
        nmap.rbegin()->first++;
      } else {
        nmap.push_back(make_pair(1, map[y]));
      }
    }

//    fprintf(stderr, "%d\n", (int)nmap.size());

    H = nmap.size();
    int source = W*H*2;
    int sink = W*H*2 + 1;
    int V = W*H*2 + 2;

    esource.clear();
    esink.clear();
    ecapacity.clear();
    eflow.clear();
    adj.clear();
    adj.resize(V);

    LOG("----------------------------------------\n");

    for (int y = 0; y < H; y++) {
      for (int x = 0; x < W; x++) {
        if (!FREE(y, x)) continue;
        add_edge((y*W+x)*2, (y*W+x)*2+1, nmap[y].first);
        if (FREE(y+1, x)) add_edge((y*W+x)*2+1, ((y+1)*W+(x))*2, 1);
        if (FREE(y-1, x)) add_edge((y*W+x)*2+1, ((y-1)*W+(x))*2, 1);
        if (FREE(y, x+1)) add_edge((y*W+x)*2+1, ((y)*W+(x+1))*2, nmap[y].first);
        if (FREE(y, x-1)) add_edge((y*W+x)*2+1, ((y)*W+(x-1))*2, nmap[y].first);
      }
    }
    for (int x = 0; x < W; x++) {
      add_edge(source, x*2, 1);
      add_edge(((H-1)*W+(x))*2+1, sink, 1);
    }

    int R = max_flow(source, sink);
    printf("%d\n", R);
    fflush(stdout);
  }
}
