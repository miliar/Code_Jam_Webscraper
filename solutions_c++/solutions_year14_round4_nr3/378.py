#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

struct edge{
  int dest, c;
  edge *rev;
  edge (int _dest = 0, int _c = 0) : dest(_dest), c(_c) {}
};

const int MAXN = 505*205*2 + 5;
vector <edge> E[MAXN];

int source = MAXN-2;
int sink = MAXN-1;
int w, h, b;
int bio[MAXN];
bool ok[1005][1005];

int in(int x, int y){
  return 2 * (x * w + y);
}

int out (int x, int y){
  return 1 + in(x, y);
}

void add_edge (int x, int y){
  E[x].push_back(edge(y, 1));
  E[y].push_back(edge(x, 0));
  E[x].back().rev = &E[y].back();
  E[y].back().rev = &E[x].back();
}

int dfs (int x){
  if (x == sink) return 1;
  if (bio[x]) return 0;

  bio[x] = 1;

  for (int i = 0; i < E[x].size(); ++i){
    if (E[x][i].c && dfs(E[x][i].dest)){
      E[x][i].c -= 1;
      E[x][i].rev->c += 1;
      return 1;
    }
  }

  return 0;
}

int dx[] = { 0, 1, -1, 0 };
int dy[] = { 1, 0, 0, -1 };

void solve (){
  scanf("%d%d%d", &w, &h, &b);
  memset(ok, 1, sizeof ok);
  for (int i = 0; i < MAXN; ++i){
    E[i].clear();
    E[i].reserve(20);
  }

  for (int i = 0; i < b; ++i){
    int x0, y0, x1, y1;
    scanf("%d%d%d%d", &x0, &y0, &x1, &y1);

    swap(x0, y0);
    swap(x1, y1);

    x0 = h - x0 - 1;
    x1 = h - x1 - 1;

    if (x0 > x1) swap(x0, x1);

    for (int x = x0; x <= x1; ++x)
      for (int y = y0; y <= y1; ++y)
	ok[x][y] = 0;
  }

  for (int i = 0; i < h; ++i)
    for (int j = 0; j < w; ++j){
      add_edge(in(i, j), out(i, j));

      for (int k = 0; k < 4; ++k){
	int nx, ny;
	nx = i + dx[k];
	ny = j + dy[k];
	if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
	if (ok[nx][ny] == 0) continue;
	add_edge(out(i, j), in(nx, ny));
      }
    }


  for (int i = 0; i < w; ++i)
    if (ok[0][i]) add_edge(out(0, i), sink);

  for (int i = 0; i < w; ++i)
    if (ok[h-1][i]) add_edge(source, in(h-1, i));

  int ans = 0;
  memset(bio, 0, sizeof bio);

  while (dfs(source)){
    ++ans;
    memset(bio, 0, sizeof bio);
  }

  printf("%d\n", ans);
}

int main (void){
  int tc; scanf ("%d", &tc);
  for (int i = 1; i <= tc; ++i){
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}


