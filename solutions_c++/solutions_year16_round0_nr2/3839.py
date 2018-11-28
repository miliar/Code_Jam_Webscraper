#include<cstdio>
#include<cstring>
#include<cassert>

#define N 102

void flip(char str[N], int i) {
  if (str[i] == '+') str[i] = '-';
  else str[i] = '+';
}

void swap(char str[N], int i, int j) {
  char ch = str[i];
  str[i] = str[j];
  str[j] = ch;
}

int solve(char str[N]) {
  int len = strlen(str);
  int count = 0;
  int j = len-1;

  while (true) {
    while (j >= 0 && str[j] == '+') j--;
    if (j < 0)
      return count;
    assert (j >= 0 && str[j] == '-');
    int i = 0;
    while (i <= j && str[i] == '+') i++;
    if (i > j)
      return count;
    if (i > 0) {
      for (int k = i-1; k >= 0; k--)
        str[k] = '-';
      count++;
    }
    for (int k = 0; k <= j; k++)
      flip(str, k);
    for (int k = 0; k <= j/2; k++)
      swap(str, k, j-k);
    count++;
  }
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    char str[N] = {0};
    scanf("%s", str);
    int res = solve(str);
    printf("Case #%d: %d\n", i, res);
  }
  return 0;
}
