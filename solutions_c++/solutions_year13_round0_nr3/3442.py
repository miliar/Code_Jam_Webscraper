#include <stdio.h>
#include <cmath>
#include <string>

bool isFair(long long x) {
  char buffer[100];
  int n = sprintf(buffer, "%lld", x);
  for (int i = 0; i < n/2 + 1; i++) {
    if (buffer[i] != buffer[n - i - 1]) return false;
  }
  return true;
}

long count(long long a, long long b) {
  long long sa = floor(sqrt(a));
  long long sb = ceil(sqrt(b));
  long result = 0;
  for (long long i = sa; i <= sb; i++) {
    long long t = i * i;
    if (t < a) continue;
    if (t > b) break;
    if (isFair(i) && isFair(t)) {
      result++;
    }
  }
  return result;
}

int main(int argc, char const *argv[])
{
  freopen("input.txt","r", stdin);
  //freopen("output.txt","w", stdout);
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    long long a, b;
    scanf("%lld%lld", &a, &b);    
    printf("Case #%d: %ld\n", i + 1, count(a, b));
  }
  return 0;
}