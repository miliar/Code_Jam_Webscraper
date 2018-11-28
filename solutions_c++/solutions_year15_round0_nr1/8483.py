#include <cstdio>

#define SMAX 1100

using namespace std;

void solve();

int main(int argc, char *argv[]) {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}

void solve() {
  char audience[SMAX];
  int max, n;
  int standing=0, friends=0;
  scanf("%d", &max);
  scanf("%s", audience);
  for (int i = 0; i <= max; i++) {
    n = int(audience[i] - '0');
    if (standing < i) {
      friends += i - standing;
      standing = i;
    }
    standing += n;
  }
  printf("%d\n", friends);
}
