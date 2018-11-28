#include <iostream>
#include <cstdio>
#include <algorithm>
#include <array>
#include <vector>

using namespace std;

// 何個Farmを買えばよいかを確かめる．
int main() {
  int t;
  cin >> t;
  for ( int i = 1; i <= t; i++ ) {
	double c, f, x;
	cin >> c >> f >> x;
	double cf = 2.0;
	double ct = 0.0;
	while ( true ) {
	  double notbuytime = x / cf;
	  double buytime = c / cf + x / ( cf + f );
	  if ( notbuytime > buytime ) {
		ct += c / cf;
		cf += f;
	  } else {
		ct += notbuytime;
		break;
	  }
	}
	printf( "Case #%d: %.7f\n", i, ct );
  }
}
