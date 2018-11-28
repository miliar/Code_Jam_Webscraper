#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
  FILE *fin = fopen("bl.in", "r");
  FILE *fout = fopen("bl.out", "w");
  int testn = 0;
  fscanf(fin, "%d", &testn);
  for (int t = 1; t <= testn; ++t) {
    fprintf(fout, "Case #%d: ", t);
    char pancakes[105];
    fscanf(fin, "%s", pancakes);
    int num = strlen(pancakes);
    int flip = 0;
    char last = pancakes[0];
    for (int i = 1; i < num; ++i) {
      if (pancakes[i] != last) {
        last = pancakes[i];
        ++flip;
      }
    }
    if ((flip % 2 == 0 && pancakes[0] == '-') ||
      (flip % 2 == 1 && pancakes[0] == '+')) {
      ++flip;
    }
    fprintf(fout, "%d\n", flip);
  }
}