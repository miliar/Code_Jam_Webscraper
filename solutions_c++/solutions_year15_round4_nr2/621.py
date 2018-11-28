#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <limits>

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

  i64 N;
  double V, X;
  cin >> N >> V >> X;
  
  i64 i;
  vector<double> R(N), C(N);
  REP(0, N, i) {
    cin >> R[i] >> C[i];
  }

  double eps = numeric_limits<double>::epsilon() * 10;
  double ans;
  if(N == 1) {
    if(abs(C[0] - X) > eps) {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
    else {
      ans = V / R[0];
    }
  }
  else if(N == 2) {
    if(abs(C[0] - X) < eps) {
      if(abs(C[1] - X) < eps) {
	ans = V / (R[0] + R[1]);
      }
      else {
	ans = V / R[0];
      }
    }
    else {
      if(abs(C[1] - X) < eps) {
	ans = V / R[1];
      }
      else {
	if(abs(C[1] - C[0]) < eps) {
	  cout << "IMPOSSIBLE" << endl;
	  return;
	}
	double t0, t1;
	t1 = - (C[0] - X) * V / (C[1] - C[0]) / R[1];
	t0 = - (C[1] - X) * V / (C[0] - C[1]) / R[0];
	if(t0 < 0 || t1 < 0) {
	  cout << "IMPOSSIBLE" << endl;
	  return;
	}
	ans = max(t0, t1);
      }
    }
  }
  printf("%.9f\n", ans);
  
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

