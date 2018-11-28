#include <cstdio>

using namespace std;

bool checkWinner (int x, int r, int c) {
  //if (x >= 7)
  //  return true;
  if (x > 2 && (r < x-1 || c < x-1))
    return true;
  if (r < x && c < x)
    return true;
  int rc = r * c;
  if (rc % x != 0)
    return true;
  return false;
}



int main () {
  
  int T;
  scanf ("%d", &T);
  char *richard = (char*) "RICHARD";
  char *gabriel = (char*) "GABRIEL";
  
  for (int t = 1; t <= T; ++t) {
    int X, R, C;
    scanf ("%d%d%d", &X, &R, &C);
    //printf ("x = %d r = %d c = %d\n", X, R, C);
    printf ("Case #%d: %s\n", t, checkWinner (X, R, C) ? richard : gabriel);
  }
  
  return 0;
}
