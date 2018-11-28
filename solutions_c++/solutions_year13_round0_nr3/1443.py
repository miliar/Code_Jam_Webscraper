/* 
 * Author: Hakobyan Tigran
 */

#pragma comment(linker, "/STACK:60777216") 
#define printTime(begin, end) printf("%.3lf\n", (double)(end - begin) / (double)CLOCKS_PER_SEC) 


#include <string.h>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <functional>
#include <complex>
#include <iostream>
#include <fstream>
#include <sstream>
#include <bitset>
#include <limits>
#include <ctime>
#include <cassert>
#include <valarray>

using namespace std;

#define IN(a) freopen(a, "r", stdin)
#define OUT(a) freopen(a, "w", stdout)

#define mp(a, b) make_pair(a, b)
#define det(a, b, c, d) (a * d - c * b)
#define sbstr(s, i, j) s.substr(i, j - i + 1)

#define clear(dp) memset(dp, -1, sizeof(dp))
#define reset(arr) memset(arr, 0, sizeof(arr))

#define EPS 1e-9
#define PI acos(-1.0)
#define MOD 1000000007
#define IINF 1000000000
#define LINF 6000000000000000000LL

inline bool polindrome (int n) {
  int k = n;
  int total = 0;
  while(n) {
    total = total * 10 + n % 10;
    n /= 10;
  }
  return k == total;
}

inline bool square (int n) {
  int k = sqrt(n + .0);
  return k * k == n;
}

int solve (int A, int B) {
  int cnt = 0;
  for(int i = A; i <= B; ++i) {
    if(polindrome(i) && square(i) && polindrome(sqrt(i + .0))) {
      cout << i << " ";
    }
  }
  return cnt;
}

int main () {
#ifndef ONLINE_JUDGE
  IN("/home/tigran/Desktop/Debug/input.txt");
  OUT("/home/tigran/Desktop/Debug/output.txt");
#endif
  solve(1, 1000000);
  return 0;
}
