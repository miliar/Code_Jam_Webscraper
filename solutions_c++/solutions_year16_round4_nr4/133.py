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

int mx[8] = {-1,1,0,0,-1,-1,1,1};
int my[8] = {0,0,-1,1,-1,1,-1,1};

// ----- //

vector<int> valid[5];
bool adj[5][5];
int ordr[5];
bool used[5];

bool coba2(int pos, int k) {
  if (pos == k) {
    return 1;
  }
  int j = ordr[pos];
  bool exist = 0;
  bool can = 1;
  for(int i = 0; i < k; i++) {
    if (adj[j][i] && !used[i]) {
      used[i] = 1;
      exist |= 1;
      can &= coba2(pos + 1, k);
      used[i] = 0;
    }
  }
  return exist & can;
}

bool coba(int k) {
  for(int i = 0; i < k; i++) {
    ordr[i] = i;
  }
  bool can = 1;
  do {
    //cout << "BISA" << endl;
    can &= coba2(0, k);
  } while(next_permutation(ordr, ordr + k));
  return can;
}

void bf(int k) {
  int s = k * k;
  for(int mask = 0; mask < (1 << s); mask ++) {
    for(int i = 0; i < k; i++) {
      for(int j = 0; j < k; j++) {
        adj[i][j] = mask & (1 << (k * i + j));
      }
    }
    //cout << "TEST " << k << " " << mask << endl;
    if (coba(k)) {
      valid[k].pb(mask);
    }
  }
}

char s[10005];

int main() {
  for(int i = 1; i <= 4; i++) {
    bf(i);
    //cout << "DONE " << i << " " << SIZE(valid[i]) << endl;
  }
  //cout << "DONE!" << endl;

  int tc;
  scanf("%d", &tc);
  //cout << "TC " << tc << endl;
  while(tc--) {
    static int t = 0;
    printf("Case #%d: ", ++t);
    int n;
    scanf("%d",&n);
    //cout << "N " << n << endl;
    int mask = 0;
    for(int i = 0; i < n; i++) {
      scanf("%s", s);
      for(int j = 0; j < n; j++) {
        if (s[j] == '1') {
          mask |= (1 << (n*i+j));
        }
      }
    }
    //cout << "MASK " << mask << endl;
    int ans = INF;
    for(int v: valid[n]) {
      if ((v | mask) == v) {
        MIN(ans, __builtin_popcount(v) - __builtin_popcount(mask));
      }
    }
    printf("%d\n", ans);
  }
}