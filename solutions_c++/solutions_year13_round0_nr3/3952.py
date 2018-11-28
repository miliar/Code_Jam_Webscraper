#include <stdio.h>
#include <math.h>
#include <string.h>

bool isPalindrome(long long unsigned int num) {
  char chars[50];
  sprintf(chars, "%llu", num);
  int len = strlen(chars);
  for (int i = 0; i <= len / 2; i++) {
    if (chars[i] != chars[len - 1 - i]) {
      return false;
    }
  }
  return true;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 0; t < T; t++) {
    long long unsigned int A, B;
    scanf("%llu%llu", &A, &B);

    unsigned int count = 0;
    long long unsigned int i = sqrt(A);
    if (i*i < A) {
      i++;
    }
    for (; i*i <= B; i++) {
      if (isPalindrome(i) && isPalindrome(i*i)) {
        count++;
      }
    }

    printf("Case #%d: %u\n", t + 1, count);
  }
}
