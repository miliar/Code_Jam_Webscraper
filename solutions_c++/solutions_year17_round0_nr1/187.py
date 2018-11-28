#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define TRACE(x) cerr << #x << " = " << x << endl
#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=(a); i<(b); i++)
#define _ << " " <<

typedef long long ll;
typedef pair<int, int> P;
#define X first
#define Y second

const int MAX = 1005;

char s[MAX];

int main()
{
  int brt;
  scanf("%d", &brt);

  FOR(br, 1, brt+1) {
    int k;
    scanf(" %s%d", s, &k);
    int da = 1;

    int n = (int) strlen(s);
    int cnt = 0;
    
    REP(i, n) {
      if (s[i] == '-') {
	if (i + k > n) da = 0;
	else {
	  FOR(j, i, i+k) s[j] ^= '+' ^ '-';	    
	  cnt++;
	}
      }
    }

    printf("Case #%d: ", br);
    if (!da) printf("IMPOSSIBLE\n");
    else printf("%d\n", cnt);
  }

  return 0;
}
