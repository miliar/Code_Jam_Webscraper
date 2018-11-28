#include <bits/stdc++.h>

using namespace std;

class MaxFlow {
private:
  struct Edge {int to, cap, rev;};
  
  const static int INF = 1e9;
  
  vector<vector<Edge>> g;
  vector<int> level, iter;
  
  void bfs(int s) {
    fill(level.begin(), level.end(), -1);
    level[s] = 0;
    queue<int> que;
    que.push(s);
    while (!que.empty()) {
      int v = que.front();
      que.pop();
      for (const Edge& e : g[v]) {
        if (e.cap == 0 || level[e.to] >= 0) continue;
        level[e.to] = level[v] + 1;
        que.push(e.to);
      }
    }
  }
  
  int dfs(int v, int t, int f) {
    if (v == t) return f;
    for (int& i = iter[v]; i < int(g[v].size()); ++i) {
      Edge& e = g[v][i];
      if (e.cap == 0 || level[v] >= level[e.to]) continue;
      int d = dfs(e.to, t, min(f, e.cap));
      if (d == 0) continue;
      e.cap -= d;
      g[e.to][e.rev].cap += d;
      return d;
    }
    return 0;
  }
  
public:
  int next() {
    g.emplace_back(vector<Edge>());
    return g.size() - 1;
  }
  
  void add_edge(int from, int to, int cap) {
    g[from].emplace_back((Edge){to, cap, int(g[to].size())});
    g[to].emplace_back((Edge){from, 0, int(g[from].size()) - 1});
  }
  
  int run(int s, int t) {
    level = vector<int>(g.size(), 0);
    iter = vector<int>(g.size(), 0);
    int flow = 0, f;
    while (true) {
      bfs(s);
      if (level[t] < 0) return flow;
      fill(iter.begin(), iter.end(), 0);
      while ((f = dfs(s, t, INF)) > 0) flow += f;
    }
  }
};

void solve() {
  int n;
  cin >> n;
  cin.ignore();
  vector<vector<string>> v(n);
  for (int i = 0; i < n; ++i) {
    string s;
    getline(cin, s);
    stringstream ss(s);
    while (ss >> s) {
      bool found = false;
      for (string str : v[i]) if (str == s) found = true;
      if (found) continue;
      v[i].emplace_back(s);
    }
  }
  unordered_set<string> k;
  for (int i = 2; i < n; ++i) for (string s : v[i]) k.insert(s);
  int r = 0;
  unordered_set<string> kk;
  for (int i = 0; i < int(v[0].size()); ++i) {
    if (!k.count(v[0][i])) {
      if (!kk.count(v[0][i])) {
        bool found = false;
        for (string s : v[1]) if (s == v[0][i]) found = true;
        if (found) ++r;
      }
      kk.insert(v[0][i]);
      v[0][i] = v[0].back();
      v[0].pop_back();
      --i;
    }
  }
  for (int i = 0; i < int(v[1].size()); ++i) {
    if (!k.count(v[1][i])) {
      v[1][i] = v[1].back();
      v[1].pop_back();
      --i;
    }
  }
  unordered_set<string> t;
  for (string s1 : v[0]) for (string s2 : v[1]) {
    if (s1 == s2) t.insert(s1);
  }
  r += t.size();
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < (int)v[i].size(); ++j) {
      if (t.count(v[i][j])) {
        v[i][j] = v[i].back();
        v[i].pop_back();
        --j;
      }
    }
  }
  /*
  cerr << endl;
  for (int i = 0; i < n; ++i) {
    cerr << i << " :";
    for (string s : v[i]) cerr << " " << s;
    cerr << endl;
  }
  */
  unordered_set<string> ss1, ss2;
  for (string s : v[0]) ss1.insert(s);
  for (string s : v[1]) ss2.insert(s);
  MaxFlow mf;
  int source = mf.next();
  int sink = mf.next();
  map<pair<string, int>, int> mp;
  for (int i = 0; i < n; ++i) for (string s : v[i]) {
    if (!mp.count(make_pair(s, 0))) {
      mp[make_pair(s, 0)] = mf.next();
      mp[make_pair(s, 1)] = mf.next();
      mf.add_edge(mp[make_pair(s, 0)], mp[make_pair(s, 1)], 1);
    }
  }
  for (int i = 0; i < (int)v[0].size(); ++i) mf.add_edge(source, mp[make_pair(v[0][i], 0)], 1);
  for (int i = 0; i < (int)v[1].size(); ++i) mf.add_edge(mp[make_pair(v[1][i], 1)], sink, 1);
  for (int i = 2; i < n; ++i) {
    for (string s1 : v[i]) for (string s2 : v[i]) if (s1 != s2) {
      if (ss1.count(s1) && ss1.count(s2)) continue;
      if (ss2.count(s1) && ss2.count(s2)) continue;
      //cerr << s1 << " " << s2 << endl;
      mf.add_edge(mp[make_pair(s1, 1)], mp[make_pair(s2, 0)], 1);
      mf.add_edge(mp[make_pair(s2, 1)], mp[make_pair(s1, 0)], 1);
    }
  }
  cout << mf.run(source, sink) + r;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
    cout << endl;
  }
}
