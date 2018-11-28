#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <set>
using namespace std;


int main()
{
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; t++)
  {
    double C, F, X;
    scanf("%lf%lf%lf", &C, &F, &X);
    //cout << C << " " << F << " " << X << endl;
    double s = 0.0;
    
    
    double f = 2.0;
    double T = 1e+18;
    
    if (X <= C)
    {
      printf("Case #%d: %lf\n", t, X / 2.0);
    }
    else
    {
      double f = 0.0;
      double l = 0.0;
      double T = 0.0;
      double best = 1e18;
      for (int i = 0; i < X + 2; i++)
      {
        double b = T + X / (2.0 + f);
        T += C / (2.0 + f);
        f += F;
        best = min(best, b);
     //   printf("%lf ", best);
      }
      printf("Case #%d: %.9lf\n", t, best);
    }
    
    //cout << endl;
    
  }
  
  return 0;
}

