#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <complex> 
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;

#define s(n)          scanf("%d",&n)
#define sl(n)         scanf("%lld",&n)
#define sf(n)         scanf("%lf",&n)
#define fill(a,v)     memset(a, v, sizeof a)
#define bitcount      __builtin_popcount
#define all(x)        x.begin(), x.end()
#define pb(z)       push_back( z )
#define gcd           __gcd

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

int a[10007];
bool used[10007];
int main() {
  int t; s(t);
  for (int _t=1; _t <= t; _t++) {
    printf("Case #%d: ", _t);
    int n, cap;
    s(n); s(cap);
    for (int i=0; i < n; i++) s(a[i]);
    sort(a, a + n);
    // for (int i=0; i < n; i++) cout << a[i] << " "; cout << endl;
    memset(used, 0, sizeof used);
    int discs = 0;
    for (int i=n-1; i >= 0; i--) if (!used[i]) {
      int bestJ = -1;
      for (int j=i-1; j >= 0; j--) {
        if (!used[j]) {
          if (a[j] + a[i] <= cap) {
            bestJ = j; break;
          }
        }
      }
      used[i] = true;
      if (bestJ >= 0) {
        used[bestJ] = true;
      }
      // cout << a[i] << " and " << (bestJ >= 0 ? a[bestJ] : -1) << endl;
      discs++;
    }
    printf("%d\n", discs);
  }
}
