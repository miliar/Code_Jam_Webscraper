#include<cstdio>
#include<deque>
#include<queue>
#include<stack>
#include<vector>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<bitset>
#include<list>
#include<set>
#include<map>

using namespace std;

int x = 0;

inline void use(int n) {
  if(n == 0) {
    x |= 1;
  }
  while(n > 0) {
    x |= (1 << (n % 10));
    n /= 10;
  }
}

int main() {
  freopen("alarge.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int test;
  scanf("%d", &test);
  for(int t = 1; t <= test; t++) {
    int n;
    scanf("%d", &n);
    if(n == 0) {
      printf("Case #%d: INSOMNIA\n", t);
    } else {
      x = 0;
      int z = n;
      while(true) {
        use(z);
        if(__builtin_popcount(x) == 10) {
          break;
        }
        z += n;
      }
      printf("Case #%d: %d\n", t, z);
    }
  }
}
