#include <bits/stdc++.h>
using namespace std;

#undef _P
#define _P(...) (void)printf(__VA_ARGS__)
#define FORR(x,arr) for(auto&& x:arr)
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define RFOR(i,a,b) for (int i = (b)-1; i >= (a); i--)
#define REP(i,n) for (int i = 0; i < (n); i++)
#define RREP(i,n) for (int i = (n)-1; i >= 0; i--)
#define ALL(x) (x).begin(), (x).end()
#define ITR(x,c) for(__typeof(c.begin()) x=c.begin();x!=c.end();x++)
#define RITR(x,c) for(__typeof(c.rbegin()) x=c.rbegin();x!=c.rend();x++)
#define BIT(n) (1LL<<(n))
#define SZ(x) ((int)(x).size())
typedef long long ll;
// -------------------------------------

int N, R, P, S;

const int _P=0, _R=1, _S=2;

int f(int np, int nr, int ns) {
  //_P("(%d,%d,%d)\n", np,nr,ns);
  int pg = 0, rg = 0, sg = 0;
  if (np + nr + ns == 1) {
    if (np) return _S;
    if (nr) return _P;
    if (ns) return _R;
  }
  if (np + nr + ns == 2) {
    if (np && nr) return _S;
    if (nr && ns) return _P;
    if (ns && np) return _R;
    return -1;
  }
  while (np + nr + ns) {
    if (np >= 2 && nr && ns && np >= nr && np >= ns) {
      pg++;
      np-=2;
      nr-=1;
      ns-=1;
    }
    else if (nr >= 2 && np && ns && nr >= ns && nr >= np) {
      rg++;
      np-=1;
      nr-=2;
      ns-=1;
    }
    else if (ns >= 2 && nr && np && ns >= nr && ns >= np) {
      sg++;
      np-=1;
      nr-=1;
      ns-=2;
    }
    else {
      return -1;
    }
  }
  return f(pg, rg, sg);
}

string create(int m, int n) {
  if (n == 0) {
    if (m == _P) {
      return "P";
    }
    else if (m == _R) {
      return "R";
    }
    else if (m == _S) {
      return "S";
    }
  }
  string s1, s2;
  if (m == _P) {
    s1 = create(_P, n-1);
    s2 = create(_R, n-1);
  }
  else if (m == _R) {
    s1 = create(_R, n-1);
    s2 = create(_S, n-1);
  }
  else if (m == _S) {
    s1 = create(_S, n-1);
    s2 = create(_P, n-1);
  }
  if (s1 < s2) return s1 + s2;
  else return s2 + s1;
}

void solve() {
  cin >> N >> R >> P >> S;
  if (N == 1) {
    if (P && R && !S) cout << "PR" << endl;
    else if (P && !R && S) cout << "PS" << endl;
    else if (!P && R && S) cout << "RS" << endl;
    else cout << "IMPOSSIBLE" << endl;
    return;
  }
  int winner = f(P, R, S);
  //_P("w: %d\n", winner);
  if (winner == -1) {
    cout << "IMPOSSIBLE" << endl;
  }
  else {
    cout << create(winner, N) << endl;
  }
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  REP(i, T) {
    cout << "Case #" <<  i+1 << ": ";
    solve();
  }

  return 0;
}
