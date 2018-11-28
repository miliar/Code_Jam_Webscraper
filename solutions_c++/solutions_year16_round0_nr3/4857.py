#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream in("data.in");
ofstream out("data.out");

int n,j;
int numFound;
int val[32];
long long divisors[11];

long long getVal(int base) {
  long long x = 0;
  for (int i=0; i<n; i++) {
    x *= base;
    x += val[i];
  }
  return x;
}

long long getDivisor(long long x) {
  for (long long d = 2; d * d <= x; d++) {
    if (x%d == 0) {
      return d;
    }
  }
  return -1;
}

void process() {
  for (int base = 2; base <= 10; base++) {
    long long x = getVal(base);
    long long d = getDivisor(x);
    
    if (d == -1) {
      return;
    }
    
    divisors[base] = d;
  }

  for (int i=0; i<n; i++) {
    out << val[i];
  }
  for (int base = 2; base <= 10; base++) {
    out << " " << divisors[base];
  }
  out << endl;
  
  numFound++;
}

void doit(int i) {
  if (i == n-1) {
    process();
    return;
  }

  val[i] = 0;
  doit(i+1);

  if (numFound == j) {
    return;
  }

  val[i] = 1;
  doit(i+1);
}

int main() {
  int t;
  in >> t;

  for (int caseNum = 1; caseNum <= t; caseNum++) {
    in >> n >> j;
    
    out << "Case #" << caseNum << ":" << endl;

    val[0] = 1;
    val[n-1] = 1;
    numFound = 0;
    doit(1);
  }
}
