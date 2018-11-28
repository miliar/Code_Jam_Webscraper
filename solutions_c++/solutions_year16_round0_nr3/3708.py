#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

long long find_factor(long long N) {
  for (long long i = 2; i * i <= N; i++) {
    if (N % i == 0)
      return i;
  }
  return 0;
}

long long convert10tob(long long N, int b) {
  if (N == 0) return 0;
  long long x = N % b;
  N /= b;
  return (x + convert10tob(N, b) * 10LL);
}

long long interpret(long long N, int b) {
  long long ret = 0;
  long long x = 1;
  while (N > 0) {
    ret += (N % 10) * x; 
    N /= 10;
    x *= b;
  }
  return ret;
}

vector<long long> test(long long n) {
  vector<long long> v;
  int i;
  for (i = 2; i <= 10; i++) {
    long long x = interpret(n, i);    
    // printf("%lld:%d:%lld\n", n, i, x);
    long long factor = find_factor(x);
    if (factor) {
      v.push_back(factor);
    } else {
      break;
    }
  }

  if (i == 11) {
    return v;
  } else {
    return vector<long long>();
  }
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    int N, J;
    scanf("%d %d", &N, &J);

    printf("Case #%d:\n", t);
    for (int i = 0; i < (1 << (N - 2)); i++) {
      long long number = convert10tob((i << 1) + (1<<(N-1)) + 1, 2);
      vector<long long> res = test(number);
      if (!res.empty()) {
        printf("%lld ", number);
        for (int j = 0; j < res.size(); j++)
          printf("%lld ", res[j]);
        puts("");
        J -= 1;
        if (!J) break;
      }
    }
  }
  
  return 0;
}
