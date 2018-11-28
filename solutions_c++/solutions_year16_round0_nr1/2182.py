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

int solve(int N) {
  set<int> s;
  long long M = N;
  while (s.size() < 10) {
    int m = M;
    while (m) {
      s.insert(m % 10);
      m /= 10;
    }
    // printf("m: %d size: %d\n", M, (int)s.size());
    M += N;
  }
  return (M - N);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  /*
  int m = 0;
  FOR(n, 1, 1000000) {
    int mm = solve(n);
    if (mm > m) {
      m = mm;
      printf("m: %d n: %d\n", m, n); 
    }
  }
  */
  FOR(t, 1, T) {
    printf("Case #%d: ", t);
    int N;
    scanf("%d", &N);
    if (!N) printf("INSOMNIA\n");
    else printf("%d\n", solve(N));
  }
  return 0;
}
