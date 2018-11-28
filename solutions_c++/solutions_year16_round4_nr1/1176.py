#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

struct Res {
  int P, R, S;
  string res;
};

vector<Res> RR;

void gen(string s) {
  for (int i = 1; i < 14; ++i) {
    Res r;
    r.res = "";
    for (int j = 0; j < s.size(); ++j) {
      if (s[j] == 'P')
	r.res += "PR";
      if (s[j] == 'S')
	r.res += "PS";
      if (s[j] == 'R')
	r.res += "RS";
    }
    s = r.res;
    RR.PB(r);
  }
}

string ssort(string s) {
  if (s.size() == 1) {
    return s;
  }
  int N = s.size();
  string left = s.substr(0, N/2);
  string right = s.substr(N/2);
  left = ssort(left);
  right = ssort(right);
  if (left < right)
    return left + right;
  else
    return right + left;
}

void genAll() {
  gen("P");
  gen("R");
  gen("S");
  for (int i = 0; i < RR.size(); ++i) {
    RR[i].P = RR[i].R = RR[i].S = 0;
    for (int j = 0; j < RR[i].res.size(); ++j) {
      if (RR[i].res[j] == 'P')
	++RR[i].P;
      if (RR[i].res[j] == 'R')
	++RR[i].R;
      if (RR[i].res[j] == 'S')
	++RR[i].S;
    }
    RR[i].res = ssort(RR[i].res);
  }
}

int main()
{
  genAll();
  int T, t;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    int R, P, S, N;
    scanf("%d%d%d%d", &N, &R, &P, &S);

    string res = "Z";
    for (int i = 0; i < RR.size(); ++i)
      if (RR[i].R == R && RR[i].P == P && RR[i].S == S && RR[i].res < res)
	res = RR[i].res;
    if (res == "Z")
      res = "IMPOSSIBLE";

    printf("Case #%d: %s\n", t+1, res.c_str());
  }

  return 0;
};
