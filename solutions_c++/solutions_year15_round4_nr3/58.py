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
  //DEBUG(from, dest, capacity);
  if(from == dest) return;
  if(capacity == 0) return;
  edges.push_back(Edge(from, dest, capacity));
}




int main()
{
  i64 T;
  cin >> T;
  rep(test_case, T){
    i64 n, word_n = 0;
    cin >> n;
    unordered_map<string, i64> mp;
    vector<string> lines(n);
    string dummy;
    getline(cin, dummy);
    rep(i, n) getline(cin, lines[i]);
    rep(i, n){
      stringstream ss(lines[i]);
      string word;
      while(ss >> word)if(mp.count(word) == 0) mp[word] = word_n++;
    }

    PushRelabel<int> flow(word_n * 2 + 2);
    const i64 source = word_n * 2 + 0;
    const i64 target = word_n * 2 + 1;
    rep(i, word_n){
      flow.addEdge(i * 2 + 0, i * 2 + 1, 1);
      flow.addEdge(i * 2 + 1, i * 2 + 0, 1);
    }
    rep(i, n){
      vector<i64> words;
      {
        string word;
        stringstream ss(lines[i]);
        while(ss >> word) words.push_back(mp[word]);
        rep(j, sz(words))rep(k, j){
          flow.addEdge(words[j] * 2 + 1, words[k] * 2, 1);
          flow.addEdge(words[k] * 2 + 1, words[j] * 2, 1);
        }
      }
      if(i == 0)for(auto word: words) flow.addEdge(source, word * 2 + 0, 1);
      if(i == 1)for(auto word: words) flow.addEdge(word * 2 + 1, target, 1);
    }
    printf("Case #%d: %d\n", (int)test_case + 1, flow.maxFlow(source, target));
  }
}

