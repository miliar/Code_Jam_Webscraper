#include <map>
#include <cstdio>

using namespace std;

const int all = (1 << 10) - 1;

int T;
map<int, int> mask;

int get_mask(int x) {
  if (mask.find(x) != mask.end()) return mask[x];
  else {
    int k = x;
    int m = 0;
    while (k) {
      m |= (1 << (k % 10));
      k /= 10;
    }
    return mask[x] = m;
  }
}

int solve(int x) {
  int X = x;
  int m = 0;
  while (m != all) {
    m |= get_mask(X);
    X += x;
  }
  return X - x;
}

int main (void) {
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    printf("Case #%d: ", i);

    int x;
    scanf("%d", &x);
    if (x == 0) printf("INSOMNIA\n");
    else printf("%d\n", solve(x));
  }
  return 0;
}
