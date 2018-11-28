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



template <class T> class MinCostFlow
{
public:
  void addEdge(int from, int dest, int capacity, T cost);
  void terminateNegativeLoop(); // This requires all negative loops to be touched.
  T minCostFlow(int flow_source, int flow_target, int flow);

  MinCostFlow(int vertex_num);
  MinCostFlow(){}

private:
  class Edge
  {
  public:
    int dest;
    int capacity;
    int reversed_index;
    T cost;
    
    Edge(int dest, int capacity, int reversed_index, T cost)
    {
      this->dest = dest;
      this->capacity = capacity;
      this->reversed_index = reversed_index;
      this->cost = cost;
    }
  };
  T negative_loop_cost;
  int vertex_num;
  std::vector<std::vector<Edge>> edges;
};

template <class T>
inline MinCostFlow<T>::MinCostFlow(int vertex_num)
{
  this->vertex_num = vertex_num;
  negative_loop_cost = 0;
  edges = std::vector<std::vector<Edge>>(vertex_num);
}

template <class T>
inline void MinCostFlow<T>::addEdge(int from, int dest, int capacity, T cost)
{
  Edge e0(dest, capacity, edges[dest].size(),  cost);
  Edge e1(from,        0, edges[from].size(), -cost);
  edges[from].push_back(e0);
  edges[dest].push_back(e1);
}

template <class T>
inline T MinCostFlow<T>::minCostFlow(int flow_source, int flow_target, int flow)
{
  std::vector<std::tuple<T, bool>> costs(vertex_num);
  T total = 0;
  std::vector<int> pre_v(vertex_num);
  std::vector<int> pre_e(vertex_num);
  while(0 < flow){
    for(int vertex = 0; vertex < vertex_num; ++vertex) costs[vertex] = std::make_tuple(0, false);
    costs[flow_source] = std::make_tuple(0, true);
    for(bool updated = true; updated;){
      updated = false;
      for(int vertex = 0; vertex < vertex_num; ++vertex){
        if(!std::get<1>(costs[vertex])) continue;
        for(int edge_index = 0; edge_index < edges[vertex].size(); ++edge_index){
          Edge &e = edges[vertex][edge_index];
          if(e.capacity == 0) continue;
          if(std::get<1>(costs[e.dest]) && std::get<0>(costs[e.dest]) <= std::get<0>(costs[vertex]) + e.cost) continue;
          costs[e.dest] = std::make_tuple(std::get<0>(costs[vertex]) + e.cost, true);
          pre_v[e.dest] = vertex;
          pre_e[e.dest] = edge_index;
          updated = true;
        }
      }
    }
    if(!std::get<1>(costs[flow_target])) return bit(50);
    int minimum_flow = flow;
    for(int vertex = flow_target; vertex != flow_source; vertex = pre_v[vertex]){
      minimum_flow = std::min(minimum_flow, edges[pre_v[vertex]][pre_e[vertex]].capacity);
    }
    flow -= minimum_flow;
    
    total += minimum_flow * std::get<0>(costs[flow_target]);
    for(int vertex = flow_target; vertex != flow_source; vertex = pre_v[vertex]){
      Edge &e = edges[pre_v[vertex]][pre_e[vertex]];
      e.capacity -= minimum_flow;
      edges[vertex][e.reversed_index].capacity += minimum_flow;
    }
  }
  return total + negative_loop_cost;
}

