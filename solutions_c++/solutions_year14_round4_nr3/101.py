#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

int x0[1024], y0[1024], x1[1024], y1[1024];
int d[1024][1024];

long long dist[1024];
bool visited[1024];

int f(int a, int b) {
  int dx, dy;
  int x = x0[a] - x1[b];
  int xx = x1[a] - x0[b];
  if ((x <= 0 && xx >= 0) || (x >= 0 && xx <= 0)) dx = 0;
  else dx = min(abs(x), abs(xx)) - 1;
  int y = y0[a] - y1[b];
  int yy = y1[a] - y0[b];
  if ((y <= 0 && yy >= 0) || (y >= 0 && yy <= 0)) dy = 0;
  else dy = min(abs(y), abs(yy)) - 1;
  return max(dx, dy);
}

int main() {
  int t;
  cin >> t;
  REP(cas,t) {
    REP(i,1024) {
      dist[i] = 10000000000000000LL;
      visited[i] = false;
    }
    dist[0] = 0;
    int w, h, b;
    cin >> w >> h >> b;
    x0[0] = -1; y0[0] = 0; x1[0] = -1; y1[0] = h;
    x0[1] = w; y0[1] = 0; x1[1] = w; y1[1] = h;
    REP(i,b) cin >> x0[i+2] >> y0[i+2] >> x1[i+2] >> y1[i+2];
    REP(i,b+2) REP(j,b+2) d[i][j] = f(i,j);
    REP(i,b+2) {
      int v = 0;
      long long dis = 10000000000000000LL;
      REP(j,b+2) if (!visited[j] && dist[j] < dis) {
        dis = dist[j];
        v = j;
      }
      visited[v] = true;
      REP(j,b+2) dist[j] = min(dist[j], dist[v] + d[v][j]);
    }
    //REP(i,b+2) cout << dist[i] << " "; cout << endl;
    printf("Case #%d: %lld\n", cas+1, dist[1]);
  }
  return 0;
}
