#include <bits/stdc++.h>

using namespace std;

typedef long long     LL;
typedef pair<int,int> pii;

double PI  = acos(-1);
double EPS = 1e-7;
int INF    = 1000000000;
LL INFLL   = 1000000000000000000LL;

#define fi            first
#define se            second
#define mp            make_pair
#define pb            push_back

#define input(in)     freopen(in,"r",stdin)
#define output(out)   freopen(out,"w",stdout)

#define MIN(a, b)     (a) = min((a), (b))
#define MAX(a, b)     (a) = max((a), (b))

#define RESET(a, b)   memset(a,b,sizeof(a))
#define ALL(a)        (a).begin(), (a).end()
#define SIZE(a)       (int)a.size()
#define SORT(a)       sort(ALL(a))
#define UNIQUE(a)     (a).erase( unique( ALL(a) ), (a).end() )
#define FOR(a, b, c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a, b, c) for (int (a)=(b); (a)>=(c); (a)--)
#define FORIT(a, b)   for (__typeof((b).begin()) a=(b).begin(); a!=(b).end(); a++)

int mx[4] = {1, 0, -1, 0};
int my[4] = {0, 1, 0, -1};

// ----- //

bool box[17][17];
int t[2][4] = {{3, 2, 1, 0}, {1, 0, 3, 2}};
int n, m;

int go(int x, int y, int d) {
  //cout << "GO " << x << " " << y << " " << box[x][y] << " " << d << endl;
  if (x == -1) {
    return y;
  }
  if (y == m) {
    return m + x;
  }
  if (x == n) {
    return m + n + m-1-y;
  }
  if (y == -1) {
    return m + n + m + n-1-x;
  }
  int nd = t[box[x][y]][d];
  //cout << "ND " << nd << endl;
  return go(x + mx[nd], y + my[nd], nd);
}

int match[50];
int wmatch[50];

int main() {
  int tc;
  scanf("%d", &tc);
  while(tc--) {
    static int t = 0;
    printf("Case #%d:\n", ++t);
    scanf("%d%d",&n,&m);
    for(int i = 0; i < (n + m); i++) {
      int u, v;
      scanf("%d %d", &u, &v);
      u--;
      v--;
      wmatch[u] = v;
      wmatch[v] = u;
    }
    bool ada = 0;
    for(int mask = 0; mask < (1 << (n * m)); mask++) {
      for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
          box[i][j] = (mask & (1 << (m * i + j)));
        }
      }
      //cout << "MASK " << mask << endl;
      for(int i = 0; i < m; i++) {
        match[i] = go(0, i, 0);
      }
      for(int i = 0; i < n; i++) {
        match[m+i] = go(i, m-1, 3);
      }
      for(int i = 0; i < m; i++) {
        match[m+n+i] = go(n-1, m-1-i, 2);
      }
      for(int i = 0; i < n; i++) {
        match[m+n+m+i] = go(n-1-i, 0, 1);
      }
      
      bool can = 1;
      for(int i = 0; i < 2 * (n + m); i++) {
        can &= (match[i] == wmatch[i]);
      } 
      if (can) {
        ada = 1;
        for(int i = 0; i < n; i++) {
          for(int j = 0; j < m; j++) {
            cout << (!box[i][j] ? "/" : "\\");
          }
          cout << endl;
        }
        break;
      }
    }
    if (!ada) puts("IMPOSSIBLE");

  }
}