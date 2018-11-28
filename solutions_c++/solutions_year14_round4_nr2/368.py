#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <unordered_map>
#include <utility>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <sys/time.h>
#include <vector>
using namespace std;
#define i64         int64_t
#define rep(i, n)   for(i64 i = 0; i < ((i64)(n)); ++i)
#define sz(v)       ((i64)((v).size()))
#define bit(n)      (((i64)1)<<((i64)(n)))
#define all(v)      (v).begin(), (v).end()

template <int POS, class TUPLE> void deploy(std::ostream &os, const TUPLE &tuple){}
template <int POS, class TUPLE, class H, class ...Ts> void deploy(std::ostream &os, const TUPLE &t){ os << (POS == 0 ? "" : ", ") << get<POS>(t); deploy<POS + 1, TUPLE, Ts...>(os, t); }
template <class ...Ts> std::ostream& operator<<(std::ostream &os, const std::tuple<Ts...> &t){ os << "("; deploy<0, std::tuple<Ts...>, Ts...>(os, t); os << ")"; return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> &v){ int remain = v.size(); os << "{"; for(auto e: v) os << e << (--remain == 0 ? "" : ", "); os << "}"; return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> &v){ int remain = v.size(); os << "{"; for(auto e: v) os << e << (--remain == 0 ? "" : ", "); os << "}"; return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::queue<T> &q){ auto qq = q; os << "{"; for(; !qq.empty(); qq.pop()){ os << qq.front() << (qq.size() != 1 ? ", " : ""); } os << "}"; return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::priority_queue<T> &q){ auto qq = q; os << "{"; for(; !qq.empty(); qq.pop()){ os << qq.top() << (qq.size() != 1 ? ", " : ""); } os << "}"; return os; }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::pair<T, K> &p){ os << "(" << p.first << ", " << p.second << ")"; return os; }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> &mp){ int remain = mp.size(); os << "{"; for(auto e: mp) os << "(" << e.first << " -> " << e.second << ")" << (--remain == 0 ? "" : ", "); os << "}"; return os; }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::unordered_map<T, K> &mp){ int remain = mp.size(); os << "{"; for(auto e: mp) os << "(" << e.first << " -> " << e.second << ")" << (--remain == 0 ? "" : ", "); os << "}"; return os; }
#define DEBUG0() { char buf[100]; sprintf(buf, "line:%3d | ", __LINE__); std::cout << buf << std::endl; }
#define DEBUG1(var0) { char buf[100]; sprintf(buf, "line:%3d | ", __LINE__); std::cout << buf << (#var0) << "=" << (var0) << std::endl; }
#define DEBUG2(var0, var1) { char buf[100]; sprintf(buf, "line:%3d | ", __LINE__); std::cout << buf << (#var0) << "=" << (var0) << ", " << (#var1) << "=" << (var1) << std::endl; }
#define DEBUG3(var0, var1, var2) { char buf[100]; sprintf(buf, "line:%3d | ", __LINE__); std::cout << buf << (#var0) << "=" << (var0) << ", " << (#var1) << "=" << (var1) << ", " << (#var2) << "=" << (var2) << std::endl; }
#define DEBUG4(var0, var1, var2, var3) { char buf[100]; sprintf(buf, "line:%3d | ", __LINE__); std::cout << buf << (#var0) << "=" << (var0) << ", " << (#var1) << "=" << (var1) << ", " << (#var2) << "=" << (var2) << ", " << (#var3) << "=" << (var3) << std::endl; }
#define DEBUG5(var0, var1, var2, var3, var4) { char buf[100]; sprintf(buf, "line:%3d | ", __LINE__); std::cout << buf << (#var0) << "=" << (var0) << ", " << (#var1) << "=" << (var1) << ", " << (#var2) << "=" << (var2) << ", " << (#var3) << "=" << (var3) << ", " << (#var4) << "=" << (var4) << std::endl; }
#define DEBUG6(var0, var1, var2, var3, var4, var5) { char buf[100]; sprintf(buf, "line:%3d | ", __LINE__); std::cout << buf << (#var0) << "=" << (var0) << ", " << (#var1) << "=" << (var1) << ", " << (#var2) << "=" << (var2) << ", " << (#var3) << "=" << (var3) << ", " << (#var4) << "=" << (var4) << ", " << (#var5) << "=" << (var5) << std::endl; }
#define ASSERT(f) { if(!(f)){ DEBUG1("error"); while(true); }}

