#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

inline int max(int a, int b) {return a>b? a:b;}
inline int min(int a, int b) {return a<b? a:b;}
int d, p[1005], maxCnt;

int solve() {
  int minVal = maxCnt, cnt;
  for (int i = 1; i < maxCnt ; i++) {
    cnt = 0;
    for (int j=0; j<d ; j++) {
      if (p[j] <= i) continue;
      cnt += p[j] / i + (p[j] % i > 0) - 1;
    }
    minVal = min(minVal , i + cnt);
  }
  return minVal;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i=0 ; i<t ; i++) {
    scanf("%d", &d);
    maxCnt = 0;
    for (int j=0 ; j<d; j++)
      scanf("%d", &p[j]), maxCnt = max(maxCnt, p[j]);
    printf("Case #%d: %d\n", i+1, solve());
  }
}