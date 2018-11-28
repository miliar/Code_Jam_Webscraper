#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <ctime>
#include <algorithm>
#include <string>

#define fori(i,b,e) for (int i = (b); i < (e); i++)
#define mp make_pair
#define pb push_back
#define add insert
#define all(a) (a).begin(), (a).end()
#define elsif else if
#define sz(a) ((int)(a).size())

#ifdef DEBUG
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...)
#endif
#define next next_sadasddsa

using namespace std;

typedef long long int int64;
typedef long double ldb;
typedef pair<int,int> pii;

inline void printInt(int a) { printf("%d", a); }
inline void printDbl(double a) { printf("%.10lf", a); }
inline int getInt() { int res;  scanf("%d", &res);  return res; }
inline double getDbl() { double res;  scanf("%lf", &res);  return res; }

char s[2000];
int a[2000];

void solve() {
  int k;
  scanf("%d%s", &k, s);
  int n = strlen(s);
  int sum = 0;
  int add = 0;
  fori(i,0,n) {
    int v = s[i] - '0';
    if (v > 0) {
      if (sum < i) {
        add += i - sum;
        sum = i;
      }
      sum += v;
    }
  }
  printf("%d\n", add);
}

int main() {
#ifdef DEBUG
  freopen("in.txt", "rt", stdin);
  freopen("out.txt", "wt", stdout);
#endif
  srand(time(0));
  int T = getInt();
  fori(i,0,T) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}