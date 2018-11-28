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

string smallest(string s) {
  if (s.size() == 1) return s;
  string p1, p2;
  REP(i, s.size()) {
    if (i < s.size() / 2) p1.push_back(s[i]);
    else                  p2.push_back(s[i]);
  }
  p1 = smallest(p1); p2 = smallest(p2);
  if (p1 < p2) return p1 + p2;
  return p2 + p1;
}

string solve(int R, int P, int S) {
  int s = R + P + S;
  if (s == 1) {
    if (R) return "R";
    if (P) return "P";
    if (S) return "S";
  }
  if (2 * R > s || 2 * P > s || 2 * S > s) return "IMPOSSIBLE";
  string tmp = solve(s / 2 - P, s / 2 - S, s / 2 - R);
  if (tmp == "IMPOSSIBLE") return tmp;
  string ans = "";
  REP(i, tmp.size()) {
    if (tmp[i] == 'R') { ans.push_back('R'); ans.push_back('S'); }
    if (tmp[i] == 'P') { ans.push_back('P'); ans.push_back('R'); }
    if (tmp[i] == 'S') { ans.push_back('S'); ans.push_back('P'); }
  }
  return smallest(ans);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    int N, R, P, S;
    scanf("%d%d%d%d", &N, &R, &P, &S);
    printf("Case #%d: %s\n", t, solve(R, P, S).c_str());
  }
  return 0;
}
