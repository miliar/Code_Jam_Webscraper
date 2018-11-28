#include<cstdio>
#include<set>

using namespace std;

int main() {
  int t;
  scanf("%d\n", &t);
  for(int i = 1; i <= t; ++i) {
    int n;
    int m;
    scanf("%d\n", &n);
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", i);
    } else {
      set<int> s;
      int k = n;
      for(;; k += n) {
        m = k;
        while (m > 0) {
            s.insert(m % 10);
            m /= 10;
        }
        if(s.size() == 10) {
          break;
        }
      }
      printf("Case #%d: %d\n", i, k);
    }
  }
  return 0;
}
