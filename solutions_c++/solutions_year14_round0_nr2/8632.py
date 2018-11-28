#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
#define inf 10000000
using namespace std;
double f, x, c;
double check(int farmnum)
{
    double curinc = 2, restime = 0;
    for (int j = 0; j < farmnum; j++)
    {
        restime += c / curinc;
        curinc += f;
    }
    return restime + x / curinc;
}
double newsolve()
{
    int l = 0, r = 1000000;

    while(r - l >= 3)
    {
            int farm1 = l + (r - l) / 3;
        int farm2 = r - (r - l) / 3;
        double res1, res2;
        res1 = check(farm1);
        res2 = check(farm2);
        if (res1 > res2)
        {
            l = farm1;
        }
        else
          r = farm2;
    }
    double curres = inf;
    for (int j = l; j <= r; j++)
    {
        curres = min(curres, check(j));
    }
    return curres;
}
/*double solve(double income)
{
    int t;
    cout << income << endl;
    cin >> t;
    if (c / income > x / income)
      return x / income;
    double res1 = c / income + solve(income + f);
    double res2 = x / income;
    return min(res1, res2);
}*/
int main()
{
  int i, j, n, m, k, t;
  ifstream cin ("input.in");
  ofstream cout ("output.txt");
  //double f, x, c, income;
  cin >> t;
  for (j = 0; j < t; j++)
  {
    cin >> c >> f >> x;

   // income = 2;
    //double res = solve(2);
   /* while(1)
    {
      double nofarm = x / income;
      double withfarm = c / income + x / (income + f);
      if (nofarm < withfarm)
      {
        res += nofarm;
        break;
      }
      else
      {
        res += withfarm;
        income += f;
      }
    }*/

    cout.precision(10);
    cout << "Case #" << j + 1 << ": ";
    cout << newsolve() << endl;
  }
}
