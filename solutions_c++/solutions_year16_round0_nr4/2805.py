#include<cstdio>
#include<set>

using namespace std;

int main() {
  int t;
  scanf("%d\n", &t);
  for(int i = 1; i <= t; ++i) {
    int k, c, s;
    scanf("%d %d %d\n", &k, &c, &s);
    printf("Case #%d:", i);
    for(int j = 1; j <= k; ++j) {
      printf(" %d", j);
    }
    printf("\n");
  }
  return 0;
}
