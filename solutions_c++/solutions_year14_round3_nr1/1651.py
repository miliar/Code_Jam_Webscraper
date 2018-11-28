#include <iostream>
#include <cstdio>

using namespace std;

int tn;
int P, Q;

int gcd(int x, int y) {
  while (y != 0) {
    int tmp = x % y;
    x = y;
    y = tmp;
  }
  return x;
}

int main(int argc, char *argv[])
{
  cin >> tn;
  for (int ti = 1; ti <= tn; ti ++ ) {
    scanf("%d/%d", &P, &Q);
    int tmp = gcd(P, Q);
    P /= tmp;
    Q /= tmp;
    int cnt = 0;
    int tmpq = Q;
    while(tmpq % 2 == 0) {
      tmpq /= 2;
      cnt++;
    }
    if (tmpq == 1) {
      cnt = 0;
      while (Q != 1) {
        for (int i = Q; i >= P; --i) {
          if (P - (i - P) >= 0) {
            cnt ++;
            P = i;
            tmp = gcd(P, Q);
            P /= tmp;
            Q /= tmp;
            break;
          }
        }
      }
      printf("Case #%d: %d\n", ti, cnt);
    } else {
      printf("Case #%d: impossible\n", ti);
    }
  }
  return 0;
}
