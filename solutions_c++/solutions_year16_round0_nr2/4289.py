#include <bits/stdc++.h>
#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(auto it=(X).begin();it!=(X).end();it++)
#define numa(x,a) for(auto x: a)
#define ite iterator
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define pf push_front
#define sec second
#define sz(x) ((int)(x).size())
#define ALL( c ) (c).begin(), (c).end()
#define gcd(a,b) __gcd(a,b)
#define mem(x,n) memset(x,n,sizeof(x))
#define endl "\n"
using namespace std;
template <int POS, class TUPLE> void deploy(std::ostream &os, const TUPLE &tuple){}
template <int POS, class TUPLE, class H, class ...Ts> void deploy(std::ostream &os, const TUPLE &t){ os << (POS == 0 ? "" : ", ") << get<POS>(t); deploy<POS + 1, TUPLE, Ts...>(os, t); }
template <class T,class U> std::ostream& operator<<(std::ostream &os, std::pair<T,U> &p){ os << "(" << p.first <<", " << p.second <<")";return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> &v){ int remain = v.size(); os << "{"; for(auto e: v) os << e << (--remain == 0 ? "}" : ", "); return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> &v){ int remain = v.size(); os << "{"; for(auto e: v) os << e << (--remain == 0 ? "}" : ", "); return os; }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> &mp){ int remain = mp.size(); os << "{"; for(auto e: mp) os << "(" << e.first << " -> " << e.second << ")" << (--remain == 0 ? "}" : ", "); return os; }
#define DEBUG1(var0) { std::cerr << (#var0) << "=" << (var0) << endl; }
#define DEBUG2(var0, var1) { std::cerr << (#var0) << "=" << (var0) << ", ";DEBUG1(var1); }
#define DEBUG3(var0, var1, var2) { std::cerr << (#var0) << "=" << (var0) << ", ";DEBUG2(var1,var2); }
#define DEBUG4(var0, var1, var2, var3) { std::cerr << (#var0) << "=" << (var0) << ", ";DEBUG3(var1,var2,var3); }
using ll = long long;

inline pair <int,int> minusfind(string &s){//[x,y)
  int x,y;
  for (int i = 0; i < sz(s);i++) {
    if (s[i] == '-') {
      x = i;
      break;
    }
  }
  y = sz(s);
  for (int i = x; i < sz(s);i++) {
    if (s[i] != '-') {
      y = i;
      break;
    }
  }
  return mp(x,y);
}
inline bool OK(string &s){
  auto it = find(ALL(s), '-');
  return it == s.end();
}
inline int solve(string &s){
  int ans = 0;
  while(!OK(s)){
    pair <int,int> t = minusfind(s);
    int x = t.fir;
    int y = t.sec;
    if (x == 0) {
      for (int i = 0; i < y; i++) {
        s[i] = '+';
      }
    }else{
      for (int i = 0; i < x; i++) {
        s[i] = '-';
      }
    }
    ans += 1;
    //DEBUG2(ans, s);
  }
  return ans;
}

int main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  int T;
  cin >> T;
  rep(i,T){
    string S;
    cin >> S;
    cout << "Case #" << i+1 << ": " << solve(S) << endl;
  }

  return 0;
}

