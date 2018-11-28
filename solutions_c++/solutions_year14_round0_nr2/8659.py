#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char const *argv[])
{
  int tc;
  cin >> tc;

  for (int z = 0; z < tc; ++z)
  {
    double total = 0.0;
    double cookies = 0.0;
    double c, f, x;
    double gen = 2.0,
           t1, t2, tf, tf_new;
  
    cin >> c >> f >> x;

    while ( 1 ) 
    {
      t1 = c / gen;
      t2 = ( x - c ) / gen;
      tf = x / gen;
      tf_new = x / ( gen + f );

      if ( tf < t1 )
      {
        total += tf;
        break;
      }

      if ( tf < t1 + tf_new )
      { // not buy factory, wait until finish
        total += tf;
        break;
      }

      if ( tf_new < t2 )  
      { // buy factory
        gen += f;
        total += t1;
      }
      else
      {
        total += t1 + t2;
        break;
      }
    }

    cout << fixed << setprecision(7) << "Case #" << z+1 << ": " << total << endl;
  }
  return 0;
}