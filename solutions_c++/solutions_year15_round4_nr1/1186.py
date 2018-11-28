#include <bits/stdc++.h>

using namespace std;

const int N = 123;
int r, c;
char g[N][N];
int was[N][N];
int nexti[N][N];
int nextj[N][N];

char dc[] = "><v^";
int di[] = {0, 0, 1, -1};
int dj[] = {1, -1, 0, 0};

int p[N * N], size[N * N];
bool finish[N * N];

int get(int i, int j) {
  return i * c + j;
}

int find(int x) {
  return p[x] == x ? x : p[x] = find(p[x]);
}

void join(int x, int y) {
  x = find(x); y = find(y);
  if(x != y) {
    if(size[x] < size[y]) {
      p[x] = y; size[y] += size[x];
    }else {
      p[y] = x; size[x] += size[y];
    }
  }
}

bool inside(int i, int j) {
  return i >= 0 && i < r && j >= 0 && j < c;
}

bool dfs(int i, int j) {
  if(was[i][j]) {
    return was[i][j] == 1;
  }
  was[i][j] = 1;
  if(nexti[i][j] != -1 && nextj[i][j] != -1) {
    if(dfs(nexti[i][j], nextj[i][j])) {
      return true;
    }
  }
  was[i][j] = 2;
  return false;
}

bool cycle(int id) {
  for(int i = 0; i < r; ++i) {
    for(int j = 0; j < c; ++j) {
      if(find(get(i, j)) == id) {
        if(dfs(i, j)) {
          return true;
        }
      }
    }
  }
  return false;
}

int main() {
  freopen("A.in", "rt", stdin);
  freopen("A.out", "wt", stdout);
  int t; scanf("%d", &t);
  for(int test = 1; test <= t; ++test) {
    printf("Case #%d: ", test);
    scanf("%d %d", &r, &c);
    for(int i = 0; i < r; ++i) {
      scanf("%s", g[i]);
      for(int j = 0; j < c; ++j) {
        if(g[i][j] != '.') {
          int id = get(i, j);
          p[id] = id;
          size[id] = 1;
        }
      }
    }
    memset(nexti, -1, sizeof nexti);
    memset(nextj, -1, sizeof nextj);
    for(int i = 0; i < r; ++i) {
      for(int j = 0; j < c; ++j) {
        if(g[i][j] == '.') continue;
        int k = strchr(dc, g[i][j]) - dc;
        int ii = i + di[k], jj = j + dj[k];
        while(inside(ii, jj) && g[ii][jj] == '.') {
          ii += di[k];
          jj += dj[k];
        }
        if(inside(ii, jj)) {
          nexti[i][j] = ii;
          nextj[i][j] = jj;
          join(get(i, j), get(ii, jj));
        }
      }
    }
    map<int, int> comp;
    for(int i = 0; i < r; ++i) {
      for(int j = 0; j < c; ++j) {
        if(g[i][j] != '.') {
          int p = find(get(i, j));
          comp[p] = size[p];
        }
      }
    }
    memset(finish, 0, sizeof finish);
    memset(was, 0, sizeof was);
    int ans = 0;
    vector<int> ones;
    for(auto cm : comp) {
      if(cm.second == 1) {
        ones.push_back(cm.first);
        continue;
      }
      ans += !cycle(cm.first);
      finish[cm.first] = 1;
    }
    bool done = false;
    while(!done) {
      done = true;
      for(int p = 0; p < (int)ones.size(); ++p) {
        int i = ones[p] / c;
        int j = ones[p] % c;
        int canReach = 0;
        bool remove = false;
        for(int k = 0; k < 4; ++k) {
          int ii = i + di[k];
          int jj = j + dj[k];
          while(inside(ii, jj) && g[ii][jj] == '.') {
            ii += di[k];
            jj += dj[k];
          }
          if(inside(ii, jj)) {
            canReach++;
            if(finish[find(get(i, j))]) {
              remove = true;
              break;
            }
          }
        }
        if(remove) {
          ans++;
          ones.erase(ones.begin() + p);
          --p;
        }else if(canReach == 0) {
          ans = -1;
          done = true;
          break;
        }
      }
    }
    if(ans == -1) puts("IMPOSSIBLE");
    else printf("%d\n", ans + (int)ones.size());
  }
  return 0;
}
