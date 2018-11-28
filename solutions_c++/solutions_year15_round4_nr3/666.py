#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
#define in(a,b) ( (b).find(a) != (b).end())
#define inf 0x3f3f3f3f
#define mfill(x, a) memset(x, a, sizeof(x))
#define pb(x) push_back(x)

#ifdef DEBUG
#include "/home/lucas/Topcoder/debug.h"
#define dbg(args...) do {cerr << #args << ": "; debug,args; cerr << endl;} while(0)
#else
#define dbg(args...)
#endif

int n;

char line[200000];
map<string, int> M;

#define MAX 300
vector<int> lines[MAX];

int m;
int col[300000];
int colaux[300000];

int main() {
  int t; scanf("%d ", &t);
  for(int cn=1; cn<=t; cn++) {
    scanf("%d ", &n);

    m = 0;
    for(int i=0; i<n; i++) {
      string s;
      scanf("%[^\n]%*c", line);
      istringstream sin(line);
      while (sin >> s) {
        if (!in(s, M)) {
          M[s] = m++;
        }
        int pos = M[s];
        lines[i].pb(pos);
      }
    }

    mfill(col, 0);
    for(int v : lines[0]) {
      col[v] |= 1;
    }
    for(int v : lines[1]) {
      col[v] |= 2;
    }

    int ans = inf;


    if (n == 2) {
      ans = 0;
      for(int i=0; i<m; i++) {
        if (col[i] == 3) ans ++;
      }
    } else if (n <= 20) {
      for(int j=0; j<(1<<(n-2)); j++) {
        memcpy(colaux, col, sizeof(int) * m);
        for(int i=2; i<n; i++) {
          int c = ( j & (1 << (i-2)) )?1:0;
          for(int v : lines[i]) {
            colaux[v] |= (1<<c );
          }
        }
        int v = 0;
        for(int i=0; i<m; i++) {
          if (colaux[i] == 3) v ++;
        }
        ans = min(v, ans);
      }
    }

    printf("Case #%d: %d\n", cn, ans);
    M.clear();
    for(int i=0; i<n; i++) {
      lines[i].clear();
    }
  }
  return 0;
}
