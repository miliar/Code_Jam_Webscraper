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
#endif


vector<bool> goodMasks[5];

void preproc() {
  for (int N = 1; N <= 4; N++) {
    vector<int> perm(N);
    iota(ALL(perm), 0);
    vector<vector<bool>> can(N, vector<bool>(N, false));

    for (int nmask = 0; nmask <= (1 << (N * N)); nmask++) {
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          can[i][j] = (nmask & (1 << (i * N + j)));
        }
      }

      bool badmask = false;

      for (int i = 0; i < N; i++) {
        int tmask = 0;
        for (int j = 0; j < N; j++) {
          if (can[i][j]) { tmask |= (1 << j); }
        }

        if (!tmask) { badmask = true; break; }

        int cpmask = tmask;

        do {
          tmask = cpmask;
          for (int x = 0; x < N; x++) {
            if (x == i) { continue; }
            if (can[x][perm[x]]) { tmask &= ~(1 << perm[x]); }
            if (!tmask) {
              badmask = true;
              break;
            }
          }

        } while (next_permutation(ALL(perm)));

        if (badmask) { break; }
      }

      goodMasks[N].push_back(!badmask);
    }
  }
}


struct Test {

  void run(int testid) {
    int N;
    cin >> N;
    int mask = 0;

    int result = 1e9;

    for (int i = 0; i < N * N; i++) {
      char ch;
      cin >> ch;
      if (ch == '1') { mask |= (1 << i); }
    }


    for (int nmask = mask; nmask < (1 << (N * N)); nmask = (nmask + 1) | mask) {
      if (goodMasks[N][nmask]) {
        mini(result, (int)__builtin_popcount(nmask) - __builtin_popcount(mask));
      }
    }

    cout << "Case #" << testid << ": " << result << "\n";
  }
};


#undef int
int main(){
#define int LL
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(11);
  cerr << fixed << setprecision(6);

  preproc();

  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cerr << i << "\n";
    Test test;
    test.run(i);

  }

  return 0;
}
