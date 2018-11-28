#include <cstdio>

using namespace std;

int myHalfCeil(int a) {
  if(a%2 == 0) return a/2;
  return (a+1)/2;
}

int min(int a, int b) {
  if(a < b) return a;
  return b;
}

bool divisible(int area, int X) {
  for(int i = 2; i*X <= area; i++){
    if(area%(i*X) == 0) return false;
  }
  return true;
}

int main() {
  int T;
  int X, R, C;
  int area;
  int caso = 1;

  scanf("%d", &T);

  while(caso <= T) {
    scanf("%d %d %d", &X, &R, &C);
    area = R*C;
    if(area < X || (area == X && X > 2) || (area-X)%X != 0 || (divisible(area-X, X) && X > 3) || X > 7 || min(R, C) < myHalfCeil(X)) printf("Case #%d: RICHARD\n", caso);
    else printf("Case #%d: GABRIEL\n", caso);

    caso++;
  }
  return 0;
}
