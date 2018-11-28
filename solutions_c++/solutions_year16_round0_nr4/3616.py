#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

int main() {
  FILE *fin = fopen("d.in", "r");
  FILE *fout = fopen("ddd.out", "w");
  int testn = 0;
  fscanf(fin, "%d", &testn);
  for (int t = 1; t <= testn; ++t) {
    fprintf(fout, "Case #%d: ", t);
    int ktiles, complexity, students;
    fscanf(fin, "%d%d%d", &ktiles, &complexity, &students);
    for (int i = 1; i <= ktiles; ++i) {
      fprintf(fout, "%d ", i);
    }
    fprintf(fout, "\n");
  }
}