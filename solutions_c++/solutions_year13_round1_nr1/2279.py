#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char **argv)
{
  int T;
  cin >> T;
  
  int z;
  for(z=0; z<T; z++ ) {
	double r,t;
	cin >> r>> t;

	long k = (long)floor(sqrt((r*r-r)/4.0 + t/2 + 1.0/16.0) - r/2.0 + 1.0/4.0);

	if( 2.0*k*k + k*(2*r-1) > t ) k-= 1;

	cout << "Case #" << z+1 << ": " << (int)k << endl;
	//printf("%lf\n", k);
  }

}
