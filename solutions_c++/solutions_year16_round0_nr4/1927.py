#include <cstdlib>
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

typedef unsigned long long int ull;

ull semipow(ull k, ull c) {
  ull res = 1;
  for (int i = 1; i < c; ++i) 
    res *= k;
  return res;
}

int main() {
  int t, n, j;

  FILE *fin = NULL, *fout = NULL;
  fin = fopen("inputD.txt", "r");
  fout = fopen("outputD.txt", "w");


  ull K, C, S;

  fscanf(fin, "%d", &t);
  for (int i = 1; i <= t; ++i) {
    fscanf(fin, "%llu %llu %llu", &K, &C, &S);
    fprintf(fout, "Case #%d:", i);

    ull p = semipow(K, C);
    ull add = 1;
    for (int j = 0; j < K; ++j) {
      fprintf(fout, " %llu", add);
      add += p;
    }
    fprintf(fout, "\n");
  }

  fclose(fin);
  fclose(fout);
	return 0;
}