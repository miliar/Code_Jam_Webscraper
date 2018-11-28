#include <iostream>
#include <cstdio>
using namespace std;

int main() {
  FILE *fin = fopen("al.in", "r");
  FILE *fout = fopen("al.out", "w");
  int testn = 0;
  int n = 0;
  fscanf(fin, "%d", &testn);
  for (int t = 1; t <= testn; ++t) {
    fprintf(fout, "Case #%d: ", t);
    fscanf(fin, "%d", &n);
    if (n == 0) {
      fprintf(fout, "INSOMNIA\n");
      continue;
    }
    int i = 1;
    bool used[10] = {false};
    int count = 0;
    while (true) {
      int number = i * n;
      while (number != 0) {
        int digit = number % 10;
        if (!used[digit]) {
          used[digit] = true;
          ++count;
        }
        number /= 10;
      }
      if (count >= 10) {
        fprintf(fout, "%d\n", i * n);
        break;
      }
      ++i;
    }
  }
}