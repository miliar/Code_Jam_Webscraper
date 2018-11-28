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







template <typename T> class PushRelabel
{
public:
  T maxFlow(int source, int target);
  void addEdge(int from, int dest, T capacity);
  
  PushRelabel(){}
  PushRelabel(int vertex_num) : vertex_num(vertex_num) {}

private:
  const int vertex_num;
  
  struct Node;
  struct CsrElement
  {
    Node *target;
    T capacity;
    CsrElement *reversed_edge;
    
    CsrElement(Node *target, T capacity, CsrElement *reversed_edge)
      : target(target), capacity(capacity), reversed_edge(reversed_edge) {}
  };
  CsrElement *csr;
  
  struct Node
  {
    int32_t height;
    T excess;
    CsrElement *first_csr_element;
    CsrElement *current_csr_element;
    
    Node *bucket_next;
    Node *bucket_prev;
  };
  
  struct Bucket
  {
    Node *top;
    Node *last;
  };
    
  struct Edge
  {
    int source;
    int target;
    T capacity;
    Edge(int source, int target, T capacity) : source(source), target(target), capacity(capacity) {}
  };
  vector<Edge> edges;
  
  void globalRelabeling(
      Node *&nodes, Node *&flow_source, Node *&flow_target, Node *&sentinel, 
      int &active_bucket_length, int &inactive_bucket_length, CsrElement *&csr, Bucket *&active_buckets, Bucket *&inactive_buckets);
};


template <typename T>
void PushRelabel<T>::globalRelabeling(
    Node *&nodes, Node *&flow_source, Node *&flow_target, Node *&sentinel, 
    int &active_bucket_length, int &inactive_bucket_length, CsrElement *&csr, Bucket *&active_buckets, Bucket *&inactive_buckets)
{
  for(Node *node = nodes; node != sentinel; ++node) node->height = vertex_num;
  for(int i = 0; i < vertex_num; ++i){
    active_buckets[i].top = active_buckets[i].last = sentinel;
    inactive_buckets[i].top = inactive_buckets[i].last = sentinel;
  }
  
  active_bucket_length = 0;
  inactive_bucket_length = 0;
  flow_target->height = 0;
  flow_source->height = 0;
  {
    Node *push_inactive_node = flow_target;
    Bucket *push_inactive_bucket = inactive_buckets + push_inactive_node->height;
    Node *push_inactive_current_top = push_inactive_bucket->top;
    push_inactive_node->bucket_prev = sentinel;
    push_inactive_node->bucket_next = push_inactive_current_top;
    push_inactive_current_top->bucket_prev = push_inactive_node;
    push_inactive_bucket->top = push_inactive_node;
    if(inactive_bucket_length < push_inactive_node->height) inactive_bucket_length = push_inactive_node->height;
  }

  
  for(int32_t height = 0; true; ++height){
    int next_height = height + 1;
    if(active_buckets[height].top == sentinel && inactive_buckets[height].top == sentinel) break;
    for(int32_t step = 0; step < 2; ++step){
      for(Node *node = (step == 0 ? active_buckets[height].top : inactive_buckets[height].top); node != sentinel; node = node->bucket_next){
        for(CsrElement *csr_ptr = node->first_csr_element, *end = (node + 1)->first_csr_element; csr_ptr != end; ++csr_ptr){
          if(csr_ptr->target->height != vertex_num) continue;
          if(csr_ptr->reversed_edge->capacity == 0) continue;
          csr_ptr->target->height = next_height;
          if(csr_ptr->target->excess == 0){ 
            Node *push_inactive_node = csr_ptr->target; 
            Bucket *push_inactive_bucket = inactive_buckets + push_inactive_node->height; 
            Node *push_inactive_current_top = push_inactive_bucket->top; 
            push_inactive_node->bucket_prev = sentinel; 
            push_inactive_node->bucket_next = push_inactive_current_top; 
            push_inactive_current_top->bucket_prev = push_inactive_node; 
            push_inactive_bucket->top = push_inactive_node; 
            if(inactive_bucket_length < push_inactive_node->height) inactive_bucket_length = push_inactive_node->height; 
          }else{
            Node *push_active_node = csr_ptr->target; \
            Bucket *push_active_bucket = active_buckets + push_active_node->height; \
            push_active_node->bucket_next = push_active_bucket->top; \
            push_active_bucket->top = push_active_node; \
            if(active_bucket_length < push_active_node->height) active_bucket_length = push_active_node->height; \
          }
        }
      }
    }
  }
  flow_source->height = vertex_num;
}


