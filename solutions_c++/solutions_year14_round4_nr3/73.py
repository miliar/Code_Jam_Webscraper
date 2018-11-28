#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define FOREACH(i, c) for(auto i = (c).begin(); i != (c).end(); ++i)
#define BIT(n, m) (((n) >> (m)) & 1)

typedef long long ll;

const ll inf = 1e15;
const ll mod = 1000 * 1000 * 1000 + 7;
const double eps = 1e-9;


struct Building{
  int x0, x1;
  int y0, y1;
  Building(){}
  Building(int x0, int y0, int x1, int y1) : x0(x0), x1(x1), y0(y0), y1(y1){}
};

int calc_dist(const Building &b0, const Building &b1){
  // cout << b0.x0 << " " << b0.x1 << " " << b0.y0 << " " << b0.y1 << endl; 
  // cout << b1.x0 << " " << b1.x1 << " " << b1.y0 << " " << b1.y1 << endl;
  assert(b0.x0 <= b0.x1);
  assert(b1.x0 <= b1.x1);
  int res = 0;
  res = max(res, - min(b0.x1, b1.x1) + max(b0.x0, b1.x0) - 1);
  res = max(res, - min(b0.y1, b1.y1) + max(b0.y0, b1.y0) - 1);
  return res;
};

void solve(){
  int W, H, B;
  cin >> W >> H >> B;
  vector<Building> buildings(B);

  REP(i, B){
    int x0, x1, y0, y1;
    cin >> x0 >> y0 >> x1 >> y1;
    buildings[i] = Building(x0, y0, x1, y1);
  }

  int s = buildings.size();
  int t = s + 1;
  int n = t + 1;
  
  buildings.push_back(Building(-1, -1, -1, H + 1));
  buildings.push_back(Building( W, -1,  W, H + 1));

  int dist[n];
  int adj[n][n];
  fill(dist, dist + n, 1e9);
  
  REP(i, n) REP(j, n){
    adj[i][j] = calc_dist(buildings[i], buildings[j]);
    // cout << i << " " << j << " " << adj[i][j] << endl;
  }

  typedef pair<int, int> PI;
  
  priority_queue<PI, vector<PI>, greater<PI> > que;
  que.push(make_pair(0, s));
  dist[s] = 0;

  int res = -1;
  while (!que.empty()){
    PI p = que.top(); que.pop();
    int v = p.second;
    int c = p.first;

    // cout << v << "  " << c << endl;
    if (v == t){
      res = c;
      break;
    }

    if (c > dist[v]) continue;

    REP(w, n){
      int nc = c + adj[v][w];
      if (nc < dist[w]){
        dist[w] = nc;
        que.push(make_pair(nc, w));
      }
    }
    
  }
  cout << res << endl;
}

int main(){
  int T;
  cin >> T;
  REP(t, T){
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
