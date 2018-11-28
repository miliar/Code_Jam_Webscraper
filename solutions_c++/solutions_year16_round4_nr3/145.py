#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 20;
const int MAX_BIG_N = 4 * MAX_N * MAX_N;

void print_answer(int case_id, int n, int m, char garden[MAX_N][MAX_N]) {
  printf("Case #%d:\n", case_id);
  for (int i = 0; i < n; i++) {
    garden[i][m] = '\0';

    // reverse(garden[i], garden[i] + m);

    printf("%s\n", garden[i]);
  }
}

void print_impossible(int case_id) {
  printf("Case #%d:\nIMPOSSIBLE\n", case_id);
}

int bounded[MAX_BIG_N];
int entry_points[MAX_BIG_N];

char garden[MAX_N][MAX_N];

int N;
vector<int> adjacent_nodes[MAX_BIG_N];
int component_ids[MAX_BIG_N];

void build_entry_points(int n, int m) {
  for (int j = 0; j < m; j++) {
    int v = 4 * j;

    entry_points[j] = v;
  }

  for (int i = 0; i < n; i++) {
    int v = 4 * (i * m + (m - 1)) + 3;

    entry_points[m + i] = v;
  }

  for (int j = 0; j < m; j++) {
    int v = 4 * ((n - 1) * m + m - j - 1) + 2;

    entry_points[m + n + j] = v;
  }

  for (int i = 0; i < n; i++) {
    int v = 4 * ((n - i - 1) * m) + 1;

    entry_points[m + n + m + i] = v;
  }
}

void add_edge(int u, int v) {
  // cerr << u << " <-> " << v << "\n";
  adjacent_nodes[u].push_back(v);
  adjacent_nodes[v].push_back(u);
}

void build_graph(int n, int m, char garden[MAX_N][MAX_N]) {
  N = 4 * n * m;
  for (int i = 0; i < N; i++) {
    adjacent_nodes[i].clear();
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      int v = 4 * (i * m + j);

      if (garden[i][j] == '\\') {
        add_edge(v, v + 3);
        add_edge(v + 1, v + 2);
      } else {
        add_edge(v, v + 1);
        add_edge(v + 2, v + 3);
      }

      if (i + 1 < n) {
        int u = 4 * ((i + 1) * m + j);

        add_edge(v + 2, u);
      }

      if (j + 1 < m) {
        int u = 4 * (i * m + (j + 1));

        add_edge(v + 3, u + 1);
      }
    }
  }
}

void dfs(int v, int component_id) {
  component_ids[v] = component_id;

  for (int u : adjacent_nodes[v]) {
    if (component_ids[u] == -1) {
      dfs(u, component_id);
    }
  }
}

void solve(int case_id) {
  int n, m; cin >> n >> m;

  for (int i = 0; i < 2 * (n + m); i++) {
    cin >> bounded[i];
    bounded[i] -= 1;
  }

  build_entry_points(n, m);
  
  for (int mask = 0; mask < (1 << (n * m)); mask++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        int k = i * m + j;
        int b = (mask >> k) & 1;

        if (b) {
          garden[i][j] = '\\';
        } else {
          garden[i][j] = '/';
        }
      }
    }

    // cout << "Trying the following garden:\n";
    // for (int i = 0; i < n; i++) {
    //   garden[i][m] = '\0';
    //   printf("%s\n", garden[i]);
    // }

    // cout << "-----------------\n";

    build_graph(n, m, garden);
    memset(component_ids, -1, sizeof(component_ids));

    for (int v = 0; v < N; v++) {
      if (component_ids[v] != -1) {
        continue;
      }

      dfs(v, v);
    }

    bool flag = true;
    for (int i = 0; i < 2 * (n + m); i += 2) {
      int v = entry_points[bounded[i]];
      int u = entry_points[bounded[i + 1]];
      if (component_ids[u] != component_ids[v]) {
        flag = false;
      }
    } 

    if (flag) {
      print_answer(case_id, n, m, garden);
      return;
    }
  }

  print_impossible(case_id);
}

int main() {
  int cases; cin >> cases;

  for (int i = 1; i <= cases; i++) {
    solve(i);
  }

  return 0;
}