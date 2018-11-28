#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int power (int x, int y) {
  int result = x;
  if (y == 0) return 1;
  for (int i = 1; i < y; i++) {
    result *= x;
  }
  return result;
}

int main() {
  freopen("input.txt","r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int x = 1; x <= t; x++) {
    int n;
    scanf("%d", &n);

    int insomnia = 1;
    vector<int> check(10, 0); // 0123456789
    for (int y = 1; y <= 1000000; y++) {
      int tmp = n * y;
      //printf("\n%d\n", tmp);

      int len = 1;
      int div;
      while(1) {
        div = tmp / 10;
        if(div == 0) break;
        len++;
        tmp = div;
      }
      //printf("len = %d\n", len);

      for (int i = 1; i <= len; i++) {
        tmp = ((n * y) / power(10, i-1)) % 10;
        //printf("%d ", tmp);
        check[tmp] = 1;
      }
      int check_end = 0;
      for (int i = 0; i < 10; i++) {
        if (check[i] == 1) check_end++;
      }
      if (check_end == 10) {
        printf("Case #%d: %d\n", x, n * y);
        insomnia = 0;
        break;
      }
    }
    if (insomnia == 1) printf("Case #%d: INSOMNIA\n", x);
  }
  return 0;
}
