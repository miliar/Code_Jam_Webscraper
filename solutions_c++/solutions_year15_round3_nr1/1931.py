#include <stdio.h>

int max(int a, int b) {
  return a>b ? a : b;
}

int log(int x) {
  int count = 1;
  while(x != 1) {
    x/=2;
    ++count;
  }
  return count;
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int ic=1; ic<=T; ++ic) {
    int R, C, L;
    scanf("%d%d%d", &R, &C, &L);
    if (R != 1) {
      printf("wrong\n");
      break;
    }
    int result = 0;
    /*
    if (C % L) {
      result = C/L + log(C % L + 1);
      if (C > 2*L) {
        result = max(result, C/L - 1 + log(L));
      }
    } else {
      result = C == L ? 1 : C/L - 1 + log(L);
    }
    */
    result = C%L ? C/L + L : C/L + L - 1;
    printf("Case #%d: %d\n", ic, result);
  }

  return 0;
}
