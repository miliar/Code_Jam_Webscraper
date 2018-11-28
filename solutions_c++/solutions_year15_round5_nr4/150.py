#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
//#include <iostream>
#include <numeric>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
//#include <cmath>
#include <set>
#include <map>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b);i>=(e);--i)

#define PB push_back
#define ALL(V) (V).begin(),(V).end()
#define SIZE(V) ((int)(V).size())

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
  #define debug(...) fprintf(stderr, __VA_ARGS__)
#else
  #define debug(...)
#endif

int __stmp;
#define scanf __stmp=scanf


// const int INF = 1000000001;
// const int MAX = 100000;

#define PARALLEL 0

/* UWAGA NA PAMIEC!
   Moze byc potrzebne nawet Z razy wiecej pamieci w trakcie dzialania,
   chyba ze bedzie sie ja alokowac i zwalniac w solve() wtedy moze byc
   potrzebne do <liczba rdzeni> razy wiecej.
   Kompilowac z --openmp
 */

class solver {
  public:
    void input() {
      scanf("%d", &p);
      val.resize(p);
      cnt.resize(p);
      REP(i,p)
        scanf("%lld", &val[i]);
      REP(i,p)
        scanf("%lld", &cnt[i]);
    }

    void solve() {
      set<LL> usedneg;
      while(1)
      {
        LL c; bool f = false;
        REP(i,p)
          if(val[i] == 0) {
            if(cnt[i] > 1) {
              f = true;
              c = 0;
              break;
            }
          } else {
            if(cnt[i] > 0 && usedneg.count(val[i]) == 0) {
              f = true;
              c = val[i];
              break;
            }
          }
        if(!f) break;
        // printf("%lld\n", c);
        // REP(i,p) printf("%lld ", cnt[i]); printf("\n");
        if(solve(c)) {
          cnt = tmpcnt;
          res.PB(c);
        } else {
          if(c < 0) usedneg.insert(c);
        }
      }
    }

    bool solve(LL x) {
      map<LL,LL> M;
      REP(i,p)
        M[val[i]] = cnt[i];
      if(x < 0) {
        LL sum = 0;
        REP(i,p)
        {
          LL v = val[i];
          // if(M[v] < M[v-x]) return false;
          sum += min(M[v], M[v-x]);
          M[v] -= min(M[v], M[v-x]);
        }
        if(sum & (sum-1)) return false;
      } else if(x == 0) {
        LL c = M[x];
        assert(!(c&(c-1)));
        assert(c > 1);
        for(auto &i : M)
        {
          assert(i.ND % 2 == 0);
          i.ND /= 2;
        }
      } else {
        REP(i,p)
        {
          LL v = val[i];
          if(M[v] > M[v+x]) return false;
          M[v+x] -= M[v];
        }
      }
      tmpcnt.clear();
      REP(i,p)
        tmpcnt.PB(M[val[i]]);
      return true;
    }

    void output() {
      for(LL a : res)
        printf("%lld ", a);
      printf("\n");
    }
  private:
    int p;
    VLL val, cnt;
    VLL res;
    VLL tmpcnt;
};

int main(int argc, char *argv[]) {
  int case_id = argc == 2 ? atoi(argv[1])-1 : -1;
  int Z;
  scanf("%d", &Z);
  vector<solver> S(Z);
  REP(z,Z) S[z].input();
  if(case_id == -1) {
    #if PARALLEL == 1
      #pragma omp parallel for schedule(dynamic)
    #endif
    REP(z,Z) S[z].solve();
  } else {
    S[case_id].solve();
  }
  REP(z,Z)
  {
    if(case_id == -1 || z == case_id) {
      printf("Case #%d: ", z+1);
      S[z].output();
    }
  }
  return 0;
}
