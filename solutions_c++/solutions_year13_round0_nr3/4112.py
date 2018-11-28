#include <cstdio>
#include <cmath>
using namespace std;
typedef long long LL;
const int MAXX = 10000100;
int T[MAXX];

bool palindrome(LL a) {
  char T[20]; int i = 0;
  while (a != 0) {
    T[i++] = a%10;
    a/=10;
  } i--;
  for (int j = 0; j <= i; j++, i--) if (T[i] != T[j]) return false;
  return true;
}

void preprocess() {
  for (LL i = 1; i < MAXX; i++) 
    if (palindrome(i) && palindrome(i*i)) T[i] = T[i-1] + 1;
    else T[i] = T[i-1];
}

const double EPS = 1e-12;
LL get(LL a, LL b) {
  LL A = ceil(sqrt(a)-EPS), B = floor(sqrt(b)+EPS);
  return T[B] - T[A-1];
}

int main() {
  int z; scanf ("%d", &z);
  preprocess();
  for (int i = 1; i <= z; i++) {
    LL a,b;
    scanf ("%lld %lld", &a, &b);
    printf ("Case #%d: %lld\n", i, get(a,b));
  }
  return 0;
}
