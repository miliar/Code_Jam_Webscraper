#include <iostream>
#include <cstdio>
using namespace std;

const int kMaxLength = 1000;

int process(int max_level, char* audience);

int main() {
  int cases;
  scanf("%d\n", &cases);
  for (int i = 1; i <= cases; i++) {
    int max_level;
    char audience[kMaxLength+1];
    scanf("%d %s\n", &max_level, audience);
    int ret = process(max_level, audience);
    printf("Case #%d: %d\n", i, ret);
  }

  return 0;
}

int process(int max_level, char* audience) {
  int need = 0;
  int current = 0;
  for (int i = 0; i <= max_level; i++) {
    if (current < i) {
      int diff = i - current;
      current += diff;
      need += diff;
    }
    int val = audience[i] - '0';
    current += val;
  }
  return need;
}
    
