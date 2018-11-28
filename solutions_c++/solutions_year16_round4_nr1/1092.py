#include <bits/stdc++.h>

using namespace std;

template<class T> inline T sqr(const T& a) {
  return a * a;
}

template<class T> inline T middle(const T &a, const T &b) {
  return (a + b) / 2;
}

template<class T> inline int len(const T &c) {
  return static_cast<int>(c.size());
}

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 100;

struct Tr {
  int r, p, s;
  Tr () {}
  Tr(int ra, int pa, int sa) : r(ra), p(pa), s(sa) {}
};

Tr Sum(Tr &a, Tr &b) {
  return Tr(a.r + b.r, a.p + b.p, a.s + b.s);
}

bool Eq(Tr &a, Tr &b) {
  return a.r == b.r && a.p == b.p && a.s == b.s;
}

string dp[3][13];
Tr dc[3][13];

int IdOf(char c) {
  switch (c) {
    case 'R':
      return 0;
    case 'P':
      return 1;
    case 'S':
      return 2;
  }
  throw 1;
}

const string letters[3] = {string("R"), string("P"), string("S")};
const string branches[3] = {string("RS"), string("PR"), string("PS")};

const Tr singles[3] = {Tr(1, 0, 0), Tr(0, 1, 0), Tr(0, 0, 1)};

string &F(int h, int top) {
  string &tg = dp[top][h];
  Tr &tc = dc[top][h];
  if (len(tg) == 0) {
    if (h == 0) {
      tg = letters[top];
      tc = singles[top];
    } else {
      const string &next = branches[top];
      int lf_id = IdOf(next[0]);
      int rg_id = IdOf(next[1]);
      string &lf = F(h - 1, lf_id);
      string &rg = F(h - 1, rg_id);
      tc = Sum(dc[lf_id][h - 1], dc[rg_id][h - 1]);
      if (lf > rg) {
        tg = rg + lf;
      } else {
        tg = lf + rg;
      }
    }
  }
  return tg;
}

string Calc(int h, Tr tr) {
  string res;
  for (int i = 0; i < 3; ++i) {
    string &cur = F(h, i);
    if (Eq(dc[i][h], tr)) {
      if (len(res) == 0 || res > cur) {
        res = cur;
      }
    }
  }
  if (len(res)) {
    return res;
  }
  return "IMPOSSIBLE";
}

void HandleCase() {
  int n, rs, ps, ss;
  scanf("%d", &n);
  scanf("%d%d%d", &rs, &ps, &ss);
  Tr tr(rs, ps, ss);
  printf("%s\n", Calc(n, tr).c_str());
}

int main() {
  int tests;
  scanf("%d", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d: ", test);
    HandleCase();
  }
  return 0;
}
