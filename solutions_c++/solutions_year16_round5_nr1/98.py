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

char s[111111];

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(testcase, 1, T) {
    scanf("%s", s);
    int S = strlen(s);
    stack<char> ss;
    int ans = 0;
    REP(i, S) {
      if (!ss.empty() && ss.top() == s[i]) { ss.pop(); ans += 10; }
      else ss.push(s[i]);
    }
    printf("Case #%d: %d\n", testcase, ans + 5 * (int)ss.size() / 2);
  }
  return 0;
}
