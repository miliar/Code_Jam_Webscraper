#define PRETEST
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <iomanip>
#include <sstream>
using namespace std;

#define INF 0x4f4f4f4f
#define FILL(a,b) memset(a,b,sizeof(a))
#define SQR(a) ((a) * (a))

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef map<string, int> msi;
typedef map<int, int> mii;

int main(int argc, char *argv[]) {
#ifdef PRETEST
  freopen("B-large.in", "r", stdin);
  freopen("out.txt", "w+", stdout);
#endif
  int T;
  scanf("%d", &T);
  for (int C = 1; C <= T; ++C) {
    int D;
    scanf("%d", &D);
    vector<int> p;
    int pp = -INF;
    for (int i = 0; i < D; ++i) {
      int x;
      scanf("%d", &x);
      p.push_back(x);
      pp = max(x, pp);
    }
    int ans = INF;
    for (int x = 1; x <= pp; ++x) {
      int sum = 0;
      for (int i = 0; i < D; ++i) {
        sum += (p[i] - 1) / x;
      }
      sum += x;
      if (sum < ans) {
        ans = sum;
      }
    }
    printf("Case #%d: %d\n", C, ans);
  }
  
  return 0;
}
