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
ll is_prime(ll mynum){//素数判定
  for(ll i = 2; i * i <= mynum; i++){
    if(mynum % i == 0){
      return i;
    }
  }
  return -1;
}
void solve(int N, int J){
  int ans = 0;
  vector <bool> nums(N);
  for (int bit = 0, fin = 1<<(N-2);bit < fin;bit++) {
    nums[0] = nums[N-1] = true;
    rep(j,N-2){
      if (bit & (1<<j)) {
        nums[j+1] = true;
      }else{
        nums[j+1] = false;
      }
    }
    vector <int> divs;
    for (int base = 2; base <= 10; base++) {
      ll b = 1;
      ll X = 0;
      rep(j,N){
        if (nums[j]) {
          X += b;
        }
        b *= base;
      }
      ll x = is_prime(X);
      if (x == -1) {
        break;
      }else{
        divs.pb(x);
      }
    }
    if (sz(divs) == 9) {
      for (int i = N-1; i >= 0; i--) {
        if (nums[i]) {
          cout << '1';
        }else{
          cout << '0';
        }
      }
      numa(x,divs){
        cout << ' ' << x;
      }
      cout << endl;
      ans += 1;
      if (ans == J) {
        break;
      }
    }
  }
}

int main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  //cout << solve(16,50) << endl;
  cout << "Case #1:" << endl;
  //solve(6,3);
  solve(16,50);
  return 0;
}

