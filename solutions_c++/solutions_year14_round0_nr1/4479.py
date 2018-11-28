#define PRETEST
#include <string>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <set>

using namespace std;

int main(void) {
#ifdef PRETEST
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  int T;
  int a[20];
  scanf("%d", &T);
  for (int z = 1; z <= T; ++z) {
    memset(a, 0, sizeof(a));
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= 4; ++i) {
      for (int j = 1; j <= 4; ++j) {
        int x;
        scanf("%d", &x);
        a[x] = i;
      }
    }
    int m;
    set<int> s;
    scanf("%d", &m);
    for (int i = 1; i <= 4; ++i) {
      for (int j = 1; j <= 4; ++j) {
        int x;
        scanf("%d", &x);
        if (i == m) {
          if (a[x] == n) {
            s.insert(x);
          }
        }
      }
    }
    printf("Case #%d: ", z);
    int size = s.size();
    if (size == 1) {
      printf("%d\n", *(s.begin()));
    } else if (size > 1) {
      printf("Bad magician!\n");
    } else {
      printf("Volunteer cheated!\n");
    }
  }
  return 0;
}
