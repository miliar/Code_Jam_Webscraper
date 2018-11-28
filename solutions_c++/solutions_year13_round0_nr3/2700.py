#include <cstdio>
#include <cmath>
using namespace std;

inline bool is_pa(unsigned long long x){
  unsigned long long y = x, ans = 0;
  while (y > 0) {
    ans *= 10;
    ans += y % 10;
    y /= 10;
  }
  return x == ans;
}

int main(){
  int t;
  unsigned long long a, b, ans;
  scanf("%d", &t);
  for (int c = 1; c <= t; ++ c){
    scanf("%llu%llu", &a, &b);
    ans = 0;
    unsigned long long ar = (unsigned long long)(sqrt(a));
    unsigned long long br = (unsigned long long)(sqrt(b));
    if (ar * ar < a) ++ ar;
    if ((br + 1) * (br + 1) <= b) ++ br;
    for (unsigned long long i = ar; i <= br; ++ i){
      if (is_pa(i) && is_pa(i * i)){
        ++ ans;
        printf("%llu %llu | ", i, i * i);
      }
    }
    putchar(10);
    printf("Case #%d: %d\n", c, ans);
  }
  
  return 0;
}
