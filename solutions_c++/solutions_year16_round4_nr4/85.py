/* Written by Filip Hlasek 2016 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

class BipartiteGraph {
  private:
    vector<int> partity1, partity2; // Original indexes
    map<int, int> new_index1, new_index2; // Mapping to new indexes
    vector< vector<int> > graph1, graph2; // Lists of neighbours

    // Tries to match a vertex v from the first partity with some
    // vertex from the other partity.
    bool match(int v);
    vector<int> matched1, matched2; // Some auxiliary variables
    vector<bool> visited1, visited2;

  public:
    void add_edge(int index1, int index2);
    void add_vertex1(int index);
    void add_vertex2(int index);

    // Returns a list of edges in the matching
    vector<pair<int, int> > maximum_matching();

    // Returns a list of pairs (original index, partity), where partity is 1 or 2
    vector<pair<int, int> > maximum_independent_set();
    vector<pair<int, int> > minimum_vertex_cover();
};

void BipartiteGraph::add_edge(int index1, int index2) {
  add_vertex1(index1);
  add_vertex2(index2);
  int i1 = new_index1[index1], i2 = new_index2[index2];
  graph1[i1].push_back(i2);
  graph2[i2].push_back(i1);
}

void BipartiteGraph::add_vertex1(int index) {
   // if a vertex with that index is already in the graph, don't add it again
  if (new_index1.find(index) != new_index1.end()) return;

  new_index1[index] = (int)partity1.size();
  partity1.push_back(index);
  graph1.push_back(vector<int>());
}

void BipartiteGraph::add_vertex2(int index) {
   // if a vertex with that index is already in the graph, don't add it again
  if (new_index2.find(index) != new_index2.end()) return;

  new_index2[index] = (int)partity2.size();
  partity2.push_back(index);
  graph2.push_back(vector<int>());
}

bool BipartiteGraph::match(int v) {
  visited1[v] = true;
  REP(i, graph1[v].size()) {
    int w = graph1[v][i];
    if (matched2[w] == -1 || (!visited1[matched2[w]] && match(matched2[w]))) {
      matched1[v] = w;
      matched2[w] = v;
      return true;
    }
  }
  return false;
}

vector<pair<int, int> > BipartiteGraph::maximum_matching() {
  matched1.clear(); matched2.clear();
  visited1.clear(); visited2.clear();
  REP(i, partity1.size()) {
    matched1.push_back(-1);
    visited1.push_back(false);
  }
  REP(i, partity2.size()) {
    matched2.push_back(-1); // not matched yet
    visited2.push_back(false);
  }
  REP(i, partity1.size()) {
    REP(j, partity1.size()) visited1[j] = false;
    match(i);
  }
  vector< pair<int, int> > result;
  REP(i, partity1.size()) if (matched1[i] != -1) {
    result.push_back(make_pair(partity1[i], partity2[matched1[i]]));
  }
  return result;
}

vector< pair<int, int> > BipartiteGraph::maximum_independent_set() {
  maximum_matching(); // precalculate matched1 and matched2

  // It represents whether the vertex is a member of the independent set
  REP(i, partity1.size()) visited1[i] = false;
  REP(i, partity2.size()) visited2[i] = true;

  vector< pair<int, int> > result;
  REP(i, partity1.size()) if (matched1[i] == -1) {
    // Seach the graph for every unmatched vertex from the first partity
    queue<int> q;
    q.push(i);
    while (!q.empty()) {
      int v = q.front(); q.pop();
      result.push_back(make_pair(partity1[v], 1));
      visited1[v] = true;
      REP(i, graph1[v].size()) {
        int w = graph1[v][i];
        if (!visited2[w]) continue;
        visited2[w] = false;
        q.push(matched2[w]);
      }
    }
  }
  REP(i, partity2.size()) if (visited2[i]) {
    result.push_back(make_pair(partity2[i], 2));
  }

  return result;
}

// Complement of maximum independent set
vector< pair<int, int> > BipartiteGraph::minimum_vertex_cover() {
  maximum_independent_set(); // Initialize visited1 and visited2
  vector< pair<int, int> > result;
  REP(i, partity1.size()) if (!visited1[i]) {
    result.push_back(make_pair(partity1[i], 1));
  }
  REP(i, partity2.size()) if (!visited2[i]) {
    result.push_back(make_pair(partity2[i], 2));
  }
  return result;
}

/*****************************************************************************/
/************************** Prewritten code ends here ************************/
/*****************************************************************************/

#define MAXN 33
int N;

bool is_ok(vector<int> e, int index) {
  vector<int> machines;
  REP(i, N) if (e[index] & (1 << i)) machines.push_back(i);
  BipartiteGraph bg;
  REP(j, N) if (j != index) REP(m, machines.size()) if (e[j] & (1 << machines[m])) {
    bg.add_edge(j, m);
  }
  int m = bg.maximum_matching().size();
  /*
  REP(i, N) {
    REP(j, N) {
      if (e[i] & (1 << j)) printf("1");
      else printf("0");
    }
    printf("\n");
  }
  printf("index: %d matching: %d\n", index, m);
  */
  return m < machines.size();
}

map<vector<int>, int> dp;

int solve(vector<int> e) {
  if (dp.count(e)) return dp[e];
  REP(i, e.size()) if (!is_ok(e, i)) {
    int ans = MAXN * MAXN;
    REP(j, N) if (!(e[i] & (1 << j))) {
      e[i] ^= (1 << j);
      ans = min(ans, 1 + solve(e));
      e[i] ^= (1 << j);
    }
    return dp[e] = ans;
  }
  return 0;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(testcase, 1, T) {
    scanf("%d", &N);
    vector<int> e;
    REP(i, N) {
      int mask = 0;
      char skill[MAXN];
      scanf("%s", skill);
      REP(j, N) mask = 2 * mask + (skill[j] == '1');
      e.push_back(mask);
    }
    int ans = solve(e);
    printf("Case #%d: %d\n", testcase, ans);
  }
  return 0;
}
