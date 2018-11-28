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
#include <bitset>
#include <climits>

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
using bs30 = bitset<30>;



void init() {}


BEGIN_SOLVER ///////////////////////////////////////////////////////////////////////////////////////

int N;
bs30 mat[30];

void input() {
  scanf("%d", &N);
  rep (i, N) rep (j, N) {
    char c;
    scanf(" %c", &c);
    mat[i][j] = (c == '1');
  }
}

bool vis[30];
vector<int> grp;

void search(int v) {
  if (vis[v]) return;
  vis[v] = true;
  grp.emplace_back(v);

  rep (w, N) if ((mat[v] & mat[w]).count()) {
    search(w);
  }
}

int K;
pair<int, int> P[110];
bool usd[110];
int ans = 0;

void dfs(int a, int b, int i0, int cst) {
  if (cst >= ans) return;
  if (a > 0 && a == b) {
    dfs(0, 0, 0, cst);
    return;
  }
  if (a == 0 && b == 0 && (int)count(usd, usd + K, true) == K) {
    ans = cst;
    return;
  }

  // debug("HEY %d %d %d %d\n", a, b, i0, cst); rep (i, K) debug(" %d", usd[i]); debug("\n");

  for (int i = i0; i < K; ++i) {
    if (usd[i]) continue;
    if (i > 0 && !usd[i - 1] && P[i] == P[i - 1]) continue;

    // if (a >= b && P[i].first > P[i].second) continue;
    // if (a <  b && P[i].first < P[i].second) continue;

    usd[i] = true;
    dfs(a + P[i].first, b + P[i].second, i,
        cst + a * P[i].second + b * P[i].first);
    usd[i] = false;

    if (a == 0 && b == 0) break;
  }
}

void solve() {
  rep (v, N) vis[v] = false;

  vector<pair<vector<int>, bs30>> gs;
  int rem = 0;

  rep (v, N) {
    if (vis[v]) continue;

    grp.clear();
    search(v);

    bs30 b;
    for (int w : grp) b |= mat[w];
    if (b.count()) {
      gs.emplace_back(grp, b);
    } else {
      assert(grp.size() == 1);
      ++rem;
    }
  }

  vector<pair<int, int>> ps;
  int base = 0;
  for (auto g : gs) {
    const auto &vs = g.first;
    const auto &b = g.second;
    for (int v : vs) base += b.count() - mat[v].count();
    ps.emplace_back(g.first.size(), g.second.count());
  }
  rep (i, rem) ps.emplace_back(1, 0);
  {
    bs30 b;
    rep (v, N) b |= mat[v];
    int k = N - b.count();
    rep (i, k) ps.emplace_back(0, 1);
  }

  sort(all(ps));
  reverse(all(ps));
  K = ps.size();
  rep (i, K) P[i] = ps[i];

  rep (i, K) usd[i] = false;
  ans = INT_MAX;
  dfs(0, 0, 0, 0);
  printf("%d\n", base + ans);
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
