#include <cstdio>

using namespace std;

double solve(double c, double f, double x)
{
  double rate = 2.0;
  double time = 0.0;

  if (x <= c)
    return x / rate;

  while (true)
  {
    time += c / rate;

    // Decide to upgrade or not.
    if (x / (rate + f) < (x - c) / rate)
    {
      rate += f;
    }
    else
    {
      time += (x - c) / rate;
      break;
    }
  }
  return time;
}

int main()
{
  FILE *fin, *fout;
  fin = fopen("input.txt", "r");
  fout = fopen("output.txt", "w");

  int T, n;
  double c, f, x, result;

  fscanf(fin, "%d\n", &T);
  for (n = 1; n <= T; n++)
  {
    fscanf(fin, "%lf %lf %lf\n", &c, &f, &x);

    result = solve(c, f, x);
    fprintf(fout, "Case #%d: %.7f\n", n, result);
  }
  fclose(fin);
  fclose(fout);
  return 0;
}
