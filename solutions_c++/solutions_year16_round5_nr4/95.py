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
#include <iostream>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

#define MAXN 222
string G[MAXN];
string B;

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(testcase, 1, T) {
    int N, L;
    scanf("%d%d", &N, &L);
    REP(i, N) cin >> G[i];
    cin >> B;
    bool ok = true;
    REP(i, N) if (B == G[i]) ok = false;
    if (!ok) {
      printf("Case #%d: IMPOSSIBLE\n", testcase);
      continue;
    }
    if (L == 1) {
      printf("Case #%d: 0 0?\n", testcase);
      continue;
    }

    string a, b;
    REP(i, L - 1) a.push_back('?');
    REP(i, 25) { b.push_back('1'); b.push_back('0'); }
    b.push_back('?');
    b.push_back('1');
    printf("Case #%d: %s %s\n", testcase, a.c_str(), b.c_str());
  }
  return 0;
}
