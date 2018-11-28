#include <cstdio>
#include <algorithm>
using namespace std;

const int maxN = 1e3 + 7;
char S[maxN];
int T, len, list[maxN];

bool cmp(int x, int y) {
  if (S[x] == S[y]) return x > y;
  return S[x] > S[y];
}

void cal(int l, int r) {
  if (l > r) return;

  for (int t = 0; t < len; t++)
    if (l <= list[t] && list[t] <= r) {
      printf("%c", S[list[t]]);
      cal(l, list[t] - 1);
      for (int i = list[t] + 1; i <= r; i++) printf("%c", S[i]);
      return;
    }
}

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("output.out", "w", stdout);

  scanf("%d", &T);
  for (int cou = 1; cou <= T; cou++) {
    scanf("%s", S), len = strlen(S);
    for (int i = 0; i < len; i++) list[i] = i;

    sort(list, list + len, cmp);

    printf("Case #%d: ", cou);
    cal(0, len - 1);
    printf("\n");
  }

  fclose(stdin);
  fclose(stdout);
}
