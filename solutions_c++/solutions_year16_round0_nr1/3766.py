#include<cstdio>

int countSheep(int N) {
  if (N == 0)
    return -1;
  bool digits[10] = {0};
  int count = 0;
  for (int i = 1; ; i++) {
    int x = N*i;
    while (x != 0) {
      int l = x%10;
      if (!digits[l]) {
        count++;
        if (count == 10)
          return N*i;
        digits[l] = true;
      }
      x /= 10;
    }
  }
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    int N;
    scanf("%d", &N);
    int res = countSheep(N);
    if (res < 0)
      printf("Case #%d: INSOMNIA\n", i);
    else
      printf("Case #%d: %d\n", i, res);
  }
}
