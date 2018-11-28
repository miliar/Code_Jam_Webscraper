#include <stdio.h>
#include <string.h>

int main(void) {
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    int s;
    scanf("%d", &s);
    int arr[s + 1];
    char str[s + 1];
    memset(str, 0, s + 1);
    memset(arr, 0, (s + 1) * sizeof(int));
    scanf("%s", str);
    for (int j = 0; j < s + 1; j++) {
      arr[j] = str[j] - '0';
    }
    int n = 0, t = 0;
    for (int j = 0; j < s + 1; j++) {
      if (j > t && arr[j]) {
        n += (j - t);
        t += n;
      }
      t += arr[j];
    }
    printf("Case #%d: %d\n", i + 1, n);
  }
  return 0;
}

