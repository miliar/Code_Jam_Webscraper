#include <numeric>
typedef long long ll;

#include <algorithm>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <set>
#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

double check(const vector<int> &s, const vector<int> &v){
  const int n = s.size();
  const int k = v.size();

  vector<double> prob(k);
  REP(i,1<<n){
    ll prod = 1;
    REP(j,n) if(i & (1 << j))
      prod *= s[j];
    REP(j,k) if(prod == v[j])
      prob[j] += 1.0 / (1 << n);
  }

  // REP(i,k) printf("%d:%.2f ", v[i], prob[i]); puts("");
  REP(i,k) if(prob[i] <= 1e-10) return 1e10;

  double ave = accumulate(prob.begin(), prob.end(), 0.0) / prob.size();
  double bun = 0.0;

  REP(i,k){
    bun += (prob[i] - ave) * (prob[i] - ave);
  }

  return bun;
}

int main(){
  const int T = getInt();
  const int r = getInt();
  const int n = getInt();
  const int m = getInt();
  const int k = getInt();

  printf("Case #1:\n");

  REP(i,r){
    vector<int> v(k);
    pair<double, vector<int> > ans = make_pair(1e10, vector<int>());
    REP(j,k) v[j] = getInt();

    for(int a = 2; a <= m; a++){
      for(int b = 2; b <= m; b++){
	for(int c = 2; c <= m; c++){
	  vector<int> s = { a, b, c };
	  sort(s.begin(), s.end());
	  const double bun = check(s, v);
	  // printf("%d %d %d: %.4f\n", a, b, c, bun);
	  ans = min(ans, make_pair(bun, s));
	}
      }
    }

    REP(i,n) printf("%d", ans.second[i]);
    puts("");
  }

  return 0;
}
