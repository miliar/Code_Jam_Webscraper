#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int x[1010], y[1010], z[1010];
int vx[1010], vy[1010], vz[1010];

int par[1010];

vector<pair<double, pair<int, int> > > con;

int getpar(int x){
  if(x == par[x]) return x;
  return (par[x] = getpar(par[x]));
}

void mer(int x, int y){
  int px = getpar(x), py = getpar(y);
  if(px != py) par[px] = py;
}

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    int N, S; scanf("%d%d", &N, &S);
    for(int i = 0; i < N; i++){
      scanf("%d%d%d", &x[i], &y[i], &z[i]);
      scanf("%d%d%d", &vx[i], &vy[i], &vz[i]);
    }

    con.clear();

    for(int i = 0; i < N; i++){
      for(int j = i + 1; j < N; j++){
        int dx = x[i] - x[j];
        int dy = y[i] - y[j];
        int dz = z[i] - z[j];

        double d = sqrt(dx * dx + dy * dy + dz * dz);

        con.push_back(make_pair(d, make_pair(i, j)));
      }
    }

    sort(con.begin(), con.end());

    for(int i = 0; i < N; i++) par[i] = i;

    double ans = 1.0;

    for(pair<double, pair<int, int> > pp : con){
      mer(pp.second.first, pp.second.second);

      if(getpar(0) == getpar(1)){
        ans = pp.first; break;
      }
    }

    printf("Case #%d: %.7lf\n", tt, ans);
  }
  return 0;
}
