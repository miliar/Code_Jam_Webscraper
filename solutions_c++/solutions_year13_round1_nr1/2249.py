#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

/*
struct Record {
  char lane;
  int speed;
  int pos;
  Record(char l, int s, int p): lane(l), speed(s), pos(p) { };
};

bool compare(const Record &lhs, const Record &rhs) {
  return lhs.pos > rhs.pos;
}
*/

double need(int r, int n) {
  double rr = r+1;
  return M_PI*(rr*rr-r*r);

}
void solve() {
  static int i;
  double r, t;
  scanf("%lf%lf", &r, &t);
  double a = 2;
  double b = 2*r-1;
  double c = -t;
  double n = floor((-b+sqrt(b*b-4*a*c))/(2*a));
  double left = a*n*n+b*n+c;
  if (left > 0) n--;
  printf("Case #%d: %.0f\n", ++i, n);
}

int main() {
  int t;
  scanf("%d", &t);
  while (t--)
    solve();

  return 0;
}

