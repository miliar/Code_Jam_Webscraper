#include <cstdio>

using namespace std;

int T;
int n, sum, add;
char a[2000];

int main(void) {
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    scanf("%d", &n);
    scanf("%s", a);
    sum = a[0] - '0';
    add = 0;
    for(int i = 1; i <= n; i++) {
      if(sum < i) {
        add += i - sum;
        sum = i;
      }
      sum += a[i] - '0';
    }
    printf("Case #%d: %d\n", t, add);
  }
  return 0;
}
