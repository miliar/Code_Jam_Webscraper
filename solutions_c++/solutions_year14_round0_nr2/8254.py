#include <iostream>
#include <cmath>
#include <iomanip> 
#include <stdio.h>

using namespace std;

int main()
{
  double c, f, x;
  int rx;
  int t, n;
  cin >> t;

  for(int p=1;p<=t;p++)
  {
    cin >> c >> f >> x;
    rx = x; 
    double a[rx+1][5];
    n = 2;
    a[0][0] = 2;
    a[0][1] = x/a[0][0];
    a[0][2] = 0;
    a[0][3] = 0;
    a[0][4] = x/a[0][0];
    for(int i=1;i<=rx;i++)
    {
      a[i][0] = a[i-1][0] + f;
      a[i][1] = x / a[i][0];
      a[i][2] = c / a[i-1][0];
      a[i][3] = a[i-1][3] + a[i][2];
      a[i][4] = a[i][1] + a[i][3]; 
    }

    //for(int i=0; i<=rx;i++)
    //{
    //  cout << a[i][0] << " \t" << a[i][1] << " \t" << a[i][2] << " \t" << a[i][3] << " \t" << a[i][4] << " \t" << endl;
    //}

    double nmin = 200000000000;
    for(int i=0;i<=rx;i++)
    {
    	nmin = min(nmin, a[i][4]);
    }
    printf("Case #%i: %.7lf\n", p, nmin);
    //cout << "Case #" << p << ": " << setprecision(7) << nmin << endl;
  }
}
