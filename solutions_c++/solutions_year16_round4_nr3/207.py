#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")

#include <bits/stdc++.h>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = int64_t;

const int N = 16;
const int TOTAL = 3 * 3 * N * N;

vector<int> g[TOTAL];
bool used[TOTAL];
int cmps[TOTAL];

void dfs(int u, int j) {
  cmps[u] = j;
  used[u] = true;
  for (int v : g[u]) {
    if (!used[v])
      dfs(v, j);
  }
}

void clear() {
  for (int i = 0; i < TOTAL; i++) {
    g[i].clear();
    used[i] = false;
    cmps[i] = i;
  }
}

void connect_first(int n, int m, int x, int y) {
  {
    int a = (2 * m + 1) * 2 * x + 2 * y + 1;
    int b = (2 * m + 1) * (2 * x + 1) + 2 * y;
    g[a].pb(b);
    g[b].pb(a);
  }
  {
    int a = (2 * m + 1) * (2 * x + 1) + 2 * y + 2;
    int b = (2 * m + 1) * (2 * x + 2) + 2 * y + 1;
    g[a].pb(b);
    g[b].pb(a);
  }
}

void connect_second(int n, int m, int x, int y) {
  {
    int a = (2 * m + 1) * 2 * x + 2 * y + 1;
    int b = (2 * m + 1) * (2 * x + 1) + 2 * y + 2;
    g[a].pb(b);
    g[b].pb(a);
  }
  {
    int a =  (2 * m + 1) * (2 * x + 1) + 2 * y;
    int b =  (2 * m + 1) * (2 * x + 2) + 2 * y + 1;
    g[a].pb(b);
    g[b].pb(a);
  }
}

void solve() {
  int n, m;
  cin >> n >> m;

  vector<int> lovers(m + m + n + n);
  for (int i = 0; i < lovers.size(); i++) {
    cin >> lovers[i];
    --lovers[i];
  }


  for (int mask = 0; mask < (1 << (n * m)); mask++) {
    clear();
    int id = 0;
    for (int x = 0; x < n; x++) {
      for (int y = 0; y < m; y++) {
        bool flag = (mask >> id) & 1;
        ++id;

        if (flag) {
          connect_first(n, m, x, y);
        } else {
          connect_second(n, m, x, y);
        }
      }
    }

    vector<int> order;

    for (int i = 0; i < m; i++) {
      order.pb(2 * i + 1);
    }
    for (int i = 0; i < n; i++) {
      order.pb((2 * m + 1) * (2 * i + 2) - 1);
    }
    for (int i = m - 1; i >= 0; i--) {
      order.pb((2 * n) * (2 * m + 1) + 1 + 2 * i);
    }
    for (int i = n - 1; i >= 0; i--) {
      order.pb((2 * m + 1) * (2 * i + 1));
    }

    assert(order.size() == lovers.size());

    for (int i = 0, j = 0; i < TOTAL; i++) {
      if (!used[i]) {
        dfs(i, j++);
      }
    }

    //cout << "SOLVE" << endl;
    //for (int i = 0; i < 9; i++) {
    //  cout << "CMP: " << cmps[i] << endl;
    //}
    //for (int i : order) {
    //  cout << i << " ";
    //}
   // cout << endl;

    bool fail = false;

    for (int i = 0; i < lovers.size(); i += 2) {
      int a = lovers[i], b = lovers[i + 1];
      if (cmps[order[a]] != cmps[order[b]]) {
        //cerr << "BAD" << endl;
        fail = true;
      }
      for (int j = 0; j < lovers.size(); j++) {
        if (j != a && j != b) {
          if (cmps[order[j]] == cmps[order[a]] || cmps[order[j]] == cmps[order[b]]) {
            //cerr << "BAD2" << endl;
            fail = true;
          }
        }
      }
    }

    if (!fail) {
      id = 0;
      for (int x = 0; x < n; x++) {
        for (int y = 0; y < m; y++) {
          bool flag = (mask >> id) & 1;
          ++id;

          if (flag) {
            cout << "/";
          } else {
            cout << "\\";
          }
        }
        cout << endl;
      }
      return;
    }
  }

  cout << "IMPOSSIBLE" << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;

  for (int test = 1; test <= tests; test++) {
    cout << "Case #" << test << ":";
    cout << endl;
    solve();
  }

  return 0;
}
