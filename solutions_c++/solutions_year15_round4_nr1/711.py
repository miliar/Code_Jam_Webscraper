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
const int dx[] = {1, 0, -1,  0};
const int dy[] = {0, 1,  0, -1};
int n, m;
char a[1000][1000];
bool in(int x, int y) {
  return (x >= 0 && x < n && y >= 0 && y < m);
}
void solve() {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) {
    scanf("%s", a[i]);
  }
  int ans = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) if (a[i][j] != '.') {
      int cnt = 0;
      bool was = false;
      for (int k = 0; k < 4; k++) {
        int curx = i;
        int cury = j;
        while (1) {
          curx += dx[k];
          cury += dy[k];
          if (!in(curx, cury)) {
            cnt++;
            if (k == 0 && a[i][j] == 'v') {
              was = true;
            }
            if (k == 1 && a[i][j] == '>') {
              was = true;
            }
            if (k == 2 && a[i][j] == '^') {
              was = true;
            }
            if (k == 3 && a[i][j] == '<') {
              was = true;
            }
            break;
          }
          if (a[curx][cury] != '.') {
            break;
          }
        }
      }
      if (cnt == 4) {
        printf("IMPOSSIBLE\n");
        return;
      }
      if (was) {
        ans++;
      }
    }
  }
  printf("%d\n", ans);
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
