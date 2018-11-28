#include <bits/stdc++.h>

using namespace std;
#define MP make_pair
#define PB push_back
#define LD long double
#define LL long long
#define int LL
#define FI first
#define SE second
#define R(i,n) for(int i=0;i<n;i++)
#define F(i,a,b) for(int i=a;i<b;i++)
#define FD(i,n) for(int i=n-1;i>=0;i--)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PII pair<int,int>
#define VI vector<int>

template<class C> void mini(C&a4, C b4){a4=min(a4,b4);}
template<class C> void maxi(C&a4, C b4){a4=max(a4,b4);}

template<class TH> void _dbg(const char *sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a){
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<"="<<h<<","; _dbg(sdbg+1,a...);
}

template<class T> ostream& operator<<(ostream& os, vector<T> V) {
  os << "[";
  for (auto& tt : V) { os << tt << ","; }
  os << "]";
  return os;
}

#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (__VA_ARGS__)
#define cerr if(0) cout
#endif

struct Sol{
  
  void go(int cas){
    cout << "Case #" << cas << ": ";
    int n;
    cin >> n;
    if(n == 0){
      cout << "INSOMNIA\n";
      return;
    }
    set<int> pom;
    int res = 0;
    while(SZ(pom)!=10){
      res++;
      int pom2 = n * res;
      while(pom2){
        pom.insert(pom2%10);
        pom2/=10;
      }
    }
    cout << n * res << "\n";
  }
};


#undef int
int main(){
#define int LL
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
