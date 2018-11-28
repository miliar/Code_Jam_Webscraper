#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo (1<<30)
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define iter(it,s) for(__typeof(s.begin())it = s.begin();it!=s.end();it++)

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int main() {
#ifndef ONLINE_JUDGE
  freopen("test.in", "rt", stdin);
//  freopen("ans.txt", "wt", stdout);
#endif
  int t;
  cin >> t;
  FOR (cs , 1 , t + 1)
  {
    long double C, F, X, res = 1e15, c = 2, cnt = 0;
    cin >> C >> F >> X;
    FOR (i , 0 , 100000000) {
      res = min (res, cnt + (X / c));
      cnt += C / c;
      c += F;
    }
    printf ("Case #%d: %.7lf\n", cs, (double)res);
  }
  return 0;
}
