#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <iomanip>
#include <set>

#define INF 2000000000
#define MOD 1000000007

using namespace std;

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int testCount;
  cin >> testCount;
  for (int testNum = 1; testNum <= testCount; testNum++) {
    int pens[1010];
    int d;
    cin >> d;
    int maxi = 0;
    for (int i = 0; i < d; i++) {
      cin >> pens[i];
      maxi = max(pens[i], maxi);
    }
    int ans = INF;
    for (int i = 1; i <= maxi; i++) {
      int cur = i;
      for (int j = 0; j < d; j++) {
	cur += (pens[j] - 1) / i;
      }
      ans = min(ans, cur);
    }
    cout << "Case #" << testNum << ": " << ans << endl;
  }
  return 0;
}
