#include <cstdio>

long long h(long long b, int i) {
  long long x = 1, y = b;
  for (int j = 0; j < 15; j++)
    x *= b;
  x++;
  for (int j = 1; j < 1 << 14; j *= 2, y *= b)
    if (i & j)
      x += y;
  return x;
}

long long g(long long x) {
  for (long long z = 3; z <= x / z; z++)
    if (x % z == 0)
      return z;
  return -1;
}

bool f(int i) {
  long long a[11];
  for (int b = 2; b <= 10; b++)
    if ((a[b] = g(h(b, i))) == -1)
      return false;
  printf("%lld", h(10, i));
  for (int b = 2; b <= 10; b++)
    printf(" %lld", a[b]);
  printf("\n");
  return true;
}

int main() {
  for (int i = 0, j = 0; j < 50 && i < 1 << 14; i++)
    if (f(i))
      j++;
}
