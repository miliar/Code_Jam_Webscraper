#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR (i, 0, n)
#define _ << " _ " <<
#define TRACE(x) cerr << #x << " = " << x << endl
#define debug(...) fprintf(stderr, __VA_ARGS__)
//#define debug
//#define TRACE(x)

using namespace std;

typedef long long llint;

const int MAXN = 1010;
const int INF = 1e9;

char s[MAXN];
int n, k;

int main(void) {
  int t;
  scanf("%d",&t);
  REP(it, t) {
    scanf("%s %d",s,&k);
    n = (int)strlen(s);

    int sol = 0;
    REP(i, n)
      if (s[i] == '-') {
	if (i + k - 1 >= n)
	  sol = -INF;
	else {
	  FOR(j, i, i + k) s[j] = (s[j] == '-') ? '+' : '-';
	  ++sol;
	}
      }
    
    printf("Case #%d: ",it+1);
    if (sol < 0)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n",sol);
  }
  return 0;
}
