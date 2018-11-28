#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;
typedef long long i64;
typedef i64 nkr_int;
typedef pair<i64, i64> pi;

typedef vector<nkr_int> vi;
typedef vector<vi> vvi;
#define pb push_back
#define iter(T) T::iterator
#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define present(c, x) ((c).find(x) != (c).end())
#define cpresent(c, x) (find(all(c), x) != (c).end())
#define REP(s, e, n)  for(n = (s); n < (e); ++n)

class Solver {
public:
  Solver() {}
  ~Solver() {}

  void solve();
};


void Solver::solve() {
  i64 R, C;
  cin >> R >> C;
  vector<string> A(R);
  i64 i, j;
  getchar();
  REP(0, R, i) {
    getline(cin, A[i]);
  }

  vi idx_l(R, -1), idx_r(R, -1), idx_u(C, -1), idx_d(C, -1);
  REP(0, R, i) {
    REP(0, C, j) {
      if(A[i][j] != '.') {
	idx_l[i] = j;
	break;
      }
    }
    REP(0, C, j) {
      if(A[i][C-1-j] != '.') {
	idx_r[i] = C-1-j;
	break;
      }
    }
  }
  REP(0, C, j) {
    REP(0, R, i) {
      if(A[i][j] != '.') {
	idx_u[j] = i;
	break;
      }
    }
    REP(0, R, i) {
      if(A[R-1-i][j] != '.') {
	idx_d[j] = R-1-i;
	break;
      }
    }
  }
  
  i64 ans = 0;
  REP(0, R, i) {
    REP(0, C, j) {
      switch(A[i][j]) {
      case '<':
	if(idx_l[i] >= j) {
	  if(idx_r[i] > j ||
	     idx_u[j] < i ||
	     idx_d[j] > i
	     )	    {
	    ans++;
	  }
	  else {
	    goto imp;
	  }
	  continue;
	}
	break;
      case '>':
	if(idx_r[i] <= j) {
	  if(idx_l[i] < j ||
	     idx_u[j] < i || 
	     idx_d[j] > i) {
	    ans++;
	  }
	  else {
	    goto imp;
	  }
	}
	break;
      case '^':
	if(idx_u[j] >= i) {
	  if(idx_d[j] > i ||
	     idx_l[i] < j ||
	     idx_r[i] > j) {
	    ans++;
	  }
	  else {
	    goto imp;
	  }
	}
	break;
      case 'v':
	if(idx_d[j] <= i) {
	  if(idx_u[j] < i ||
	     idx_l[i] < j ||
	     idx_r[i] > j) {
	    ans++;
	  }
	  else {
	    goto imp;
	  }
	}
	break;
      } 
    }
  }

  cout << ans << endl;
  return;

imp:
  cout << "IMPOSSIBLE" << endl;
  return;
}

int main(int argc, char *argv[]){

  i64 N;
  cin >> N;
  i64 n;

  Solver s;

  REP(0, N, n) {
    cout << "Case #" << n + 1 << ": ";

    s.solve();
  }

  return 0;
}