template <typename T>
T PushRelabel<T>::maxFlow(int flow_source_i, int flow_target_i)
{
  const int edge_num = edges.size();
  Node *nodes;
  Node *flow_source;
  Node *flow_target;
  Node *sentinel;
  Bucket *active_buckets;
  Bucket *inactive_buckets;
  int active_bucket_length;
  int inactive_bucket_length;

  // Construct a CSR.
  {
    // Use height as counter.
    nodes = (Node*)calloc(vertex_num + 1, sizeof(Node));
    for(int vertex = 0; vertex < vertex_num + 1; ++vertex) nodes[vertex].height = 0; 
    for(auto edge: edges){
      ++nodes[edge.source].height;
      ++nodes[edge.target].height;
    }

    csr = (CsrElement*)malloc(edge_num * 2 * sizeof(CsrElement));
    for(int32_t i = 0; i < vertex_num; ++i) nodes[i + 1].height += nodes[i].height;
    for(int32_t i = 0; i <= vertex_num; ++i) nodes[i].first_csr_element = csr + nodes[i].height;
    for(auto edge: edges){
      CsrElement *source_ptr = --nodes[edge.source].first_csr_element;
      CsrElement *target_ptr = --nodes[edge.target].first_csr_element;
      *source_ptr = CsrElement(nodes + edge.target, edge.capacity, target_ptr);
      *target_ptr = CsrElement(nodes + edge.source, 0, source_ptr);
    }
    for(int32_t i = 0; i <= vertex_num; ++i) nodes[i].current_csr_element = nodes[i].first_csr_element;
    
    flow_source = nodes + flow_source_i;
    flow_target = nodes + flow_target_i;
    
    sentinel = nodes + vertex_num;
    active_buckets = (Bucket*)malloc(vertex_num * sizeof(Bucket));
    inactive_buckets = (Bucket*)malloc(vertex_num * sizeof(Bucket));
    for(int i = 0; i < vertex_num; ++i){
      active_buckets[i].top = active_buckets[i].last = sentinel;
      inactive_buckets[i].top = inactive_buckets[i].last = sentinel;
    }
  }
  
  // Push flow from source.
  {
    flow_source->height = vertex_num;
    for(CsrElement *csr_ptr = flow_source->first_csr_element, *end = (flow_source + 1)->first_csr_element; csr_ptr != end; ++csr_ptr){
      csr_ptr->target->excess += csr_ptr->capacity;
    }
    // Dummy up.
    ++flow_target->excess;
  }
  
  // Main.
  {
  
    const int32_t global_relabeling_cycle = vertex_num * 6 + edge_num;
    globalRelabeling(nodes, flow_source, flow_target, sentinel, active_bucket_length, inactive_bucket_length, csr, active_buckets, inactive_buckets);
    
    for(int32_t step = 0; 0 < active_bucket_length;){
      // Global Relabeling.
      if(global_relabeling_cycle < step * 0.5){
        globalRelabeling(nodes, flow_source, flow_target, sentinel, active_bucket_length, inactive_bucket_length, csr, active_buckets, inactive_buckets);
        step = 0;
        continue;
      }
      
      // No active vertex.
      if(active_buckets[active_bucket_length].top == sentinel){
        --active_bucket_length;
        continue;
      }
      
      // Discharge.
      Node *node = active_buckets[active_bucket_length].top; 
      active_buckets[active_bucket_length].top = node->bucket_next;
      ASSERT(node != flow_source);
      ASSERT(node != flow_target);
      CsrElement *csr_ptr = node->current_csr_element;
      T local_excess = node->excess;
      int local_height = node->height;
      for(CsrElement *end = (node + 1)->first_csr_element; true; ++csr_ptr){
      
        // Relabel.
        if(csr_ptr == end){
          int32_t next_height = vertex_num - 1;
          step += 12;
          for(CsrElement *ptr = node->first_csr_element; ptr != end; ++ptr){
            step += 1;
            if(ptr->capacity == 0) continue;
            int32_t h = ptr->target->height;
            if(h < next_height){
              next_height = h;
              csr_ptr = ptr;
            }
          }
          
          
          // Gap relabeling.
          if(local_height != next_height + 1 && active_buckets[local_height].top == sentinel && inactive_buckets[local_height].top == sentinel){
            int max_height = (active_bucket_length < inactive_bucket_length) ? inactive_bucket_length : active_bucket_length;
            for(int height = local_height; height <= max_height; ++height){
              for(Node *node = inactive_buckets[height].top; node != sentinel; node = node->bucket_next){
                node->height = vertex_num;
              }
              inactive_buckets[height].top = sentinel;
            }
            active_bucket_length = local_height;
            inactive_bucket_length = local_height;

            local_height = vertex_num;
            flow_source->excess += local_excess;
            local_excess = 0;
            break;
          }
  
  
          local_height = next_height + 1;
          if(local_height == vertex_num){
            flow_source->excess += local_excess;
            local_excess = 0;
            break;
          }
        }
        
        
        // Push.
        if(0 < csr_ptr->capacity && csr_ptr->target->height < local_height){
          Node *push_target = csr_ptr->target; 
          T flow = (local_excess < csr_ptr->capacity) ? local_excess : csr_ptr->capacity; 
          if(push_target->excess == 0){ 
            Node *remove_prev = push_target->bucket_prev; 
            Node *remove_next = push_target->bucket_next; 
            remove_prev->bucket_next = remove_next;
            remove_next->bucket_prev = remove_prev;
            Bucket *remove_inactive_bucket = inactive_buckets + push_target->height;
            if(remove_inactive_bucket->top == push_target) remove_inactive_bucket->top = remove_next;
            
            Bucket *bucket = active_buckets + push_target->height; 
            push_target->bucket_next = bucket->top; 
            bucket->top = push_target; 
            if(active_bucket_length < push_target->height) active_bucket_length = push_target->height; 

          } 
          local_excess -= flow; 
          csr_ptr->capacity -= flow; 
          push_target->excess += flow; 
          csr_ptr->reversed_edge->capacity += flow; 
      
          if(local_excess == 0){
            node->height = local_height;
            Node *push_inactive_node = node;
            Bucket *push_inactive_bucket = inactive_buckets + push_inactive_node->height;
            Node *push_inactive_current_top = push_inactive_bucket->top;
            push_inactive_node->bucket_prev = sentinel;
            push_inactive_node->bucket_next = push_inactive_current_top;
            push_inactive_current_top->bucket_prev = push_inactive_node;
            push_inactive_bucket->top = push_inactive_node;
            if(inactive_bucket_length < push_inactive_node->height) inactive_bucket_length = push_inactive_node->height;

            break;
          }
        }
      }
      node->height = local_height;
      node->excess = local_excess;
      node->current_csr_element = csr_ptr;
    }
  }
    
  {
    // Dummy down.
    --flow_target->excess;
  }
  
  T answer = flow_target->excess;

  free(csr);
  free(nodes);
  free(active_buckets);
  free(inactive_buckets);

  return answer;
}

