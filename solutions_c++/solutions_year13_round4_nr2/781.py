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
  i64 solve2(i64 N, i64 P);
};


void Solver::solve() {
  i64 N, P;
  cin >> N >> P;

  i64 a1, a2;
  i64 num = 1 << N;
  a1 = solve2(N, P);
  a2 = (num - 1) - (solve2(N, num - P) + 1);
  cout << a1 << " " << a2 << endl;
}

i64 Solver::solve2(i64 N, i64 P) {
  i64 n2 = 1 << N;
  if(P == n2) {
    return n2 - 1;
  }

  i64 th = n2 - P;
  i64 i = 0;
  i64 nc = n2 - 1;
  while(nc >= th) {
    nc /= 2;
    ++i;
  }

  i64 ans = 1 << i;
  return ans - 2;
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

