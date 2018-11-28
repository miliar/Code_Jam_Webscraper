#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

int GCD(int P, int Q) {
  if (Q == P) return P;
  else if (P < Q) return GCD(P, Q - P);
  else return GCD(P - Q, Q);
}

int maxbit(int P) {
  if (P == 1) return 0;
  else return 1+maxbit(P >> 1);
}

int ancestor(int P, int Q) {
  double k = log2(Q);
  if (ceil(k) != k) return -1; // Impossible
  else return (int)k-maxbit(P);
}

int main () {
  ifstream input;
  input.open("input");

  int ntest;
  input >> ntest;

  for (int k=0;k<ntest;k++) {
    int P, Q;
    char slash;
    input >> P >> slash >> Q;

    int gcd = GCD(P, Q);
    P /= gcd;
    Q /= gcd;

    int a = ancestor(P,Q);
    if (a < 0)
      cout << "case #" << k+1 << ": impossible" << endl;
    else
      cout << "case #" << k+1 << ": " << ancestor(P,Q) << endl;
  }

  input.close();
  return 0;
}

