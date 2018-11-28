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

int d[3];
int e[3];
int n;
string cc[3] = {"R", "P", "S"};

string calc(int lvl, int p) {
  if (lvl == n+1) {
    //cout << "MASUK " << cc[p] << endl;
    e[p]++;
    return cc[p];
  }
  int q = (p+2)%3;
  string s1 = calc(lvl + 1, p);
  string s2 = calc(lvl + 1, q);
  if (s1 < s2) return s1 + s2;
  else return s2 + s1;
}

int main() {
  int tc;
  scanf("%d", &tc);
  while(tc--) {
    static int t = 0;
    printf("Case #%d: ", ++t);
    scanf("%d%d%d%d",&n,&d[0],&d[1],&d[2]);
    string ans = "~";
    {
      RESET(e, 0);
      string s = calc(1, 0);
      //cout << s.length() << " " << e[0] << " " << e[1] << " " << e[2] << endl;
      if (d[0] == e[0] && d[1] == e[1] && d[2] == e[2] && ans > s) {
        ans = s;
      }
    }
    {
      RESET(e, 0);
      string s = calc(1, 1);
      //cout << s.length() << " " << e[0] << " " << e[1] << " " << e[2] << endl;
      if (d[0] == e[0] && d[1] == e[1] && d[2] == e[2] && ans > s) {
        ans = s;
      }
    }
    {
      RESET(e, 0);
      string s = calc(1, 2);
      //cout << s.length() << " " << e[0] << " " << e[1] << " " << e[2] << endl;
      if (d[0] == e[0] && d[1] == e[1] && d[2] == e[2] && ans > s) {
        ans = s;
      }
    }
    if (ans == "~") ans = "IMPOSSIBLE";
    cout << ans << endl;
  }
}