//In the name of God
#include <algorithm>
#include <iostream>
#include <iomanip>

using namespace std;

int t;
long double c, f, x, ans, a[1000000];

int main ()
{
  cin >> t ;
  for(int ii = 1 ; ii <= t ; ii++)
    {
      cin >> c >> f >> x ; 
      ans = x / 2.0;
      a[0] = 0;
      for(int i = 1 ; i <= x ; i++)
	{
	  a[i] = a[i - 1] + (c / (2.0 + (i - 1.0) * f));
	  ans = min(ans, a[i] + x / (2.0 + (long double)i * f));
	}
      cout << "Case #" << ii << ": " << fixed << setprecision(7) << ans << endl ;
    }
}
