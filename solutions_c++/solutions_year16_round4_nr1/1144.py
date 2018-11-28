#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

typedef long long ll;
const string IMPOSSIBLE = "IMPOSSIBLE";

int T, N, R, P, S;

struct Res {
  string ans;
  int r, p, s;
};

void addType(Res& res, char type) {
  switch (type) {
    case 'R': ++res.r; break;
    case 'P': ++res.p; break;
    case 'S': ++res.s; break;
    default: assert(false);
  }
}

char worse(char type) {
  switch (type) {
    case 'R': return 'S';
    case 'P': return 'R';
    case 'S': return 'P';
    default: assert(false);
  }
}

void solve(size_t height, char top, Res& res, size_t offset) {
  if (height == 0) {
    res.ans[offset] = top;
    addType(res, top);
  } else {
    size_t len = 1 << (height - 1);
    solve(height - 1, top, res, offset);
    solve(height - 1, worse(top), res, offset + len);
    if (res.ans.substr(offset, len) > res.ans.substr(offset + len, len)) {
      REP(i,(int)len) {
        swap(res.ans[offset + i], res.ans[offset + len + i]);
      }
    }
  }
}

Res& solve(char top, Res& res) {
  res.r = res.p = res.s = 0;
  res.ans = string(1 << N, ' ');
  solve(N, top, res, 0);
  return res;
}

string consider(string&& s, const Res& r) {
  if (r.r != R || r.p != P || r.s != S) {
    return move(s);
  }
  if (s == IMPOSSIBLE || r.ans < s) {
    return move(r.ans);
  }
  return move(s);
}

string solve() {
  string s = IMPOSSIBLE;
  Res r;
  s = consider(move(s), solve('R', r));
  s = consider(move(s), solve('P', r));
  s = consider(move(s), solve('S', r));
  return s;
}

int main() {
  scanf("%d", &T);
  REP(t, T) {
    scanf("%d%d%d%d", &N, &R, &P, &S);
    printf("Case #%d: %s\n", t+1, solve().c_str());
  }
  return 0;
}
