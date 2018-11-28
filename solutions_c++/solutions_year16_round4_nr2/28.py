#include <bits/stdc++.h>

using namespace std;
#define MP make_pair
#define PB push_back
#define LL long long
#define int LL
#define st first
#define nd second
#define FI st
#define SE nd
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define RE(i,n) FOR(i,1,n)
#define REP(i, n) FOR(i, 0, (int)(n)-1)
#define R(i,n) REP(i,n)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PII pair<int,int>
#define VI vector<int>
template<class C> void mini(C&a, C b){a=min(a,b);}
template<class C> void maxi(C&a, C b){a=max(a,b);}

template<class TH> void _dbg(const char* sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char* sdbg, TH h, TA... t){
  while(*sdbg!=',')cerr<<*sdbg++; cerr<<"="<<h<<","; _dbg(sdbg+1, t...);
}

template<class T> ostream& operator<<(ostream& os, vector<T> V) {
  os << "["; for(auto vv : V) os << vv << ","; return os << "]";
}

#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (__VA_ARGS__)
#define cerr if(0) cout
#endif

using LD = long double;


struct Test {
  vector<LD> probabs;
  int N, K;
  LD maxProb = 0;

  LD getProb(vector<LD> P) {
    debug(P);
    assert(SZ(P) == K);
    vector<LD> res(K + 1);
    res[0] = 1;

    for (LD p : P) {
      for (int i = K; i > 0; i--) {
        res[i] = res[i - 1] * p + res[i] * (1 - p);
      }
      res[0] = res[0] * (1 - p);
    }

    return res[K / 2];
  }

  void run(int testid) {
    cin >> N >> K;
    debug(N, K);
    for (int i = 0; i < N; i++) {
      LD prob;
      cin >> prob;
      probabs.PB(prob);
    }

    sort(ALL(probabs));

    for (int lend = 0; lend <= K; lend++) {
      vector<LD> P(probabs.begin(), probabs.begin() + lend);
      for (int i = N - (K - lend); i < N; i++) { P.PB(probabs[i]); }

      maxi(maxProb, getProb(P));
    }

    cout << "Case #" << testid << ": " << maxProb << "\n";
  }
};


#undef int
int main(){
#define int LL
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(11);
  cerr << fixed << setprecision(6);

  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    Test test;
    test.run(i);
  }

  return 0;
}
