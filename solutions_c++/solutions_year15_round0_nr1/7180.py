#include <cstdio>
#include <cstdlib>
#include <bitset>

int main() {
  int numCases, sMax;
  int value;
  scanf("%d", &numCases);
  for (int i = 1; i <= numCases; ++i) {
    scanf("%d", &sMax);
    char* bitstr = (char*)malloc(sMax + 2);
    scanf("%s", bitstr);
    int def = 0, count = 0;
    for (int j = 0; j <= sMax; ++j) {
      value = bitstr[j] - '0';
      if (value != 0) {
        if (j > (count + def)) {
          def = j - count;
        }
      }
      count += value;
    }
    free(bitstr);
    printf("Case #%d: %d\n", i, def);
  }
  return 0;
}
