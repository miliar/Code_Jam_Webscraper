#include <iostream>
#include <Vector>

using namespace std;

double recurse( double curSpeed, double seconds, double C, double F, double X)
{
    double settle = seconds + X/curSpeed;
    double next = seconds + C/curSpeed + X/(curSpeed + F);
    
    if( settle < next )
        return settle;
    else
        return recurse( curSpeed+F, seconds+C/curSpeed, C, F, X );
}

int main()
{
    int cases;
    double C, F, X;
    
    cout.precision(7);
    
  cin >> cases;

  for( int c = 0; c < cases; c ++ )
  {

      cin >> C >> F >> X;
      cout << "Case #" << c+1 << ": ";
      printf("%4.7f\n",recurse( 2, 0, C, F, X));
      
      
  }

  return 0;
}