/*

const i64 MAX = 1050;
i64 n;
i64 positions[MAX];
i64 dp[MAX][MAX];

i64 recur(i64 used_l, i64 used_r)
{
  if(used_l == 0 && used_r == n - 1) return 0;
  i64 &res = dp[used_l][used_r];
  if(res != -1) return res;
  
  res = bit(50);
  i64 pos = positions[(n - 1) - (used_r - used_l + 1)];
  if(used_r + 1 !=  n) res = min(res, recur(used_l, used_r + 1) + max((i64)0, pos - (used_r + 1)));
  if(used_l - 1 != -1) res = min(res, recur(used_l - 1, used_r) + max((i64)0, pos - (used_l - 1)));
  
  DEBUG3(used_l, used_r, res);
  return res;
}

int main()
{
  i64 T;
  cin >> T;
  rep(test_case, T){
    cin >> n;
    vector<i64> a(n);
    rep(i, n) cin >> a[i];
    vector<i64> b = a;
    sort(all(b));
    rep(i, n)rep(j, n)if(a[i] == b[j]) positions[j] = i;
    rep(i, n) DEBUG2(i, positions[i]);
    
    memset(dp, -1, sizeof(dp));
    
    i64 ans = bit(50);
    rep(i, n){
      i64 t = recur(i, i) + max((i64)0, (positions[n - 1] - i));
      DEBUG2(i, t);
      ans = min(ans, t);
    }
    
    cout << "Case #" << test_case + 1 << ": " << ans << endl;
  }
}
*/




int main()
{
  i64 T;
  cin >> T;
  rep(test_case, T){
    i64 n;
    
    cin >> n;
    vector<i64> a(n);
    rep(i, n) cin >> a[i];
    vector<vector<i64>> greater(n, vector<i64>(n + 2, 0));
    rep(i, n){
      rep(j, n){
        greater[i][j + 1] = greater[i][j];
        if(a[i] < a[j]) greater[i][j + 1] += 1;
      }
    }
    
    vector<i64> positions(n);
    vector<i64> b = a;
    sort(all(b));
    rep(i, n)rep(j, n)if(a[i] == b[j]) positions[j] = i;
    //rep(i, n) DEBUG2(i, positions[i]);
    
    i64 ans = bit(50);
    rep(mid, n + 1){
      i64 total = 0;
      for(i64 num = n - 1; 0 <= num; --num){
        i64 pos = positions[num];
        if(mid <= pos){
          i64 rem = (pos - mid) - (greater[pos][pos] - greater[pos][mid]);
          i64 passed = greater[pos][n] - greater[pos][pos];
          i64 to_pass = (greater[pos][mid] - greater[pos][0]) + (greater[pos][pos] - greater[pos][mid]);
          i64 way0 = rem;
          i64 way1 = rem - passed + to_pass;
          total = total + min(way0, way1);
          /*
          DEBUG2(way0, way1);
          DEBUG2(mid, num);
          DEBUG3(rem, passed, to_pass);
          DEBUG1(total);
          */
        }else{
          i64 rem = (mid - pos - 1) - (greater[pos][mid] - greater[pos][pos]);
          i64 passed = greater[pos][pos] - greater[pos][0];
          i64 to_pass = (greater[pos][n] - greater[pos][mid]) + (greater[pos][mid] - greater[pos][pos]);
          i64 way0 = rem;
          i64 way1 = rem - passed + to_pass;
          total = total + min(way0, way1);
          /*
          DEBUG2(way0, way1);
          DEBUG2(mid, num);
          DEBUG3(rem, passed, to_pass);
          DEBUG1(total);
          */
        }
      }
      ans = min(ans, total);
    }
    
    cout << "Case #" << test_case + 1 << ": " << ans << endl;
  }
}




