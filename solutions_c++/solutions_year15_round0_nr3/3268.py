#include <stdio.h>
#include <algorithm>

#define ONE 1
#define I 2
#define J 3
#define K 4


char table[][4] = {
  { ONE,    I,     J,    K },
  {   I, -ONE,     K,   -J },
  {   J,   -K,  -ONE,    I },
  {   K,    J,    -I, -ONE },
};

char multiply(char a, char b) {
  char r = table[std::abs(a) - 1][std::abs(b) - 1];
  if ((a < 0 && b > 0) || (a > 0 && b < 0)) {
    r *= -1;
  }
  //printf("mul: %d * %d = %d\n", a, b, r);
  return r;
}

char divide(char a, char b) {
  return multiply(a, -b);
}

char pow(char a, int n) {
  char r = a;
  for (int i = 1; i < n; i++) {
    r = multiply(r, a);
  }
  return r;
}

char charToQuan(char a) {
  return (a - 'i') + 2;
}

bool solve(int l, int x, char str[]) {
  char _i = charToQuan(str[0]);
  char init_k = ONE;

  // printf("%s", str);
  // printf("\n");
  if (l * x < 3) return false;

  for (int i = 2; i < l * x; i++) {
    init_k = multiply(init_k, charToQuan(str[i % l]));
  }

  for (int i = 1; i < l * x; i++) {
    if (_i == I) {
      char _j = charToQuan(str[i % l]);
      // printf("     _J  %d\n", i);
      // printf("     _J  %c\n", str[i]);
      // printf("     _J  %d\n", _j);
      char _k = init_k;
      for (int k = i + 1; k < l * x; k++) {
        //         printf("%d %d\n", i, k);
        // //        fflush(stdin);
        //         printf("  _j:%d _k:%d\n", _j, _k);
        if (_j == J && _k == K) {
          // printf("%d %d\n", i, k);
          // char aa = ONE;
          // for (int a = 0; a < i; a++) {
          //   aa = multiply(aa, charToQuan(str[a % l]));
          // }
          // char bb = ONE;
          // for (int a = i; a < k; a++) {
          //   bb = multiply(bb, charToQuan(str[a % l]));
          // }
          // char cc = ONE;
          // for (int a = k; a < l*x; a++) {
          //   cc = multiply(cc, charToQuan(str[a % l]));
          // }
          // printf("%d %d %d", aa, bb, cc);
          // if(cc != 4) {
          //   printf("error");
          //   exit(0);
          // }
          return true;
        }
        _j = multiply(_j, charToQuan(str[k % l]));
        _k = divide(charToQuan(str[k % l]), _k);
                // printf("  _j:%d _k:%d\n", _j, _k);
      }
    }
    _i = multiply(_i, charToQuan(str[i % l]));
    init_k = divide(charToQuan(str[(i+1) % l]), init_k);
  }
  return false;
}

int main() {
  int t = 0;
  scanf("%d", &t);

  for (int i = 0; i < t; i++) {
    int l, x;
    char str[10001];
    scanf("%d %d", &l, &x);
    scanf("%s", str);
    bool result = solve(l, x, str);
    printf("Case #%d: %s\n", i + 1, result ? "YES" : "NO");
  }
  return 0;
}
