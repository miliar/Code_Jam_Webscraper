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

string z[20][3];

struct Sol{
  bool spr(string &a,int r,int p,int s){
    for(char z:a){
      if(z == 'P')p--;
      if(z == 'R')r--;
      if(z == 'S')s--;
    }
    return p == 0 && r == 0 && s == 0;
  }
  void go(int cas){
    cout << "Case #" << cas << ": ";
    int n,r,p,s;
    string res;
    cin >> n >> r >> p >> s;
    R(i,3){
      if(spr(z[n][i],r,p,s)){
        cout << z[n][i] << "\n";
        return;
      }
    }
    cout << "IMPOSSIBLE\n";
  }
};


string lacz(string& a,string &b){
  if(a < b)
    return a + b;
  else
    return b + a;
}
int32_t main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(11);
  cerr << fixed << setprecision(11);
  z[0][0] = "P";
  z[0][1] = "R";
  z[0][2] = "S";
  for(int i=1;i<=13;i++){
    R(j,3){
      z[i][j] = lacz(z[i-1][j],z[i-1][(j+1)%3]);
    }
  }
  int t;  
  cin >> t;
  R(i,t){
    Sol sol;
    sol.go(i+1);
  }
}
