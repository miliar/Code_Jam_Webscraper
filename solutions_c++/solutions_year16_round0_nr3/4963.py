#include <stdio.h>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <string.h>

using namespace std;

void gen (int n, queue<string> & t, const string & prefix = "") {
  if (n == 0) {
    t.emplace(prefix);
    return;
  }
  gen(n - 1, t, prefix + '0');
  gen(n - 1, t, prefix + '1');
}


int main() {
  int T;
  scanf("%d", &T);

  for (int i = 1; i <= T; ++i) {
    printf("Case #%d:\n", i);

    int N, j;
    scanf("%d %d", &N, &j);

    queue <string> t;
    gen(N - 2, t);

    int m = 0;
    set<unsigned long long> vl;
    while (m < j) {
      string s = t.front();
      t.pop();
      s = "1" + s + "1";

      bool p = false;
      vector<unsigned long long> c(10);
      int o = 0;
      for (int k = 2; k <= 10 && p == false; ++k) {
        unsigned long long n = strtoull(s.c_str(), 0, k);
        p = true;

        unsigned long long root = sqrt(n);
        for (unsigned long long l = 2; l <= root; ++l) {
          if (n % l == 0) {
            unsigned long long a = l;
            unsigned long long b = n / l;

            if (vl.find(a) == vl.end()) {
              p = false;
              c[o++] = a;
              vl.emplace(a);
              break;
            } else if (a != b) {
              p = false;
              c[o++] = b;
              vl.emplace(b);
              break;
            }
          }
        }
      }

      if (p == false) {
        ++m;
        printf("%s %llu %llu %llu %llu %llu %llu %llu %llu %llu\n", s.c_str(), c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8]);
      }
    }
  }

  return 0;
}
