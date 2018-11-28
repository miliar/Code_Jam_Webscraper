#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <string>
#include <vector>

using namespace std;

//#define debug(args...) fprintf(stderr, args)
#define debug(...)

//
int end[500000];
int len[500000];

int main() {
  //

  int num_tests = 0;
  scanf("%d\n", &num_tests);
  for (int test = 1; test <= num_tests; ++test) {
    // input
    int ch = 0;
    int k = 0;
    int l = 0;
    end[k] = len[k] = 0;
    while ((ch = getchar()) != ' ') {
      if (ch < 'a' || ch > 'z')
        continue;
      ++l;
      if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
        if (len[k] > 0) {
          ++k;
          end[k] = len[k] = 0;
        }
      }
      else {
        end[k] = l;
        ++len[k];
      }
    }
    if (len[k] > 0)
      ++k;
    debug("k=%d\n", k);
    int n = 0;
    scanf("%d\n", &n);
    long long n_value = 0;
    int last = -1;
    for (int i = 0; i < k; ++i) {
      if (len[i] < n)
        continue;
      debug("i=%d, e=%d, l=%d\n", i, end[i], len[i]);
      int s = len[i] - n + 1;
      int a = end[i] * s - s * (s - 1) / 2 - n * s + s;
      n_value += a;
      debug("s=%d, a=%d, n_value=%lld\n", s, a, n_value);
      if (last >= 0) {
        int b = end[last] - n + 1;
        int r = end[i] - len[i] -b;
        n_value += b * r;
        debug("b=%d, r=%d, n_value=%lld\n", b, r, n_value);
      }
      last = i;
    }
    if (last >= 0) {
      int b = end[last] - n + 1;
      int r = l - end[last];
      n_value += b * r;
    }
    // output
    printf("Case #%d: %lld\n", test, n_value);
  }
  return 0;
}
