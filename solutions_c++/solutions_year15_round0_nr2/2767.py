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

int memo[1010][1010];

int calc(int t, int x){
  if (memo[t][x] >= 0) {
    return memo[t][x];
  }
  if (t >= x) {
    return memo[t][x] = 0;
  }
  int ret = calc(t,x/2) + calc(t,(x+1)/2) + 1;
  if (x % 2 == 1) {
    ret = min(ret, calc(t,x/2) + calc(t,x/2) + 1 + 1);
  }
  ret = min(ret,calc(t,t) + calc(t,x-t) + 1);
  return memo[t][x] = ret;
}

bool OK(int t, vector <int> &nums){
  // common eat
  for (int eat = 1; eat <= t; eat++) {
    int ct = eat;
    rep(i,sz(nums)){
      int x = calc(eat, nums[i]);
      ct += x;
    }
    if (ct <= t) {
      return true;
    }
  }
  return false;
}


int main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  mem(memo,-1);
  int T;
  cin >> T;
  rep2(k,1,T+1){
    int D;
    cin >> D;
    int tmax = 0;
    vector <int> nums(D);
    rep(i,D){
      cin >> nums[i];
      tmax = max(tmax,nums[i]);
    }
    int ans = tmax;
    for (int t = 1;t <= tmax; t++) {
      if (OK(t, nums)) {
        ans = t;
        break;
      }
    }
    cout << "Case #" << k << ": " << ans << endl;
  }
  return 0;
}

