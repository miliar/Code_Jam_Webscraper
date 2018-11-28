#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

const char* fo = "output.txt";

int a[33];
int found;
long long divisorAtBase[10];
void Generate(int n, int k, int j, ofstream &fo);

int main(int argc, const char * argv[]) {
  ofstream fout;
  fout.open(fo);
  
  found = 0;
  Generate(16, 0, 50, fout);
  
  fout.close();
  return 0;
}

long long interpretAtBase(int n, int base) {
  long long result = 0;
  for (int i = 0; i < n; i++) {
    result += a[i] * pow(base, i);
  }
  return result;
}

long long getDivisor(long long x) {
  for (long long i = 2; i < sqrt(x); i++) {
    if (x % i == 0) {
      return i;
    }
  }
  return -1;
}

bool check(int n) {
  for (int base = 2; base <= 10; base++) {
    long long numAtBase = interpretAtBase(n, base);
    long long divisor = getDivisor(numAtBase);
    
    if (divisor != -1) {
      divisorAtBase[base] = divisor;
    } else {
      return false;
    }
  }
  
  return true;
}

void Generate(int n, int k, int j, ofstream &fo) {
  if (k == n) {
    if (found < j && check(n)) {
      found++;
      for (int i = n - 1; i >= 0; i--) {
        fo << a[i];
      }
      fo  << " ";
      for (int base = 2; base <= 10; base++) {
        fo << divisorAtBase[base] << " ";
      }
      fo << endl;
    }
    return;
  }
  
  if (k == 0 || k == n - 1) {
    a[k] = 1;
    Generate(n, k + 1, j, fo);
  } else {
    for (int i = 0; i < 2; i++) {
      a[k] = i;
      Generate(n , k + 1, j, fo);
    }
  }
}
