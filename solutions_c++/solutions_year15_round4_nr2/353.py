#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 105;
const double EPS = 1e-6;

double v[MAX], temp[MAX];
double trebv, trebtemp;

int Jednak(double a, double b)
{
  return abs(a - b) < EPS;
}

int Veci(double a, double b)
{
  return a - EPS > b;
}

int Manji(double a, double b)
{
  return a + EPS < b;
}

int main()
{
  int brt;

  scanf("%d", &brt);

  for (int tt=1; tt<=brt; tt++) {
    int n;
    scanf("%d%lf%lf", &n, &trebv, &trebtemp);

    for (int i=0; i<n; i++)
      scanf("%lf%lf", &v[i], &temp[i]);

    printf("Case #%d: ", tt);

    if (n == 1) {
      if (!Jednak(temp[0], trebtemp))
        printf("IMPOSSIBLE\n");
      else
        printf("%lf\n", trebv / v[0]);
      continue;
    }

    if (Jednak(temp[0], temp[1])) {
      if (!Jednak(trebtemp, temp[0]))
        printf("IMPOSSIBLE\n");
      else
        printf("%lf\n", trebv / (v[0] + v[1]));
    }
    else {
      if (Veci(temp[0], temp[1])) {
        swap(temp[0], temp[1]);
        swap(v[0], v[1]);
      }

      if (Manji(trebtemp, temp[0]) || Veci(trebtemp, temp[1]))
        printf("IMPOSSIBLE\n");
      else {
        double vol2 = (trebv * (trebtemp - temp[0])) / (temp[1] - temp[0]);
        double vol1 = trebv - vol2;

        printf("%lf\n", max(vol2 / v[1], vol1 / v[0]));
      }
    }

  }

  return 0;
}
