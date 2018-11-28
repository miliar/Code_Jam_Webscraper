#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <cstdarg>
#include <sys/time.h>

#ifdef _OPENMP
#include <omp.h>
#endif

using namespace std;

#define BEGIN_SOLVER struct solver {
#define END_SOLVER };

const int MAX_OUT = 10000;
const char *OUTPUT_FORMAT = "Case #%d: %s"; //"Case #%d:\n%s";

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair

typedef long long ll;

const double EPS = 1E-9;
const double INF = 1E12;

void init() {}



BEGIN_SOLVER ///////////////////////////////////////////////////////////////////////////////////////

int N, S;
double X[1010][3], V[1010][3];

void input() {
  scanf("%d%d", &N, &S);
  rep (i, N) {
    rep (d, 3) scanf("%lf", &X[i][d]);
    rep (d, 3) scanf("%lf", &V[i][d]);
  }
}

double sqr(double x) { return x * x; }

vector<double> quadratic(double a, double b, double c) {
  vector<double> res;
  if (fabs(a) < EPS) {
    if (fabs(b) > EPS) res.push_back(-c / b);
    else if (c < EPS) {
      return {-INF, INF}; // 恒等式
    }
  }
  else {
    double d = b * b - 4 * a * c;
    if (d > EPS) {
      if (b > 0) res.push_back((-b - sqrt(d)) / (2 * a));
      else res.push_back((-b + sqrt(d)) / (2 * a));
      res.push_back(c / a / res[0]);
    }
    else if (d > -EPS) res.push_back(-b / (2 * a));
  }
  return res;
}

vector<tuple<double, double, int>> adj[1010];

bool check(double L) {
  //
  // Graph construction
  //
  rep (i, N) adj[i].clear();

  rep (i, N) rep (j, i) {
    double a = 0.0, b = 0.0, c = 0.0;
    rep (d, 3) {
      double x = X[i][d] - X[j][d];
      double v = V[i][d] - V[j][d];
      a += sqr(v);
      b += 2 * x * v;
      c += sqr(x);
    }
    c -= sqr(L);
    auto ts = quadratic(a, b, c);
    // debug("? (%f %f %f) %d--%d: ", a, b, c, i, j); for (double t : ts) debug("%lf ", t); debug("\n");

    if (ts.size() == 2) {
      sort(all(ts));
      if (ts[1] > EPS) {
        for (double &t : ts) t = max(t, 0.0);
        adj[i].emplace_back(ts[0], ts[1], j);
        adj[j].emplace_back(ts[0], ts[1], i);
        // debug("! %d--%d, (%lf,%lf)\n", i, j, ts[0], ts[1]);
      }
    }
  }
  rep (i, N) sort(all(adj[i]));

  //
  // Search
  //
  multimap<pair<double, double>, int> que;
  que.emplace(make_pair(0.0, S), 0);

  double doneT[1010] = {};
  int doneI[1010] = {};

  while (!que.empty()) {
    double tlb = que.begin()->first.first;
    double tub = que.begin()->first.second;
    int v = que.begin()->second;
    que.erase(que.begin());
    if (tub < doneT[v] - EPS) continue;
    // debug("[%lf, %lf), %d\n", tlb, tub, v);

    if (v == 1) return true;

    for (int &i = doneI[v]; i < (int)adj[v].size(); ++i) {
      auto e = adj[v][i];
      double startT = get<0>(e), endT = get<1>(e);
      int toV = get<2>(e);
      if (tub < startT - EPS) break;  // too early

      if (endT < tlb - EPS) continue;  // useless edge...

      // myself
      tub = max(tub, endT + S);
      doneT[v] = max(doneT[v], tub);

      // traverse
      que.emplace(make_pair(max(tlb, startT), endT), toV);
    }
  }
  return false;
}

void solve() {
  double lb = 0.0, ub = 1E9;
  rep (iter, 100) {
    double md = (lb + ub) / 2.0;
    if (check(md)) ub = md;
    else lb = md;
  }
  printf("%.10f\n", lb);
}










////////////////////////////////////////////////////////////////////////////////////////////////////
// Template
////////////////////////////////////////////////////////////////////////////////////////////////////

