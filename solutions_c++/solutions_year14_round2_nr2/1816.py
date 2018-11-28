#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <string>
#include <sstream>
#include <iomanip>
#include <iostream>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)

#ifdef WIN32  
#define LLD "%I64d"
#else 
#define LLD "%Ld"
#endif

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...)
#endif

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int inf = (int) 1e9;
const int maxn = (int) 1e5 + 1;
const double eps = (double) 1e-8;

int main() {
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    int a, b, k, ans = 0;
    scanf("%d%d%d", &a, &b, &k);
    for (int i = 0; i < a; i++) 
      for (int j = 0; j < b; j++)
        if ((i & j) < k) 
          ans++;
    printf("Case #%d: %d\n", tt, ans);
  }
    
  return 0;
}
