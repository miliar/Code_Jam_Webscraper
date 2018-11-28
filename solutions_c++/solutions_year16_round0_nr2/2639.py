#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
int plus[1000], minus[1000];

int main() {
  char s[1000];
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; ++tc) {
    scanf("%s", s);
    int l = strlen(s);
    plus[0] = minus[0] = 0;
    for (int i = 0; i < l; ++i) {
      plus[i+1] = ((s[i] == '+') ? plus[i] : minus[i] + 1);
      minus[i+1] = ((s[i] == '-') ? minus[i] : plus[i] + 1);
    }
     
    printf("Case #%d: %d\n", tc, plus[l]);
  }
  return 0;
}
