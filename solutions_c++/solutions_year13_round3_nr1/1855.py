#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef long long            int64;
typedef pair<double, double> pdd;
typedef pair<int,  int>      pii;
typedef pair<int64,int64>    pii64;
typedef unsigned long long   uint64;
typedef vector<double>       vd;
typedef vector<int64>        vi64;
typedef vector<int>          vi;
typedef vector<vi>           vvi;

const double eps = 1e-11;
const double pi  = acos(-1.0);
const int    p   = 1000000007;

int solve() {
  return 0;
}

inline bool is_cons(char c) {
    return c != 'a' && c != 'e' && c != 'u' && c!= 'i' &&
            c != 'o';
}

int main() {
    unsigned int nTests;
    cin >> nTests;

    for(unsigned int testNumber = 0; testNumber < nTests; testNumber++) {
      printf("Case #%d: ", testNumber + 1);

      string str;
      int n;
      cin >> str >> n;
      int len;
      len = str.length();

      int cons = 0;
      int count = 0;
      int last_good = -1;
      bool lg = false;

      for (int i = 0; i < len; ++i) {
          if (is_cons(str[i])) {
              ++cons;
          } else {
              cons = 0;
          }

          if (cons >= n) {
              last_good = i - n;
              lg = true;
          }
          if (lg) {
              count += last_good + 2;
          }
      }

      cout << count << endl;

    }
    return 0;
}
