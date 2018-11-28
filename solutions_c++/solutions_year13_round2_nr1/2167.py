#include <cctype>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <string>
#include <vector>

using namespace std;

//
int a, n;
int m[100];  // moles

int main() {
  //

  int num_tests = 0;
  scanf("%d", &num_tests);
  for (int test = 1; test <= num_tests; ++test) {
    // input
    scanf("%d%d", &a, &n);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &m[i]);
    }
    sort(m, m + n);
    int r = 0;
    for (int i = 0; i < n; ++i) {
      int c = 0;
      int cmax = n - i;
      while (a < m[i] + 1) {
        // add a mote of size a - 1
        if (++c >= cmax) {
          break;
        }
        a += a - 1;
      }
      if (c >= cmax) {
        r += cmax;
        break;
      }
      r += c;
      a += m[i];
    }
    // output
    printf("Case #%d: %d\n", test, r);
  }
  return 0;
}
