#include <bits/stdc++.h>

using namespace std;
#define PB push_back
#define MP make_pair
#define LL long long
#define int LL
#define R(i,n) for(int i = 0; i < (n); i++)
#define VI vector<int>
#define PII pair<int,int>
#define LD long double
#define FI first
#define SE second
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())

template<class C> void mini(C& _a4, C _b4) { _a4 = min(_a4, _b4); }
template<class C> void maxi(C& _a4, C _b4) { _a4 = max(_a4, _b4); }

template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<','; _dbg(sdbg+1, a...);
}

template<class T> ostream& operator<<(ostream& os, vector<T> V) {
  os << "["; for (auto& vv : V) os << vv << ","; os << "]";
  return os;
}

#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (__VA_ARGS__)
#define cerr if(0)cout
#endif




struct Sol{
  int n,k;
  vector<LD> t;
  LD licz(vector<LD>& x){
    vector<LD> dp(k+1,0);
    dp[0] = 1;
    R(i,k){
      vector<LD> dp2;
      R(j,k+1){
        LD pom = 0;
        if(j) pom += dp[j-1] * x[i];
        pom += dp[j] * (1.-x[i]);
        dp2.PB(pom);
      }
      swap(dp,dp2);
    }
    return dp[k/2];
  }
  void go(int cas){
    cout << "Case #" << cas << ": ";
    cin >> n >> k;
    R(i,n){
      LD pom;
      cin >> pom;
      t.PB(pom);
    }
    sort(ALL(t));
    LD res = 0;
    R(i,k+1){
      vector<LD> pom;
      R(j,i)pom.PB(t[j]);
      R(j,k-i)pom.PB(t[n-1-j]);
      maxi(res,licz(pom));
    }
    cout << res << endl;
  }
};

int32_t main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(11);
  cerr << fixed << setprecision(11);
  int t;  
  cin >> t;
  R(i,t){
    Sol sol;
    sol.go(i+1);
  }
}
