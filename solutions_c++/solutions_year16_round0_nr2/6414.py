#include <cstdio>
#include <cstring>
#include <fstream>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    char S[300];
    scanf("%s", S);

    int res = 1;
    int size = strlen(S);
    char curr = S[0];
    for (int j = 1; j < size; j++) {
      if (S[j] != curr) {
        curr = S[j];
        res++;
      }
    }
    if (S[size - 1] == '+') {
      res--;
    }

    printf("Case #%d: %d\n", i + 1, res);
  }

  return 0;
}