template <typename T>
inline void PushRelabel<T>::addEdge(int from, int dest, T capacity)
{
  if(from == dest) return;
  if(capacity == 0) return;
  edges.push_back(Edge(from, dest, capacity));
}





template <typename T> class MaxFlow
{
public:
  void addEdge(int from, int dest, T cap);
  T maxFlow(int flow_source, int flow_target);
  
  MaxFlow(int vertex_num);

private:

  class Edge
  {
  public:
    int target;
    int reversed_index;
    T capacity;
    Edge(int target, int reversed_index, T capacity)
    {
      this->target = target;
      this->reversed_index = reversed_index;
      this->capacity = capacity;
    }
  };

  int vertex_num;
  vector<int> levels;
  vector<int> iters;
  vector<vector<Edge>> edges;
  
  void bfs(int flow_source);
  T dfs(int vertex, int flow_target, T flow);
};

template <typename T>
inline void MaxFlow<T>::bfs(int flow_source)
{
  for(int vertex = 0; vertex < vertex_num; ++vertex) levels[vertex] = -1;
  levels[flow_source] = 0;
  std::queue<int> q;
  q.push(flow_source);
  while(!q.empty()){
    int vertex = q.front();
    q.pop();
    for(Edge &e: edges[vertex]){
      if(levels[e.target] != -1) continue;
      if(e.capacity == 0) continue;
      levels[e.target] = levels[vertex] + 1;
      q.push(e.target);
    }
  }
}

template <typename T>
inline T MaxFlow<T>::dfs(int vertex, int flow_target, T flow)
{
  if(vertex == flow_target) return flow;
  for(int &edge_index = iters[vertex]; edge_index < edges[vertex].size(); ++edge_index){
    Edge &e = edges[vertex][edge_index];
    if(levels[e.target] <= levels[vertex]) continue;
    if(e.capacity == 0) continue;
    T flowed = dfs(e.target, flow_target, flow == -1 ? e.capacity : std::min(flow, e.capacity));
    if(flowed == 0) continue;
    e.capacity -= flowed;
    edges[e.target][e.reversed_index].capacity += flowed;
    return flowed;
  }
  return 0;
}

