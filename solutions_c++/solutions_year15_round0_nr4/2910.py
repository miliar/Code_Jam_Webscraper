#include<iostream>
#include<string>
using namespace std;

int main (void) {
  int t;
  scanf("%d", &t);
  for (int cn = 1; cn <= t; ++cn) {
    int x, r, c;
    int res = 0;
    string ret;
    scanf("%d%d%d", &x, &r, &c);
    if (r * c % x != 0) {
      res = 0;
    } else if (x <= 2) {
      res = 1;
    } else if (x == 4) {
        if (r * c >= 12) {
          res = 1;
        } else
          res = 0;
    } else if (x == 3) {
        if (r == 1 || c == 1)
          res = 0;
        else 
          res = 1;
    } else 
        res = 1;
    printf("Case #%d: %s\n", cn, res ? "GABRIEL" : "RICHARD");
  }
  return 0;
}
