#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

#define FOR(i,a,b) for(int i(a); i <= b; ++i)
#define FORD(i,a,b) for(int i(a); i >= b; --i)
#define REP0(i,n) FOR(i,0,n-1)
#define REP1(i,n) FOR(i,1,n)
#define PU push_back
#define PO pop_back
#define MP make_pair
#define A first
#define B second
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define SZ(s) (int)((s).size())
#define CL(a) memset((a),0,sizeof(a))
#define MAX(X,Y) X = max((X),(Y))
#define MIN(X,Y) X = min((X),(Y))
#define FORIT(X,Y) for(typeof((Y).begin()) X=(Y).begin(); X!=(Y).end(); ++X)
#define VI vector <int>
#define ll long long
#define PII pair<int,int>
#define PDD pair<double,double>
#define INF 1000000000

using namespace std;

int T;
int cnt(string &s, char a, int &p) {
    int c = 0;
    while (p < SZ(s)) {
        if(s[p]!=a)
            break;
        c++;
        p++;
    }
    return c;
}
void solve() {
  T++;
  printf("Case #%d: ", T);
  int N;
  cin >> N;
  vector<string> S(N);
  REP0(i,N) {
    cin >> S[i];
  }
  int ans = 0;
  int p = 0;
  vector<int> P(N,0);
  while (p < SZ(S[0])) {
    char a = S[0][p];
    int c = cnt(S[0],a,p);
//    printf("%c %d\n", a, c);
    int minn = c;
    int maxx = c;
    REP1(j,N-1) {
//        printf("%d %d\n",j, P[j]);
        int d = cnt(S[j],a,P[j]);
        if (d < minn)
            minn = d;
        if (d > maxx)
            maxx = d;
        if (d == 0)
            break;
    }
    if (minn == 0) {
        ans = -1;
        break;
    }
    ans += maxx-minn;
  }
  if (ans != -1) {
    REP1(i,N-1) {
        if (P[i] != SZ(S[i])) {
            ans = -1;
            break;
        }
    }
  }
  if (ans==-1)
    printf("Fegla Won\n");
  else
    printf("%d\n", ans);
}

int main() {
//  freopen("A.in", "r", stdin);
  int T;
  cin >> T;
  while (T-->0) solve();
  return 0;
}
