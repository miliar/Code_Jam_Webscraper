#include<cstdio>
#include<vector>
#include <cmath>

using namespace std;

int main() {
  int t;
  int count = 0;
  scanf("%d\n", &t);
  for(int i = 1; i <= t; ++i) {
    int n, ile;
    scanf("%d %d\n", &n, &ile);
    printf("Case #%d:\n", i);
    unsigned long long d = 16384;
    for(unsigned long long j = 0; j < 16384; ++j) {
      if (count == ile) {
        break;
      }
      vector<unsigned long long> v;
      vector<unsigned long long> cc;
      for (unsigned long long r = 2; r <= 10; r++) {
        cc.clear();
        unsigned long long t = 1;
        unsigned long long cj = j;
        unsigned long long w = r;
        for (unsigned long long l = 1; l < 15; l++, w *=r ) {
          cc.push_back(cj % 2);
          if (cj % 2 == 1) {
            t += w;
          }
          cj /= 2;
        }
        t += w;
        for (unsigned long long uu = 3; uu <= (unsigned long long)(sqrt((float) t)); uu += 2) {
          if (t % uu == 0) {
            v.push_back(uu);
            break;
          }
        }
      }
      if (v.size() == 9) {
        count ++;
        printf("1");
        for(int jkl = cc.size() -1; jkl >= 0; jkl--) {
          printf("%llu", cc[jkl]);
        }
        printf("1");
        for(int jkk = 0; jkk < 9; jkk++) {
          printf(" %llu", v[jkk]);
        }
        printf("\n");
      }
    }
  }
  return 0;
}
