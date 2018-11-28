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
};

typedef pair<i64, i64> pi;
typedef pair<pi, i64> ppi;

const i64 NUM = 1000002013;

i64 N, M;
void add_cost(i64 s, i64 e, i64 t, i64 &ideal) {
  i64 d = e - s;

  N %= NUM;
  t %= NUM;

  i64 c0 = (d * N) % NUM;
  ideal += (c0 * t) % NUM;

  i64 c1 = (d * (d - 1) / 2) % NUM;
  ideal -= (c1 * t) % NUM;

  if(ideal < 0) {
    while(ideal < 0) {
      ideal += NUM;
    }
  }
  ideal %= NUM;
}

void Solver::solve() {
  cin >> N >> M;
  
  vector<ppi> nums(M);
  set<i64> stations0;
  i64 i, j;

  i64 ideal = 0;
  REP(0, M, i) {
    cin >> nums[i].first.first >> nums[i].first.second >> nums[i].second;
    stations0.insert(nums[i].first.first);
    stations0.insert(nums[i].first.second);

    add_cost(nums[i].first.first, nums[i].first.second, nums[i].second, ideal);
  }
  vi stations(all(stations0));

  vi passengers(sz(stations) - 1, 0);
  REP(0, M, i) {
    vi::iterator is = lower_bound(all(stations), nums[i].first.first);
    vi::iterator ie = lower_bound(all(stations), nums[i].first.second);

    i64 s0 = is - stations.begin();
    i64 e0 = ie - stations.begin();
    REP(s0, e0, j) {
      passengers[j] += nums[i].second;
    }
  }

  bool flag = true;
  vi::iterator b = passengers.begin(), e = passengers.begin();
  i64 real = 0;
  while(flag) {
    b = e;
    while(b != passengers.end() && *b == 0) {
      b++;
    }
    if(b == passengers.end()) {
      if(e == passengers.begin()) {
	break;
      }
      else {
	e = passengers.begin();
      }
    }
    else {
      i64 minval = *b;
      e = b;
      while(e != passengers.end() && *e != 0) {
	minval = min(minval, *e);
	e++;
      }

      add_cost(stations[b - passengers.begin()], stations[e - passengers.begin()], minval, real);
      for(vi::iterator it=b;it!=e;++it) {
	(*it) -= minval;
      }

      if(e == passengers.end()) {
	e = passengers.begin();
      }
    }
  }
  cout << ideal - real << endl;
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