template <typename T>
inline T MaxFlow<T>::maxFlow(int flow_source, int flow_target)
{
  T total = 0;
  while(true){
    bfs(flow_source);
    if(levels[flow_target] == -1) return total;
    for(int vertex = 0; vertex < vertex_num; ++vertex) iters[vertex] = 0;
    T flow;
    while(0 < (flow = dfs(flow_source, flow_target, -1))) total += flow;
  }
}

template <typename T>
inline MaxFlow<T>::MaxFlow(int vertex_num)
{
  this->vertex_num = vertex_num;
  edges = std::vector<std::vector<Edge>>(vertex_num);
  levels = std::vector<int>(vertex_num);
  iters = std::vector<int>(vertex_num);
}

template <typename T>
inline void MaxFlow<T>::addEdge(int from, int dest, T capacity)
{
  Edge e0(dest, edges[dest].size(), capacity);
  Edge e1(from, edges[from].size(),        0);
  edges[from].push_back(e0);
  edges[dest].push_back(e1);
}




int main()
{
  i64 T;
  cin >> T;
  rep(test_case, T){
    i64 n, m, k;
    cin >> m >> n >> k;
    
    vector<vector<i64>> v(k, vector<i64>(4, -1));
    rep(i, k)rep(j, 4) cin >> v[i][j];
    rep(i, k)rep(j, 4)if(j & 1) swap(v[i][j], v[i][j ^ 1]);
    
    /*
    vector<i64> coordinates;
    coordinates.push_back(-1);
    coordinates.push_back(bit(50));
    rep(i, k)rep(j, 4)if(~j & 1)for(i64 t = -1; t <= 1; ++t) coordinates.push_back(v[i][j] + t);
    sort(all(coordinates));
    coordinates.erase(unique(all(coordinates)), coordinates.end());
    
    map<i64, i64> mp;
    rep(i, sz(coordinates)) mp[coordinates[i]] = i;
    
    rep(i, k)rep(j, 4)if(~j & 1){ ASSERT(mp.count(v[i][j])); }
    rep(i, k)rep(j, 4)if(~j & 1) v[i][j] = mp[v[i][j]];
    
    n = sz(mp);
    */
    
    //DEBUG0();
    vector<vector<i64>> used(n + 1, vector<i64>(m + 1, 0));
    rep(i, k){
      used[v[i][0] + 0][v[i][1] + 0] += 1;
      used[v[i][2] + 1][v[i][1] + 0] -= 1;
      used[v[i][0] + 0][v[i][3] + 1] -= 1;
      used[v[i][2] + 1][v[i][3] + 1] += 1;
    }
    //DEBUG1(used);
    rep(i, n)rep(j, m + 1) used[i + 1][j] += used[i][j];
    rep(i, n + 1)rep(j, m) used[i][j + 1] += used[i][j];
    
    PushRelabel<int> flow(n * m * 2 + 2);
    i64 source = n * m * 2 + 0;
    i64 target = n * m * 2 + 1;
    
    #define getIndex(x, y) (((x) * m + (y)) * 2)
    rep(i, m)if(used[0][i] == 0) flow.addEdge(source, getIndex(0, i), 1);
    rep(i, m)if(used[n - 1][i] == 0) flow.addEdge(getIndex(n - 1, i) + 1, target, 1);
    
    //DEBUG1(used);
    rep(i, n)rep(j, m){
      if(used[i][j]) continue;
      //DEBUG2(i, j);
      flow.addEdge(getIndex(i, j), getIndex(i, j) + 1, 1);
      if(0 <= j - 1) flow.addEdge(getIndex(i, j) + 1, getIndex(i, j - 1), 1);
      if(j + 1 <  m) flow.addEdge(getIndex(i, j) + 1, getIndex(i, j + 1), 1);
      if(i + 1 <  n) flow.addEdge(getIndex(i, j) + 1, getIndex(i + 1, j), 1);
      if(0 <= i - 1) flow.addEdge(getIndex(i, j) + 1, getIndex(i - 1, j), 1);
    }
    
    cout << "Case #" << test_case + 1 << ": " << flow.maxFlow(source, target) << endl;
  }
  
}






