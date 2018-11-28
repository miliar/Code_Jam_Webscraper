/* Written by Filip Hlasek 2016 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

#define MAXN 1111
int X[MAXN], Y[MAXN], Z[MAXN];
int Vx[MAXN], Vy[MAXN], Vz[MAXN];
int N, S;

/*
double Dist(int i, int j, double t) {
  double dx = (X[i] + t * Vx[i]) - (X[j] + t * Vx[j]);
  double dy = (Y[i] + t * Vy[i]) - (Y[j] + t * Vy[j]);
  double dz = (Z[i] + t * Vz[i]) - (Z[j] + t * Vz[j]);
  return sqrt(dx * dx + dy * dy + dz * dz);
}
*/

#define INF 1000000000000000000LL
double Start[MAXN][MAXN], End[MAXN][MAXN];

void calc_interval(int a, int b, double D) {
  /*
  Start[a][b] = 0; End[a][b] = INF;
  double l = 0, r = INF;
  REP(i, 100) {
    double m = (l + r) / 2;
  }
  */

  double dx = X[a] - X[b], vx = Vx[a] - Vx[b];
  double dy = Y[a] - Y[b], vy = Vy[a] - Vy[b];
  double dz = Z[a] - Z[b], vz = Vz[a] - Vz[b];

  if (Vx[a] == Vx[b] && Vy[a] == Vy[b] && Vz[a] == Vz[b]) {
    if (dx * dx + dy * dy + dz * dz <= D * D) {
      Start[a][b] = 0;
      End[a][b] = INF;
    }
    else Start[a][b] = End[a][b] = -1;
    return;
  }

  double A = vx * vx + vy * vy + vz * vz;
  double B = 2 * (vx * dx + vy * dy + vz * dz);
  double C = dx * dx + dy * dy + dz * dz - D * D;

  double disc = B * B - 4 * A * C;
  if (disc <= 0) { Start[a][b] = End[a][b] = -1; return; }

  Start[a][b] = (-B - sqrt(disc)) / (2 * A);
  End[a][b] =   (-B + sqrt(disc)) / (2 * A);
  if (End[a][b] < 0) { Start[a][b] = End[a][b] = -1; }
  else Start[a][b] = max(Start[a][b], 0.0);
}

double Dist[MAXN];
bool done[MAXN];
priority_queue< pair<double, int> > pq;

void add(double s, int v) {
  if (!done[v] && Dist[v] > s) {
    Dist[v] = s;
    pq.push(make_pair(-s, v));
  }
}

bool possible(double D) {
  // printf("D: %lf\n", D);
  REP(i, N) Dist[i] = INF;
  REP(i, N) done[i] = false;
  while (!pq.empty()) pq.pop();
  add(0, 0);
  while (!pq.empty()) {
    int v = pq.top().second; pq.pop();
    if (v == 1) { /* printf("Fine!\n"); */return true; }
    if (done[v]) continue;
    done[v] = true;
    double T = Dist[v] + S;
    // if (D < 3.53) printf("vertex: %d time: %lf\n", v, T);
    vector< pair<pair<double, double>, int> > nb;
    REP(i, N) if (i != v) {
      calc_interval(v, i, D);
      // if (D < 3.53) printf("v: %d i: %d start: %lf end: %lf\n", v, i, Start[v][i], End[v][i]);
      nb.push_back(make_pair(make_pair(Start[v][i], End[v][i]), i));
    }
    sort(nb.begin(), nb.end());
    REP(i, nb.size()) if (nb[i].first.first >= -0.5 && nb[i].first.first <= T) {
      // if (D < 3.53) printf("adding: (v = %d) (nb = %d) time: %lf\n", v, nb[i].second, nb[i].first.first);
      add(nb[i].first.first, nb[i].second);
      T = max(T, nb[i].first.second + S);
    }
  }
  return false;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(testcase, 1, T) {
    scanf("%d%d", &N, &S);
    REP(i, N) scanf("%d%d%d%d%d%d", X + i, Y + i, Z + i, Vx + i, Vy + i, Vz + i);

    double l = 0, r = INF;
    REP(i, 200) {
      if (r - l < 1e-6) break;
      double m = (l + r) / 2;
      if (possible(m)) r = m;
      else l = m;
    }

    // fprintf(stderr, "%d\n", testcase);
    printf("Case #%d: %.12lf\n", testcase, l);
  }
  return 0;
}
