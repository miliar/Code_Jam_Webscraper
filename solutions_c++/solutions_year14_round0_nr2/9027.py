#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

vector<double> v(100002);
double fa = 0;
double fb = 0;
double C;
double F;
double X;


inline double countTime(int N)
{
  double ans = 0;
  for (int j = 0; j < N; j++)
  {
    ans += (N - j) * C / (2 + j * F);
  }
  ans *= F;
  ans += X;
  ans += (N * C);
  ans /= (2 + F * N);
  return ans;
}

inline double f(int N)
{
  double x = 0;
  for (int j = 0; j < N; j++)
  {
    x += ((N - j) * C / (2 + F * j));
  }
  x = x * F * F;
  double temp = (F * F * N * C + 2 * F * C) * v[N];
  x = x + X * F - 2 * C - temp;
  return x;
}

double findZero(int a, int b)
{
  int c;
  double fc;
  while (b - a > 1)
  {
    c = (a + b) / 2;
    fc = f(c);
    if (fc < 0)
    {
      fb = fc;
      b = c;
    }
    else
    {
      fa = fc;
      a = c;
    }
  }
  double m = 1e307;
  for (int i = b - 10; i < b + 10; i++)
  {
    if (i >= 0)
    {
      double ans = countTime(i);
      if (ans < m)
        m = ans;
    }
  }
  return m;
}

int main(void)
{
  ifstream in("codejamB.in");
  ofstream out("codejamB.out");
  int T;
  in >> T;
  for (int i = 0; i < T; i++)
  {
    in >> C >> F >> X;
    int N = X + 1;
    v[0] = 0.5;
    for (int j = 1; j <= N; j++)
    {
      v[j] = v[j - 1] + 1 / (2 + F * j);
    }

    fb = f(N);
    fa = F / 2.0;
    double ans = findZero(0, N);
    out.setf(ios::fixed, ios::floatfield); 
    out << "Case #" << i + 1 <<": " << std::setprecision(7) << ans << endl;
  }
  in.close();

  out.close();
  return 0;
}