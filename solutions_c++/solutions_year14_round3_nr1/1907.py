#include <cstdio>
#include <vector>

using namespace std;

const char* INPUT_FILE = "A-small-attempt0.in";
const char* OUTPUT_FILE = "a.out";

int calc(int, int);

int main() {
  int test_cases;
  FILE* fin = fopen(INPUT_FILE, "r");
  FILE* fout = fopen(OUTPUT_FILE, "w");

  fscanf(fin, "%d\n", &test_cases);
  for (int round = 1; round <= test_cases; round++) {
    int a, b;
    fscanf(fin, "%d/%d\n", &a, &b);
    int result = calc(a, b);

    if (result == -1)
      fprintf(fout, "Case #%d: impossible\n", round);
    else
      fprintf(fout, "Case #%d: %d\n", round, result);
  }
  fclose(fin);
  fclose(fout);

  return 0;
}

int calc(int a, int b) {
  if ((b & (b-1)) != 0)
    return -1;

  for (int i = 0; i < 40; i++) {
    //printf("%d %d\n", a, b);
    if (b == 1 && a == 1)
      return i;
    if (a > b) {
      if (a > b * 2)
        return -1;
      return i;
    }
    b /= 2;
  }

  return -1;
}

