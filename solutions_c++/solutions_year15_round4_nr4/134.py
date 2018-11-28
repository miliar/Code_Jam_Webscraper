#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
typedef vector<int> vi;


#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define x first
#define y second
#define y1 y1_gdssdfjsdgf
#define y0 y0_fsdjfsdogfs
#define ws ws_fdfsdfsdgfs
#define image(a) {sort(all(a)),a.resize(unique(all(a))-a.begin());}
#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
#define problem_name "a"
int n, m;
int a[10][10];
const int dx[] = {1, 0, -1,  0};
const int dy[] = {0, 1,  0, -1};
bool check2(int x, int y) {
  if (x < 0 || x >= n) return true;
  y = (y + m) % m;
  if (a[x][y] == -1) return true;
  int c1 = 0;
  int c2 = 0;
  for (int i = 0; i < 4; i++) {  
    int x1 = x + dx[i];
    if (x1 < 0 || x1 >= n) continue;
    int y1 = (y + dy[i] + m) % m;
    if (a[x1][y1] == a[x][y]) {
      c1++;
    }
    if (a[x1][y1] == -1) {
      c2++;
    }
  }
  if (c1 > a[x][y] || c1 + c2 < a[x][y]) return false;
  return true;
}
bool check(int x, int y) {
  if (!check2(x, y)) {
    return false;
  }
  for (int i = 0; i < 4; i++) {
    if (!check2(x + dx[i], y + dy[i])) {
      return false;
    }
  }
  return true;
}
set<vector<vector<int> > > M;
void bct(int x, int y) {
  if (y == m) {
    bct(x + 1, 0);
    return;
  }
  if (x == n) {
    for (int sh = 0; sh < m; sh++) {
      vector<vector<int> > c(n, vector<int>(m, 0));
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          c[i][j] = a[i][(j + sh) % m];
        }
      }
      if (M.find(c) != M.end()) {
        return;
      }
      if (sh == m - 1) {
        M.insert(c);
      }
    }      
    return;
  }
  for (int i = 1; i < 4; i++) {
    a[x][y] = i;
    if (check(x, y)) {
      bct(x, y + 1);
    }
    a[x][y] = -1;
  }
}

void solve() {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      a[i][j] = -1;
    }
  }
  M.clear();
  bct(0, 0);
  printf("%d\n", M.size());
}

int main(){
  assert(freopen(problem_name".out","wt",stdout));
  assert(freopen(problem_name".in","rt",stdin));
  int T;
  scanf("%d", &T);
  for (int ti = 1; ti <= T; ti++) {
    printf("Case #%d: ", ti);
    solve();
  }
  return 0;
}