char out_buf[MAX_OUT], *out_p;

solver() : out_p(NULL) {}



void printf(const char* format, ...)
  __attribute__((format(printf, 2, 3)))
{
  if (!out_p) out_p = out_buf;

  va_list args;
  va_start(args, format);
  out_p += vsnprintf(out_p, sizeof(char) * (MAX_OUT - (out_p - out_buf)), format, args);
  va_end(args);

  if (out_p - out_buf >= MAX_OUT) {
    fprintf(stderr, "error: Output Limit Exceeded !!\n");
    exit(EXIT_FAILURE);
  }
}

void puts(const char *s) {
  printf("%s\n", s);
}

void debug(const char* format, ...)
  __attribute__((format(printf, 2, 3)))
{
  va_list args;
  va_start(args, format);
  vfprintf(stderr, format, args);
  va_end(args);
  fflush(stderr);
}



END_SOLVER /////////////////////////////////////////////////////////////////////////////////////////



double sec() {
  struct timeval tv;
  gettimeofday(&tv, NULL);
  return tv.tv_sec + tv.tv_usec * 1e-6;
}



void print_status(int c, int C, double t0, double t1, int nth) {
  static const int L = 5;
  if (C > L && c % (C / L) != 0) return;
  else if (c - (nth - 1) / 2 <= 0) fprintf(stderr, "[ case: %d / %d ]\n", c, C);
  else {
    double t = sec();
    fprintf(stderr, "[ case: %d / %d | time: %.3f / %.3f ]\n",
            c, C, t - t0, (t1 - t0) + (t - t1) / (c - (nth - 1) / 2) * C);
  }
}



int main(int argc, char **argv) {
  bool parallel = false, status = false;
  for (int i = 1; i < argc; i++) {
    if (strcmp(argv[i], "-p") == 0) parallel = status = true;
    else if (strcmp(argv[i], "-s") == 0) status = true;
    else {
      fprintf(stderr, "usage: %s [-p] [-s]\n", argv[0]);
      exit(EXIT_FAILURE);
    }
  }

  double t0 = sec();
  init();
  double t1 = sec();
  if (status) fprintf(stderr, "[ init: %.3f ]\n", t1 - t0);

  string tmp;
  getline(cin, tmp);
  int C = atoi(tmp.c_str());

  if (!parallel) {
    if (status) fprintf(stderr, "[ mode: single thread ]\n");

    rep (c, C) {
      if (status) print_status(c, C, t0, t1, 1);

      solver *s = new solver();
      assert(s != NULL);
      s->input();
      s->solve();
      printf(OUTPUT_FORMAT, c + 1, s->out_buf);
      fflush(stdout);
      delete s;
    }
  }
  else {
#ifdef _OPENMP

    int nth = omp_get_max_threads();
    if (status) fprintf(stderr, "[ mode: parallel (%d) ]\n", nth);

    vector<string> out(C);
    vector<bool> done(C);
    int solve_c = 0, out_c = 0;
    omp_lock_t lock;
    omp_init_lock(&lock);

#pragma omp parallel for schedule(dynamic, 1)
    rep (c, C) {
      solver *s = new solver();
      assert(s != NULL);

      int my_c;
      omp_set_lock(&lock);
      {
        while (out_c < C && done[out_c]) {
          printf(OUTPUT_FORMAT, out_c + 1, out[out_c].c_str());
          fflush(stdout);
          out_c++;
        }
        if (status) print_status(solve_c, C, t0, t1, nth);
        my_c = solve_c++;
        s->input();
      }
      omp_unset_lock(&lock);

      s->solve();

      omp_set_lock(&lock);
      {
        out[my_c] = string(s->out_buf);
        done[my_c] = true;
      }
      omp_unset_lock(&lock);
      delete s;
    }

    omp_destroy_lock(&lock);

    while (out_c < C) {
      assert(done[out_c]);
      printf(OUTPUT_FORMAT, out_c + 1, out[out_c].c_str());
      out_c++;
    }

#else
    fprintf(stderr, "error: compile with -fopenmp !!\n");
#endif
  }

  exit(EXIT_SUCCESS);
}
