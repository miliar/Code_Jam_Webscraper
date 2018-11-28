#include <bits/stdc++.h>

using namespace std;

typedef long double ld;
typedef long long ll;

long long rdtsc() {
  long long tmp;
  asm("rdtsc" : "=A"(tmp));
  return tmp;
}

inline int myrand() {
#ifdef _WIN32
  return abs((rand() << 15) ^ rand());
#else
  return rand();
#endif
}

inline int rnd(int x) {
  return myrand() % x;
}

#ifdef LOCAL
#define LLD "%lld"
#else
#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif
#endif

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stdout)
#else
#define eprintf(...) ;
#endif

#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())
#define TASK "text"

void precalc() {
}

int n;
int p, r, s;

bool read() {
  if (scanf("%d%d%d%d", &n, &r, &p, &s) < 4) {
    return false;
  }
  assert(p + r + s == (1 << n));
  return true;
}

string getans(char ch, int it, int &p, int &r, int &s) {
  if (it == 0) {
    p = r = s = 0;
    if (ch == 'P') {
      p = 1;
    } else if (ch == 'S') {
      s = 1;
    } else {
      assert(ch == 'R');
      r = 1;
    }
    string res = "";
    res += ch;
    return res;
  }

  int cp[2], cr[2], cs[2];
  string sl = "", sr = "";
  if (ch == 'S') {
    sl = getans('P', it - 1, cp[0], cr[0], cs[0]);
    sr = getans('S', it - 1, cp[1], cr[1], cs[1]);
  } else if (ch == 'P') {
    sl = getans('P', it - 1, cp[0], cr[0], cs[0]);
    sr = getans('R', it - 1, cp[1], cr[1], cs[1]);
  } else {
    assert(ch == 'R');
    sl = getans('S', it - 1, cp[0], cr[0], cs[0]);
    sr = getans('R', it - 1, cp[1], cr[1], cs[1]);
  }

  p = cp[0] + cp[1];
  r = cr[0] + cr[1];
  s = cs[0] + cs[1];

//  eprintf("%c, %d: %s, %s\n", ch, it, sl.c_str(), sr.c_str());

  return min(sl + sr, sr + sl);
}

void solve() {
  string ans = "";
  {
    int cp = 0, cr = 0, cs = 0;
    string cur = getans('P', n, cp, cr, cs);
    if (cp == p && cr == r && cs == s && (ans == "" || cur < ans)) {
      ans = cur;
    }
  }
  {
    int cp = 0, cr = 0, cs = 0;
    string cur = getans('R', n, cp, cr, cs);
    if (cp == p && cr == r && cs == s && (ans == "" || cur < ans)) {
      ans = cur;
    }
  }
  {
    int cp = 0, cr = 0, cs = 0;
    string cur = getans('S', n, cp, cr, cs);
    if (cp == p && cr == r && cs == s && (ans == "" || cur < ans)) {
      ans = cur;
    }
  }

  if (ans == "") {
    printf("IMPOSSIBLE\n");
  } else {
    printf("%s\n", ans.c_str());
  }
}

int main() {
  srand(rdtsc());
  precalc();
#ifdef LOCAL 
  assert(freopen(TASK".out", "w", stdout));
  assert(freopen(TASK".in", "r", stdin));
#endif

  int T;
  scanf("%d", &T);
  for (int tn = 1; tn <= T; ++tn) {
    assert(read());
    printf("Case #%d: ", tn);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}


