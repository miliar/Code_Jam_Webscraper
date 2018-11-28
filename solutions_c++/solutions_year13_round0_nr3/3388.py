#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int A;
int B;
char buff[20];

bool isPal(int n) {
  int d = sprintf(buff, "%d", n);
  int dd = d/2;
  for (int i = 0; i < dd; ++i)
    if (buff[i] != buff[d-1-i])
      return false;
  return true;
}

bool isSqu(int n) {
  double d = sqrt(n);
  double fd= floor(d);
  int n1 = fd * fd;
  return (n == n1);
}


bool isSquPal(int n) {
  double d = floor(sqrt(n));
  return isPal(d);
}

int solve() {
  int r = 0;
  for (int i = A; i <= B; ++i) {
    if (isPal(i) && isSqu(i) && isSquPal(i)) {
      /*            printf("%d is %s %s %s\n", i,
             (isPal(i)? "Pal":""),
             (isSqu(i)? "Squ":""),
             (isSquPal(i)? "SquPal":""));*/
      ++r;
    }
  }
  return r;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> A >> B;
    int r = solve();
    printf("Case #%d: %d\n", t, r);
  }
  return 0;
}
