#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdio>
#include <utility>
#include <iomanip>
#include <assert.h>
#define MP make_pair
#define PB push_back
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define RE(i, n) FOR(i, 1, n)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#ifdef LOCAL
#define debug(x) {cerr <<#x <<" = " <<x <<"\n"; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<"\n"; }}
#else
#define debug(x)
#define debugv(x)
#endif
#define make(type, x) type x; cin>>x;
#define make2(type, x, y) type x, y; cin>>x>>y;
#define make3(type, x, y, z) type x, y, z; cin>>x>>y>>z;
using namespace std;
typedef long long ll;
typedef long double LD;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef vector<int> VI;
typedef vector<ll> VLL;
typedef vector<PII> VPII;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.first << ", " << pair.second << ")";}

const int INF = 1e9;
const int N = 1e6 + 2;
VPII slo[N];
int dis[N];
int bui[N][2][2];
void AddEdge(int a, int b, int c) {
  slo[a].PB(MP(b, c));
  slo[b].PB(MP(a, c));
}
int Dijkstra(int source, int sink) {
  set<pair<int, int> > secik;
  dis[source] = 0;
  secik.insert(MP(source, 0));
  while (!secik.empty()) {
    auto p = *secik.begin();
    secik.erase(p);
    int act_v = p.second;
    int act_dis = p.first;
    //debug(act_v);
    for (auto v : slo[act_v]) {
      int nei = v.first;
      int c = v.second;
      if (act_dis + c < dis[nei]) {
        secik.erase(MP(dis[nei], nei));
        dis[nei] = act_dis + c;
        secik.insert(MP(dis[nei], nei));
      }
    }
  }
  return dis[sink];
}

int main() {
  // nie zapomnij o ll
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(10);
  double beg = 1.0 * clock() / CLOCKS_PER_SEC;
  
  make(int, tr);
  RE (tt, tr) {
    cout<<"Case #"<<tt<<": ";
    make3(int, w, h, b);
    for (int i = 0; i < N; i++) {
      slo[i].clear();
      dis[i] = INF;
    }
    int source = 0;
    int sink = b + 1;
    if (b == 0) {
      cout<<w<<endl;
      continue;
    }
    RE (i, b) {
      REP (j, 2) {
        REP (k, 2) {
          cin>>bui[i][k][j];
        }
      }
      RE (j, i - 1) {
        int diss = 0;
        REP (k, 2) {
          if (bui[i][k][1] < bui[j][k][0]) {
            maxi(diss, bui[j][k][0] - bui[i][k][1] - 1);
          } else {
            maxi(diss, max(0, bui[i][k][0] - bui[j][k][1] - 1));
          }
        }
        AddEdge(i, j, diss);
      }
      AddEdge(source, i, bui[i][0][0]);
      AddEdge(sink, i, w - bui[i][0][1] - 1);
    }
    
    
    
    cout<<Dijkstra(source, sink)<<endl;
  }
        
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  // nie zapomnij o ll
  return 0;
}
