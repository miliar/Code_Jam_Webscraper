#include <cstdio>
#include <algorithm>
using namespace std;

void solve(int c, int N) {
  if (N == 0) {
    printf("Case #%d: INSOMNIA\n", c);
    return;
  }
  int see[10] = {0};
  for (int i = N; ; i += N) {
    char str[20];
    sprintf(str, "%d", i);
    for (int j = 0; str[j] != '\0'; j++) {
      see[str[j]-'0'] = 1;
    }
    
    if (find(see, see + 10, 0) == see + 10) {
      printf("Case #%d: %d\n", c, i);
      return;
    }
  }

}

int main() {
  int T,N;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf("%d", &N);
    solve(i + 1, N);
  }
}
