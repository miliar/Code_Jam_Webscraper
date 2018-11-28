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
  int n;
  vector<vector<int>> d;
  vector<bool> cz;
  vector<pair<PII,int>> t;
  void init(){
    d.resize(n*2);
    cz.resize(n*2);
  }
  void add_edge(int a,int b){
    d[a].PB(b);
    d[b].PB(a);
  }
  PII dfs(int nr){
    if(cz[nr])return {0,0};
    cz[nr] = 1;
    int a = nr < n, b = nr < n ? 1 : -1;
    for(int ak:d[nr]){
      PII pom = dfs(ak);
      a += pom.FI;
      b += pom.SE;
    }
    return {a,b};
  }
  
  void dod(PII x){
    debug("dod",x.FI,x.SE);
    for(auto &el:t){
      if(x == el.FI){
        el.SE ++;
        return;
      }
    }
    t.PB({x,1});
  }
  
  map<pair<vector<int>, int>, int> pam;
  vector<int> kr;
  int licz(int roz,int bil){
    if(bil == 0 && roz != 0){
      return licz(0,0) + roz * roz;
    }
    auto x = pam.find({kr,roz});
    if(x != pam.end())return x->SE;
    int &res = pam[{kr,roz}];
    res = 1e9;
    bool cz = 1;
    R(i,SZ(t)){
      if(kr[i] < t[i].SE){
        cz = 0;
        kr[i]++;
        mini(res,licz(roz + t[i].FI.FI, bil + t[i].FI.SE));
        kr[i]--;
      }
    }
    if(cz)res = 0;
    return res;
  }
  
  void go(int cas){
    cout << "Case #" << cas << ": ";
    cin >> n;
    init();
    int res = 0;
    R(i,n){
      string z;
      cin >> z;
      R(j,n)if(z[j] == '1'){
        add_edge(i,n+j);
        res--;
      }
    }
    R(i,n*2){
      if(!cz[i]){
        PII x = dfs(i);
        if(x.SE == 0){
          res += x.FI * x.FI;
        }else{
          dod(x);
        }
      }
    }
    kr.resize(SZ(t));
    debug(res);
    cout << licz(0,0) + res << endl;
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
