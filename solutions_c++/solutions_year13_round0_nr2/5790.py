#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

#define NMAX 40

int grid[NMAX][NMAX];

struct node {
  int i, j;
  int dist;
  node(int i, int j, int dist) : i(i), j(j), dist(dist) { }
  bool operator<(node const& other) const {
    return dist < other.dist;
  }
};

int di[] = {1,-1,0,0};
int dj[] = {0,0,1,-1};

bool visited[NMAX][NMAX];
int getrad(int n, int sourcei, int sourcej) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      visited[i][j] = false;
    }
  }
  priority_queue<node> q;
  q.push(node(sourcei, sourcej, 11));
  int minDist = 100000;
  while (q.size() > 0) {
    node v = q.top();
    q.pop();
    if (!visited[v.i][v.j]) {
      visited[v.i][v.j] = true;
      for (int d = 0; d < 4; d++) {
        int i1 = v.i + di[d];
        int j1 = v.j + dj[d];
        if (i1 >= 0 && i1 < n && j1 >= 0 && j1 < n) {
          int dist = v.dist + grid[i1][j1] + 1;
          q.push(node(i1, j1, dist));
        }
      }
      minDist = min(minDist, v.dist);
    }
  }
  return minDist;
}

int main() {
  freopen("pogo.in","r",stdin);
  freopen("pogo.out","w",stdout);

  int n;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      char c;
      c = fgetc(stdin);
      grid[i][j] = c;
    }
  }

  int dist1 = 10000;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      int rad = getrad(n, i, j);
      dist1 = min(dist1, rad);
    }
  }

  printf("%d\n", dist1);
}
