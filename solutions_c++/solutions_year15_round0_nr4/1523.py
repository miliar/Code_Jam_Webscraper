#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <set>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <ctime>
#include <algorithm>
#include <string>
#include <cstring>

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

bool CanChoose(int x, int r, int c) {
  if (r > c)
    swap(r, c);

  if (r * c % x != 0)
    return true;
  if (x > 6)
    return true;
  if (x < 3)
    return false;
  if (x == 3)
    return r == 1;
  if (x == 4)
    return r == 1 || r == 2;
  return false;
}

void solve() {
  int x = getInt();
  int r = getInt();
  int c = getInt();
  if (!CanChoose(x,r,c)) {
    printf("GABRIEL\n");
  } else {
    printf("RICHARD\n");
  }
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