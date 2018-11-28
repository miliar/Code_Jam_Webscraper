#include <bits/stdc++.h>

using namespace std;

#define FOR(i,s,e) for(int (i)=(s);(i)<(int)(e);(i)++)
#define REP(i,e) FOR(i,0,e)
#define RFOR(i,e,s) for(int (i)=(e)-1;(i)>=(int)(s);(i)--)
#define RREP(i,e) RFOR(i,e,0)

#define all(o) (o).begin(), (o).end()
#define psb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))

typedef long long ll;
typedef pair<int, int> PII;
typedef priority_queue<int, vector<int>, greater<int>> PQI;
typedef priority_queue<PII, vector<PII>, greater<PII>> PQII;

const double EPS = 1e-10;
const int T = 100;
const int N = 100;
int t, n;
int pk[N];

int main() {
  scanf("%d ", &t);
  REP(cs, t) {
    string s; cin >> s;
    int n = s.size();
    REP(i,n) pk[i] = s[i]=='+' ? 1 : -1;

    int res = 0;
    while (1) {
      int r = 0;
      while (r+1<n && pk[r+1]==pk[0]) r++;
      if (r==n-1) {
        res += pk[0]==1 ? 0 : 1;
        break;
      }
      REP(i,r+1) pk[i] *= -1;
      res++;
    }
    printf("Case #%d: %d\n", cs+1, res);
  }
  return 0;
}