template <class T> 
void MinCostFlow<T>::terminateNegativeLoop()
{
  std::vector<int> pre_v(vertex_num);
  std::vector<int> pre_e(vertex_num);
  std::vector<int> used(vertex_num);
  std::vector<T> distances(vertex_num);

  while(true){
    int vertex_in_loop = -1;
    for(int i = 0; i < vertex_num; i++) used[i] = distances[i] = 0;
    for(int step = 0; step <= vertex_num; ++step){
      bool updated=false;
      for(int vertex = 0; vertex < vertex_num; ++vertex){
        for(int edge_index = 0; edge_index < edges[vertex].size(); ++edge_index){
          Edge &e = edges[vertex][edge_index];
          if(e.capacity == 0 || distances[e.dest] <= distances[vertex] + e.cost) continue;
          distances[e.dest] = distances[vertex] + e.cost;
          pre_v[e.dest] = vertex;
          pre_e[e.dest] = edge_index;
          vertex_in_loop = e.dest;
          updated = true;
        }
      }
      if(!updated) return;
    }

    for(; !used[vertex_in_loop]; vertex_in_loop = pre_v[vertex_in_loop]) used[vertex_in_loop] = true;
    
    T total_cost = 0;
    int minimum_capacity = edges[pre_v[vertex_in_loop]][pre_e[vertex_in_loop]].capacity;
    int cur = vertex_in_loop;
    do{
      total_cost += edges[pre_v[cur]][pre_e[cur]].cost;
      minimum_capacity = std::min(minimum_capacity, edges[pre_v[cur]][pre_e[cur]].capacity);
      cur = pre_v[cur];
    }while(cur != vertex_in_loop);

    negative_loop_cost += total_cost * minimum_capacity;
    
    cur = vertex_in_loop;
    do{
      Edge &e = edges[pre_v[cur]][pre_e[cur]];
      e.capacity -= minimum_capacity;
      edges[cur][e.reversed_index].capacity += minimum_capacity;
      cur = pre_v[cur];
    }while(cur != vertex_in_loop);
  }
}



int main()
{
  i64 T;
  cin >> T;
  rep(test_case, T){
    i64 k;
    cin >> k;
    map<i64, vector<i64>> mp;
    vector<tuple<string, i64>> a(k);
    rep(i, k) cin >> get<0>(a[i]) >> get<1>(a[i]);
    rep(i, k)if(get<1>(a[i]) != 0) mp[get<1>(a[i])].push_back(i);
    
    vector<i64> is_inf(k, 0);
    vector<i64> bef_aft(k, -1);
    for(auto p: mp){
      vector<i64> v = p.second;
      i64 bef0 = -1, bef1 = -1;
      for(auto t: v){
        if(get<0>(a[t]) == "E"){
          if(bef0 != -1){
            is_inf[bef0] = true;
            bef_aft[bef0] = t;
          }
          bef0 = t;
        }else{
          if(bef1 != -1){
            is_inf[t] = true;
            bef_aft[t] = bef1;
          }
          bef1 = t;
        }
      }
    }
    
    MinCostFlow<i64> flow(k * 4 + 2);
    i64 source = k * 4 + 0;
    i64 target = k * 4 + 1;
    i64 total = 0;
    const i64 INF = 100000;
    rep(i, k){
      flow.addEdge(source, i * 4 + 0, 1, 0);
      flow.addEdge(i * 4 + 3, target, 1, 0);
      if(get<0>(a[i]) == "E"){
        total += INF;
        flow.addEdge(i * 4 + 0, i * 4 + 1, 1, -INF);
        if(!is_inf[i]) flow.addEdge(i * 4 + 1, target, 1, 1);
      }else{
        total += INF;
        flow.addEdge(i * 4 + 2, i * 4 + 3, 1, -INF);
        if(!is_inf[i]) flow.addEdge(source, i * 4 + 2, 1, 0);
      }
    }
    
    rep(aft, k)rep(bef, aft){
      if(get<0>(a[bef]) != "E") continue;
      if(get<0>(a[aft]) != "L") continue;
      if(bef_aft[bef] != -1 && bef_aft[bef] < aft) continue;
      if(bef_aft[aft] != -1 && bef < bef_aft[aft]) continue;
      i64 n0 = get<1>(a[bef]);
      i64 n1 = get<1>(a[aft]);
      if(n0 != 0 && n1 != 0 && n0 != n1) continue;
      flow.addEdge(bef * 4 + 1, aft * 4 + 2, 1, 0);
    }
    
    i64 ans = bit(50);
    rep(i, k){
      total += flow.minCostFlow(source, target, 1);
      ans = min(ans, total);
    }
    cout << "Case #" << test_case + 1 << ": ";
    if(ans < INF / 2) cout << ans << endl;
    else cout << "CRIME TIME" << endl;
  }
}






