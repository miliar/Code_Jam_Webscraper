#include <stdio.h>
#include <string.h>

int solve(const int test_index, bool* S, const int length) {
  int num_happy = 0;
  for (int i = 0; i < length; ++i) {
    num_happy += S[i];
  }
  int num_flips = 0;
  if (num_happy == length)
    return num_flips;
  for (int i = length - 1; i >= 0; --i) {
    if (S[i] == false) {
      for (int j = 0; j <= i; ++j) {
        S[j] = !S[j];
      }
      break;
    }
  }
  num_flips += 1 + solve(test_index, S, length);
  return num_flips;
}


int main() {
  int T = 0;
  scanf("%d", &T);
  for (int i = 0; i < T; ++i) {
    char stack[100] = {0};
    scanf("%s", stack);
    bool* S = new bool[strlen(stack)]();
    for (int j = 0; j < strlen(stack); ++j) {
      S[j] = (stack[j] == '+'? true : false);
    }
    int num_flips = solve(i + 1, S, strlen(stack));
    printf("Case #%d: %d\n", i + 1, num_flips);
    delete[] S;
  }
  return 0;
}

