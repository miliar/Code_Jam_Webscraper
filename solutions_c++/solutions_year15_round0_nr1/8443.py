#include <stdio.h>

int main() {
  int count;
  char input[1002];
  scanf("%d", &count);
  for(int i = 0; i < count; ++i) {
    int length;
    scanf("%d", &length);
    scanf("%s", input);
    int stood = 0;
    int required = 0;
    for(int j = 0; j <= length; ++j) {
      int people = input[j] - '0';
      if(stood >= j) {
        stood += people;
      } else {
        required += j - stood;
        stood += j - stood;
        stood += people;
      }
    }
    printf("Case #%d: %d\n", i+1, required);
  }
}
