#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef vector<P> Vp;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef map<int, int> MAP;
typedef vector<MAP> Vmap;

const int INF = 1000000000;

int W, H, B;
Vi x0, Y0, x1, Y1;
Vi vx, vy;
MAP mx, my;
int nx, ny;

Mi mat;

int N;
Mi net;
Vmap flow;

inline int tonode(int x, int y, int z) {
  return 2*nx*y + 2*x + z;
}

inline void aresta(int a, int b, int f) {
  net[a].push_back(b);
  net[b].push_back(a);
  flow[a][b] += f;
}

int maxflow(int a, int b) {
  int maxf = 0;
  while (true) {
    cerr << "maxf=" << maxf << endl;
    Vi pare(N, -1);
    pare[a] = -2;
    queue<int> q;
    q.push(a);
    while (not q.empty() and pare[b] == -1) {
      int x = q.front();
      q.pop();
      for (int i = 0; i < int(net[x].size()); ++i) {
        int y = net[x][i];
        if (pare[y] == -1 and flow[x][y] > 0) {
          pare[y] = x;
          q.push(y);
        }
      }
    }
    if (pare[b] == -1) break;
    /*
    int f = INF;
    for (int x = b; x != a; x = pare[x])
      f = min(f, flow[pare[x]][x]);
    for (int x = b; x != a; x = pare[x]) {
      flow[pare[x]][x] -= f;
      flow[x][pare[x]] += f;
    }
    maxf += f;
    */
    for (int i = 0; i < int(net[b].size()); ++i) {
      int t = net[b][i];
      if (pare[t] == -1) continue;
      int f = flow[t][b];
      for (int x = t; x != a and f > 0; x = pare[x])
        f = min(f, flow[pare[x]][x]);
      if (f > 0) {
        for (int x = t; x != a; x = pare[x]) {
          flow[pare[x]][x] -= f;
          flow[x][pare[x]] += f;
        }
      }
      maxf += f;
    }
  }
  return maxf;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> W >> H >> B;
    x0 = Y0 = x1 = Y1 = Vi(B);
    set<int> sx, sy;
    sx.insert(0);
    sx.insert(W);
    sy.insert(0);
    sy.insert(H);
    for (int k = 0; k < B; ++k) {
      cin >> x0[k] >> Y0[k] >> x1[k] >> Y1[k];
      sx.insert(x0[k]);
      sx.insert(x1[k] + 1);
      sy.insert(Y0[k]);
      sy.insert(Y1[k] + 1);
    }
    vx = Vi(sx.begin(), sx.end());
    vy = Vi(sy.begin(), sy.end());
    mx.clear();
    my.clear();
    nx = vx.size();
    ny = vy.size();
    for (int i = 0; i < nx; ++i) mx[vx[i]] = i;
    for (int i = 0; i < ny; ++i) my[vy[i]] = i;
    
    mat = Mi(nx, Vi(ny, 0));
    for (int k = 0; k < B; ++k) {
      int xx0 = mx[x0[k]];
      int xx1 = mx[x1[k] + 1];
      int yy0 = my[Y0[k]];
      int yy1 = my[Y1[k] + 1];
      for (int i = xx0; i < xx1; ++i)
        for (int j = yy0; j < yy1; ++j)
          mat[i][j] = 1;
    }
        
//     for (int j = H - 1; j >= 0; --j) {
//       for (int i = 0; i < W; ++i)
//         cerr << mat[i][j];
//       cerr << endl;
//     }
    
    N = 2*nx*ny + 2;
    net = Mi(N);
    flow = Vmap(N);
    
    for (int i = 0; i < nx - 1; ++i)
      for (int j = 0; j < ny - 1; ++j) {
        if (mat[i][j] != 0) continue;
        
        int fx = vx[i + 1] - vx[i];
        int fy = vy[j + 1] - vy[j];
        
        net[tonode(i, j, 0)].push_back(tonode(i, j, 1));
        net[tonode(i, j, 1)].push_back(tonode(i, j, 0));
        flow[tonode(i, j, 0)][tonode(i, j, 1)] = max(fx, fy);
        
        if (i + 1 < nx - 1 and mat[i + 1][j] == 0) {
          net[tonode(i, j, 1)].push_back(tonode(i + 1, j, 0));
          net[tonode(i + 1, j, 0)].push_back(tonode(i, j, 1));
          flow[tonode(i, j, 1)][tonode(i + 1, j, 0)] = fy;
          
          net[tonode(i + 1, j, 1)].push_back(tonode(i, j, 0));
          net[tonode(i, j, 0)].push_back(tonode(i + 1, j, 1));
          flow[tonode(i + 1, j, 1)][tonode(i, j, 0)] = fy;
        }
        
        if (j + 1 < ny - 1 and mat[i][j + 1] == 0) {
          net[tonode(i, j, 1)].push_back(tonode(i, j + 1, 0));
          net[tonode(i, j + 1, 0)].push_back(tonode(i, j, 1));
          flow[tonode(i, j, 1)][tonode(i, j + 1, 0)] = fx;
          
          net[tonode(i, j + 1, 1)].push_back(tonode(i, j, 0));
          net[tonode(i, j, 0)].push_back(tonode(i, j + 1, 1));
          flow[tonode(i, j + 1, 1)][tonode(i, j, 0)] = fx;
        }
      }
    
    for (int i = 0; i < nx - 1; ++i)
      if (mat[i][0] == 0) {
        net[2*nx*ny].push_back(tonode(i, 0, 0));
        net[tonode(i, 0, 0)].push_back(2*nx*ny);
        flow[2*nx*ny][tonode(i, 0, 0)] = vx[i + 1] - vx[i];
      }
    
    for (int i = 0; i < nx - 1; ++i)
      if (mat[i][ny - 2] == 0) {
        net[tonode(i, ny - 2, 1)].push_back(2*nx*ny + 1);
        net[2*nx*ny + 1].push_back(tonode(i, ny - 2, 1));
        flow[tonode(i, ny - 2, 1)][2*nx*ny + 1] = vx[i + 1] - vx[i];
      }
    
    int res = maxflow(2*nx*ny, 2*nx*ny + 1);
    cerr << "Case #" << cas << ": " << res << endl;
    cout << "Case #" << cas << ": " << res << endl;
  }
}
