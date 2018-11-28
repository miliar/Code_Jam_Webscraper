#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define image(a) {sort(all(a)), a.resize(unique(all(a)) - a.begin());}
struct pnt {
  int x, y;
  pnt() {
  }
  pnt(int _x, int _y) : x(_x), y(_y) {
  }
};
pnt operator -(pnt a, pnt b) {
  return pnt(a.x - b.x, a.y - b.y);
}
pnt operator +(pnt a, pnt b) {
  return pnt(a.x + b.x, a.y + b.y);
}
int sp(pnt a, pnt b) {
  return a.x * b.x + a.y * b.y;
}
int vp(pnt a, pnt b) {
  return a.x * b.y - a.y * b.x;
}
int n, m;
pnt p[1000];
int tp[1000];
vector<pair<int, int>> ls;
char s[1000][1000];
int go[10000];
int N, M;
int num(pnt a) {
  return a.x * M + a.y;
}
int up(int x) {
  if (x == go[x]) return x;
  return go[x] = up(go[x]);
}
void merge(int x, int y) {
  x = up(x);
  y = up(y);
  if (x != y) {
    go[x] = y;
  }
}
void merge(pnt a, pnt b) {
  merge(num(a), num(b));
}
int up(pnt a) {
  return up(num(a));
}
void solve() {
  cin >> n >> m;
  N = 2 * n + 1;
  M = 2 * m + 1;
  for (int i = 0; i < m; i++) {
    p[i] = pnt(0, i * 2 + 1);
    tp[i] = 0;
  }
  for (int i = 0; i < n; i++) {
    p[i + m] = pnt(i * 2 + 1, 2 * m);
    tp[i + m] = 1;
  }
  for (int i = 0; i < m; i++) {
    p[i + n + m] = pnt(2 * n, (m - 1 - i) * 2 + 1);
    tp[i + n + m] = 2;
  }
  for (int i = 0; i < n; i++) {
    p[i + n + m + m] = pnt((n - 1 - i) * 2 + 1, 0);
    tp[i + n + m + m] = 3;
  }
  ls.clear();
  for (int i = 0; i < n + m; i++) {
    int x, y;
    cin >> x >> y;
    x--, y--;
    ls.pb(mp(x, y));
  }
  
  for (int msk = 0; msk < (1 << (n * m)); msk++) {
    for (int i = 0; i < N * M; i++) {
      go[i] = i;
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if ((msk >> (i * m + j)) & 1) {
          s[i][j] = '/';
          merge(pnt(2 * i + 1, 2 * j), pnt(2 * i, 2 * j + 1));
          merge(pnt(2 * i + 1, 2 * j + 2), pnt(2 * i + 2, 2 * j + 1));
        } else {
          s[i][j] = '\\';
          merge(pnt(2 * i + 1, 2 * j), pnt(2 * i + 2, 2 * j + 1));
          merge(pnt(2 * i + 1, 2 * j + 2), pnt(2 * i, 2 * j + 1));
        }
      }
    }
    bool good = true;
    for (int i = 0; i < sz(ls); i++) {
      if (up(p[ls[i].x]) != up(p[ls[i].y])) {
        good = false;
      }
    }
    if (good) {
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          printf("%c", s[i][j]);
        }
        printf("\n");
      }
      return;
    }
  }
  printf("IMPOSSIBLE\n");
}

int main(){
  assert(freopen("a.out","wt",stdout));
  assert(freopen("a.in","rt",stdin));
  int T;
  scanf("%d", &T);
  for (int ti = 1; ti <= T; ti++) {
    printf("Case #%d:\n", ti);
    solve();
  }
  return 0;
}
