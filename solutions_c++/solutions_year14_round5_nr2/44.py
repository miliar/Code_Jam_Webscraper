#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <sys/time.h>
#include <unordered_map>
#include <unordered_set>
#include <unistd.h>
#include <utility>
#include <vector>
using namespace std;
#define i32         int32_t
#define rep(i, n)   for(i32 i = 0; i < ((i32)(n)); ++i)
#define sz(v)       ((i32)((v).size()))
#define bit(n)      (((i32)1)<<((i32)(n)))
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

const i32 MAX = 105;
i32 T, P, Q;
i32 H[MAX], G[MAX];
i32 dp[MAX][15][15][150][2];

i32 bonus0[MAX];
i32 bonus1[MAX];
i32 need1[MAX];



i32 recur(i32 pos, i32 opp, i32 my, i32 rem, i32 turn)
{
  if(pos == Q) return 0;
  if(H[pos] <= opp * P + my * T) return recur(pos + 1, 0, 0, rem, turn) + (turn == 1 ? 0 : G[pos]);
  i32 &res = dp[pos][opp][my][rem][turn];
  if(res != -1) return res;
  
  
  res = 0;
  if(opp == 0 && my == 0){
    i32 need = H[pos] / T + (H[pos] % T ? 1 : 0);
    for(i32 t = 1; t < min(rem, need); ++t){
      res = max(res, recur(pos, opp, t, rem - t, turn));
    }
    if(need <= rem){
      res = max(res, recur(pos + 1, opp, my, rem - need, turn) + G[pos]);
    }
  }
  
  if(turn){
    res = max(res, recur(pos, opp, my, rem + 1, false));
    res = max(res, recur(pos, opp, my + 1, rem, false));
  }else{
    res = max(res, recur(pos, opp + 1, my, rem, true));
  }
  
  return res;
}


int main()
{
  i32 TEST_CASE;
  cin >> TEST_CASE;
  rep(test_case, TEST_CASE){
    cin >> T >> P >> Q;
    rep(i, Q) cin >> H[i] >> G[i];
    
    memset(dp, -1, sizeof(dp));
    i32 ans = recur(0, 0, 0, 0, 1);
    cout << "Case #" << test_case + 1 << ": " << ans << endl;
  }
}






