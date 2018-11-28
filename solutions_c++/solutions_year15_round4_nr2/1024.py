#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long double EPS = 1e-12;

int main() {
  freopen("B-small-attempt4.in", "r", stdin);
  freopen("b.out", "w", stdout);

  cout.precision(10);

  int nTest;
  scanf("%d", &nTest);

  for (int test = 0; test < nTest; test++) {
    int n;
    long double v, t;

    cin >> n >> v >> t;

    printf("Case #%d: ", test + 1);

    if (n == 1) {
      long double r, c;
      cin >> r >> c;

      if (abs(t - c) < EPS) {
        cout << v / r << endl;
      }
      else
        printf("IMPOSSIBLE\n");
    }
    else {
      long double r1, c1, r2, c2;

      cin >> r1 >> c1;
      cin >> r2 >> c2;

      long double D = c2 - c1;
      long double Dx = v * c2 - t * v;
      long double Dy = t * v - c1 * v;

//      cout << D << " " << Dx << " " << Dy << endl;

      if (abs(D - 0.00) > EPS) {
        if (((Dx / D / r1 < 0) && abs(Dx / D / r1 - 0.00) > EPS) ||
            ((Dy / D / r2 < 0) && abs(Dy / D / r2 - 0.00) > EPS))
          printf("IMPOSSIBLE\n");
        else
          cout << max(Dx / D / r1, Dy / D / r2) << endl;
      }
      else {
        if (abs(Dx - 0.00) > EPS || abs(Dy - 0.00) > EPS)
          printf("IMPOSSIBLE\n");
        else {
          cout << v / (r1 + r2) << endl;
        }
      }
    }
  }

  return 0;
}
