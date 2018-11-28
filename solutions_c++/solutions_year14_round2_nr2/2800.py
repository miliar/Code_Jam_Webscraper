#include <algorithm>
#include <assert.h>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <numeric>
#include <limits>
#include <iomanip>
using namespace std;

#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define LL long long
#define LD long double
#define vi vector<int>
#define vl vector<LL>
#define vs vector<string>
#define vb vector<bool>
#define ii pair<int, int>
#define vii vector<ii>
#define SET(v, i) (v | (1 << i))
#define TEST(v, i) (v & (1 << i))
#define TOGGLE(v, i) (v ^ (1 << i))

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
//    LL a, b, k;
//    cin >> a >> b >> k;
//    LL ret = 0;
//    LL mna = min(a, k);
//    ret += mna * b;
//    if (a > k) {
//      ret += (a - k) * min(b, k);
//    }
//
//    printf("Case #%d: ", i);
//    cout << ret << endl;
    int a, b, k;
    cin >> a >> b >> k;
    int ret = 0;
    for (int j = 0; j < a; ++j) {
      for (int n = 0; n < b; ++n) {
        if ((n & j) < k)
          ++ret;
      }
    }

    printf("Case #%d: %d\n", i, ret);
  }
  return 0;
}
