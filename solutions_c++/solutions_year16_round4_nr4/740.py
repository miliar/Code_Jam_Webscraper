#include <bits/stdc++.h>

using namespace std;

const int N = 30;

int n;
char s[N][N];
int fa[N];
bool vis[N];
int belong[N];
int anssum;

void init() {
  for (int i = 0; i < N; ++i) {
    fa[i] = i;
  }
}

int find(int x) {
  return fa[x] == x ? x : (fa[x] = find(fa[x]));
}

void mrg(int x, int y) {
  x = find(x);
  y = find(y);
  if (x != y) {
    fa[x] = y;
  }
}

bool check() {
  vector<int> v[N];
  for (int i = 1; i <= n; ++i) {
    v[belong[i]].push_back(i);
  }
  for (int i = 1; i <= n; ++i) {
    for (int j = i + 1; j <= n; ++j) {
      if (belong[i] != belong[j] && find(i) == find(j)) {
        return 0;
      }
    }
  }
  int a[N][N];
  memset(a, 0, sizeof(a));
  for (int i = 1; i <= n; ++i) {
    set<int> st;
    for (int j : v[i]) {
      for (int k = 1; k <= n; ++k) {
        if (s[j][k] == '1') {
          st.insert(k);
        }
      } 
    }
    if (st.size() > v[i].size()) return 0;
  }
  int tmp = 0;
  for (int i = 1; i <= n; ++i) {
    tmp += v[i].size() * v[i].size();
  }
  anssum = min(anssum, tmp);
  return 1;
}

void dfs(int ps) {
  if (ps == n + 1) {
    check(); 
    return;
  }
  for (int i = 1; i <= n; ++i) {
    belong[ps] = i;
    dfs(ps + 1);
  }
}


int main() {
  int t;
  scanf("%d", &t);
  for (int _ = 1; _ <= t; ++_) {
    scanf("%d", &n);
    init();
    anssum = n * n;
    for (int i = 1; i <= n; ++i) {
      scanf("%s", s[i] + 1);
    }
    for (int i = 1; i <= n; ++i) {
      for (int j = i + 1; j <= n; ++j) {
        for (int k = 1; k <= n; ++k) {
          if (s[i][k] == '1' && s[j][k] == '1') {
            mrg(i, j);
            break;
          }
        }
      }
    }
    dfs(1);
    int cc = 0;
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        cc += (s[i][j] == '1');
      }
    }
    printf("Case #%d: %d\n", _, anssum - cc);
    /*
    memset(vis, 0, sizeof(vis));
    vector<int> v;
    for (int i = 1; i <= n; ++i) {
      if (!vis[i]) {
        int c = 1;
        for (int j = i + 1; j <= n; ++j) {
          if (find(i) == find(j)) {
            c++;
          }
        }
        v.push_back(c);
      }
    }
    int tt = 0;
    for (auto i : v) {
      tt += i;
    }
    tt = n - tt;
    int sum = 0;
    for (auto i : v) {
      sum += i * i;
    }
    int cc = 0;
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        cc += (s[i][j] == '1');
      }
    }
    printf("%d\n", sum + tt - cc);*/
  }
  return 0;
}
