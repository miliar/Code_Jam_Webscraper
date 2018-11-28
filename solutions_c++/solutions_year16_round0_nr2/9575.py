#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MAXN = 1000;

int main(int argc, char** argv) {
  FILE* fin = fopen(argv[1], "r");
  FILE* fout = fopen(argv[2], "w");

  int t;
  fscanf(fin, "%d\n", &t);
  char pc[MAXN] = {0};
  for (int c = 1; c <= t; ++c) {
    fgets(pc, MAXN, fin);
    // printf("Case #%d: %s", c, pc);
    int r = strlen(pc) - 2;
    int res = 0;
    while (r >= 0) {
      int l = 0;
      while (pc[r] == '+')
        --r;
      if (r < 0)
        break;
      while (l < r && pc[l] == '+')
        ++l;
      if (l > 0) {
        for (int i = 0; i < l; ++i)
          pc[i] = '-';
        ++res;
      }
      // printf("%d\n", r);
      for (int i = 0; i <= r / 2; ++i) {
        char pci = pc[i];
        pc[i] = (pc[r - i] == '-') ? '+' : '-';
        if (r - i != i)
          pc[r - i] = (pci == '-') ? '+' : '-';
      }
      // printf("%s", pc);
      r -= l + 1;
      ++res;
    }
    fprintf(fout, "Case #%d: %d\n", c, res);
  }

  fclose(fin);
  fclose(fout);
  return 0;
}
