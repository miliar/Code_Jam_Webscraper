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











int main()
{
  i64 T;
  cin >> T;
  rep(test_case, T){
    i64 s, n;
    cin >> s >> n;
    vector<double> positions(n), speeds(n);
    rep(i, n) cin >> positions[i];
    rep(i, n) cin >> speeds[i];
    rep(i, n)if(positions[i] < 0) speeds[i] = -speeds[i];
    priority_queue<tuple<double, i64, i64>> q;
    q.push(make_tuple(0, n, 0));
    vector<unordered_map<i64, double>> mp(n + 1);
    while(sz(q)){
      i64 mask = get<2>(q.top());
      i64 pos_i = get<1>(q.top());
      double d = get<0>(q.top());
      //DEBUG(mask, pos_i, d);
      q.pop();
      if(pos_i != n && mp[pos_i][mask] < d) continue;
      rep(i, n)if(~mask & bit(i)){
        double pos = pos_i == n ? 0 : positions[pos_i] + speeds[pos_i] * d;
        double dist = abs(positions[i] + speeds[i] * d - pos);
        double next_time = d + dist / (s - abs(speeds[i]));
        i64 next_mask = mask;
        rep(j, n){
          if(positions[i] * positions[j] < 0) continue;
          if(abs(positions[j] + speeds[j] * next_time) - 1e-8 <=
             abs(positions[i] + speeds[i] * next_time)){
            next_mask |= bit(j);
          }
        }
        if(mp[i].count(next_mask) && mp[i][next_mask] < next_time){
          continue;
        }
        mp[i][next_mask] = next_time;
        q.push(make_tuple(next_time, i, next_mask));
      }
    }
    double best = 1e100;
    rep(i, n)if(mp[i].count(bit(n) - 1)) best = min(best, mp[i][bit(n) - 1]);
    printf("Case #%d: %0.20lf\n", (int)test_case + 1, best);
  }
}






















