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





i64 n, d;
vector<vector<i64>> children;
vector<i64> cut;
vector<i64> salaries;
vector<i64> total;
vector<i64> sorted;

i64 getTotal(i64 pos)
{
  i64 &res = total[pos];
  if(res != -1) return res;
  res = 1;//salaries[pos];
  for(auto child: children[pos]) res += getTotal(child);
  return res;
}

void recur(i64 pos, i64 lower, i64 upper)
{
  i64 salary = salaries[pos];
  if(1){
    if(salary < sorted[lower] || sorted[upper] + d < salary){
      for(i64 i = lower; i <= upper; ++i){
        cut[i] += getTotal(pos);
      }
      return;
    }

    while(lower <= upper){
      if(salary <= sorted[lower] + d) break;
      cut[lower] += getTotal(pos);
      ++lower;
    }
    while(lower <= upper){
      if(sorted[upper] <= salary) break;
      cut[upper] += getTotal(pos);
      --upper;
    }
    if(!(lower <= upper)) return;

    for(auto child: children[pos]) recur(child, lower, upper);
  }else if(0){
    if(salary < sorted[lower] || sorted[upper] < salary){
      for(i64 i = lower; i <= upper; ++i){
        cut[i] += getTotal(pos);
      }
      return;
    }

    while(lower <= upper){
      if(salary - d <= sorted[lower]) break;
      cut[lower] += getTotal(pos);
      ++lower;
    }
    while(lower <= upper){
      if(sorted[upper] <= salary + d) break;
      cut[upper] += getTotal(pos);
      --upper;
    }
    if(!(lower <= upper)) return;

    for(auto child: children[pos]) recur(child, lower, upper);
  }else{
    while(lower <= upper){
      if(abs(salary - sorted[lower]) <= d) break;
      cut[lower] += getTotal(pos);
      ++lower;
    }
    while(lower <= upper){
      if(abs(salary - sorted[upper]) <= d) break;
      cut[upper] += getTotal(pos);
      --upper;
    }
    for(auto child: children[pos]) recur(child, lower, upper);
  }
}

int main()
{
  i64 T;
  cin >> T;
  rep(test_case, T){
    cin >> n >> d;
    children = vector<vector<i64>>(n);
    cut = vector<i64>(n, 0);
    salaries = vector<i64>(n, 0);
    total = vector<i64>(n, -1);
    vector<i64> managers(n);
    i64 m, a, c, r;
    cin >> salaries[0] >> a >> c >> r;
    rep(i, n)if(i) salaries[i] = (salaries[i - 1] * a + c) % r;
    cin >> managers[0] >> a >> c >> r;
    rep(i, n)if(i) managers[i] = (managers[i - 1] * a + c) % r;

    bool debug = false;
    if(debug){
      d = 3;
      rep(i, n) salaries[i] = 100 - i;
      rep(i, n) managers[i] = i - 1;
    }

    rep(i, n)if(i) children[managers[i] % i].push_back(i);
    if(debug){
      DEBUG(salaries);
      DEBUG(children);
    }

    sorted = salaries;
    sort(all(sorted));
    recur(0, 0, n - 1);
    i64 best = n;
    printf("Case #%d: %d\n", (int)test_case + 1, (int)(n - *min_element(all(cut))));
  }
}



















