#include <cstdlib>
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int trim(long long int &n) {
  int i = 0;
  while (n % 10 == 0) {
    n /= 10; 
    ++i;
  }
  return i;
}

bool foo(long long int n, long long int &res) {
  if (n == 0)
    return false;

  int trimmed = trim(n);
  long long int tmp, test = 0, num;
  bool v[10] = { false };
  
  if (trimmed) {
    v[0] = true;
    test = 1;
  }

  for (int i = 1; ; ++i) {
    res = n * i;
    tmp = n * i;
    while (tmp) {
      num = tmp % 10;
      tmp = tmp / 10;
      
      if (!v[num]) {
        v[num] = true;
        test = test | (1 << num);
      }
    }
    
    if (test == 0b1111111111)
      break;
  }

  while (trimmed) {
    res *= 10;
    --trimmed;
  }

  return true;
}

int main() {
  int t;
  long long n, res;
  FILE *fin = NULL, *fout = NULL;
  fin = fopen("inputA.txt", "r");
  fout = fopen("outputA.txt", "w");
  // for (int i = 0; i <= 1000000; ++i) {
  //   fprintf(fin, "%d\n", i);
  // }

  fscanf(fin, "%d", &t);
  for (int i = 1; i <= t; ++i) {
    fscanf(fin, "%lld", &n);
    if (foo(n, res))
      fprintf(fout, "Case #%d: %lld\n", i, res);
    else
      fprintf(fout, "Case #%d: INSOMNIA\n", i);
  } 



  fclose(fin);
  fclose(fout);
	return 0;
}