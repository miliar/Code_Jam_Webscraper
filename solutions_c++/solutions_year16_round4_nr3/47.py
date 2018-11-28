#ifndef KOMAKI_LOCAL
#define NDEBUG
#endif

#include <bits/stdc++.h>
#include <sys/time.h>
#include <unistd.h>
using namespace std;
#define i64         int64_t
#define rep(i, n)   for(i64 i = 0; i < ((i64)(n)); ++i)
#define sz(v)       ((i64)((v).size()))
#define bit(n)      (((i64)1)<<((i64)(n)))
#define all(v)      (v).begin(), (v).end()

std::string dbgDelim(int &i){ return (i++ == 0 ? "" : ", "); }
#define dbgEmbrace(exp) { int i = 0; os << "{"; { exp; } os << "}"; return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> v);
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> v);
template <class T> std::ostream& operator<<(std::ostream &os, std::queue<T> q);
template <class T> std::ostream& operator<<(std::ostream &os, std::priority_queue<T> q);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::pair<T, K> p);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> mp);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::unordered_map<T, K> mp);
template <int INDEX, class TUPLE> void dbgDeploy(std::ostream &os, TUPLE tuple){}
template <int INDEX, class TUPLE, class H, class ...Ts> void dbgDeploy(std::ostream &os, TUPLE t)
{ os << (INDEX == 0 ? "" : ", ") << get<INDEX>(t); dbgDeploy<INDEX + 1, TUPLE, Ts...>(os, t); }
template <class T, class K> void dbgDeploy(std::ostream &os, std::pair<T, K> p, std::string delim)
{ os << "(" << p.first << delim << p.second << ")"; }
template <class ...Ts> std::ostream& operator<<(std::ostream &os, std::tuple<Ts...> t)
{ os << "("; dbgDeploy<0, std::tuple<Ts...>, Ts...>(os, t); os << ")"; return os; }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::pair<T, K> p)
{ dbgDeploy(os, p, ", "); return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> v)
{ dbgEmbrace( for(T t: v){ os << dbgDelim(i) << t; }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> s)
{ dbgEmbrace( for(T t: s){ os << dbgDelim(i) << t; }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::queue<T> q)
{ dbgEmbrace( for(; q.size(); q.pop()){ os << dbgDelim(i) << q.front(); }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::priority_queue<T> q)
{ dbgEmbrace( for(; q.size(); q.pop()){ os << dbgDelim(i) << q.top();   }); }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> mp)
{ dbgEmbrace( for(auto p: mp){ os << dbgDelim(i); dbgDeploy(os, p, "->"); }); }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::unordered_map<T, K> mp)
{ dbgEmbrace( for(auto p: mp){ os << dbgDelim(i); dbgDeploy(os, p, "->"); }); }
#define DBG_OUT std::cerr
#define DBG_OVERLOAD(_1, _2, _3, _4, _5, _6, macro_name, ...) macro_name
#define DBG_LINE() { char s[99]; sprintf(s, "line:%3d | ", __LINE__); DBG_OUT << s; }
#define DBG_OUTPUT(v) { DBG_OUT << (#v) << "=" << (v); }
#define DBG1(v, ...) { DBG_OUTPUT(v); }
#define DBG2(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG1(__VA_ARGS__); }
#define DBG3(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG2(__VA_ARGS__); }
#define DBG4(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG3(__VA_ARGS__); }
#define DBG5(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG4(__VA_ARGS__); }
#define DBG6(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG5(__VA_ARGS__); }

#define DEBUG0() { DBG_LINE(); DBG_OUT << std::endl; }
#define DEBUG(...)                                                      \
  {                                                                     \
    DBG_LINE();                                                         \
    DBG_OVERLOAD(__VA_ARGS__, DBG6, DBG5, DBG4, DBG3, DBG2, DBG1)(__VA_ARGS__); \
    DBG_OUT << std::endl;                                               \
  }





// hedge
// -1: ?
// 0: /
// 1: \

const i64 U = 0;
const i64 L = 1;
const i64 D = 2;
const i64 R = 3;

class Pos
{
public:
  Pos(){}
  Pos(i64 x, i64 y, i64 dir) : x(x), y(y), dir(dir) {}

  i64 x, y, dir;
  Pos move(i64 hedge)
  {
    if(hedge == 0){
      if(dir == U) return Pos(x, y, L);
      if(dir == L) return Pos(x, y, U);
      if(dir == D) return Pos(x, y, R);
      if(dir == R) return Pos(x, y, D);
    }
    if(hedge == 1){
      if(dir == U) return Pos(x, y, R);
      if(dir == R) return Pos(x, y, U);
      if(dir == D) return Pos(x, y, L);
      if(dir == L) return Pos(x, y, D);
    }
    assert(false);
    return Pos(-1, -1, -1);
  }
  Pos flip()
  {
    if(dir == U) return Pos(x - 1, y, D);
    if(dir == D) return Pos(x + 1, y, U);
    if(dir == L) return Pos(x, y - 1, R);
    if(dir == R) return Pos(x, y + 1, L);
    assert(false);
    return Pos(-1, -1, -1);
  }

};



vector<string> solve(i64 n, i64 m, vector<i64> input)
{
  //DEBUG(n, m, input);
  unordered_map<i64, i64> pair;
  rep(i, sz(input) / 2){
    pair[input[i * 2 + 0] - 1] = input[i * 2 + 1] - 1;
    pair[input[i * 2 + 1] - 1] = input[i * 2 + 0] - 1;
  }

  i64 T = (n + m) * 2;
  vector<i64> lefts;
  rep(i, T) lefts.push_back((i + 1) % T);
  map<i64, Pos> initial_positions;
  rep(i, m) initial_positions[i] = Pos(0, i, U);
  rep(i, n) initial_positions[i + m] = Pos(i, m - 1, R);
  rep(i, m) initial_positions[i + m + n]  = Pos(n - 1, m - 1 - i, D);
  rep(i, n) initial_positions[i + m + n + m] = Pos(n - 1 - i, 0, L);
  set<tuple<i64, i64, i64>> initial_position_set;
  for(auto p: initial_positions) initial_position_set.insert(make_tuple(p.second.x, p.second.y, p.second.dir));

  vector<i64> finished(T, 0);
  vector<vector<i64>> mp(n, vector<i64>(m, -1));

  while(true){
    bool update = false;
    bool found = false;

    rep(start, T){
      if(finished[start]) continue;
      found = true;
      i64 cur = lefts[start];
      i64 end = pair[start];
      while(finished[cur] && cur != end) cur = lefts[cur];
      if(cur != end) continue;
      update = true;
      finished[start] = true;
      finished[end] = true;

      Pos pos = initial_positions[start];
      Pos goal = initial_positions[end];
      while(true){
        i64 &cell = mp[pos.x][pos.y];
        if(cell == -1) {
          cell = (pos.dir == L || pos.dir == R) ? 0 : 1;
        }
        pos = pos.move(cell);
        if(pos.x == goal.x && pos.y == goal.y && pos.dir == goal.dir) break;
        if(initial_position_set.count(make_tuple(pos.x, pos.y, pos.dir))) return vector<string>();
        pos = pos.flip();
      }
      if(0){
        vector<string> ans(n, string(m, '?'));
        char clion_bug = '\\';
        rep(i, n)rep(j, m) ans[i][j] = ((mp[i][j] == 0) ? '/' : mp[i][j] == 1 ? clion_bug : '?');
        rep(i, n) DEBUG(ans[i]);
      }
    }

    if(!found) break;
    if(!update) return vector<string>();
  }

  vector<string> ans(n, string(m, '?'));
  char clion_bug = '\\';
  rep(i, n)rep(j, m) ans[i][j] = ((mp[i][j] == 0) ? '/' : clion_bug);
  return ans;
}


int main()
{
  i64 T;
  cin >> T;
  rep(test_case, T){
    i64 n, m;
    cin >> n >> m;
    vector<i64> v(n * 2 + m * 2);
    rep(i, n * 2 + m * 2) cin >> v[i];
    vector<string> ans = solve(n, m, v);
    cout << "Case #" << test_case + 1 << ": " << endl;
    if(sz(ans) == 0){
      cout << "IMPOSSIBLE" << endl;
    }else{
      rep(i, n) cout << ans[i] << endl;
    }
  }
}

















