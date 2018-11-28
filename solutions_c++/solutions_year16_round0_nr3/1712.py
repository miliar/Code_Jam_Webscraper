#include <cstdlib>
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

typedef unsigned long long int ull;

vector<ull> codes;
ull v[] = {65537, 43046722, 4294967297, 152587890626, 2821109907457, 33232930569602, 281474976710657, 1853020188851842, 10000000000000001};

void foo(int n, int j) {
  const ull code_base = (1 << (n-1)) + 1;
  ull code = 0;
  int count = 0;
  vector<ull> v;

  for (ull i = 0; i < (1 << (n - 2)) - 1 && count < j; ++i) {
    cout << i << " out of " << (1 << (n - 2)) - 1 << endl;;
    code = code_base | (i << 1);

    codes.push_back(code);
    ++count;
  }
}

void print_code(FILE *f, ull code, int n) {
  for (int i = n - 1; i >= 0; --i) {
    if ((1 << i) & code)
      fprintf(f, "1");
    else 
      fprintf(f, "0");
  }
}

void print_prove(FILE *f, ull *v) {
  for (int i = 0; i < 9; ++i) {
    fprintf(f, " %lld", v[i]);
  }
}

int main() {
  int t, n, j;
  FILE *fin = NULL, *fout = NULL;

  fout = fopen("outputC.txt", "w");

  n = 16;
  j = 500;

  fprintf(fout, "Case #1:\n");
  foo(n, j);
  for (int k = 0; k < j; ++k) {
    print_code(fout, codes[k], n);
    print_code(fout, codes[k], n);
    print_prove(fout, v);
    fprintf(fout, "\n");
  }

  fclose(fout);
	return 0;
}