#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <cstdlib>
#pragma warning(disable : 4996)
using namespace std;

int T, X, R, W;

int main() {
      freopen("D-small-attempt0.in", "r", stdin);
      freopen("output.txt","w",stdout);
      cin >> T;
      for(int i = 0; i < T; ++i) {
	     cin >> X >> R >> W;
	      if (R > W) {
		  int tmp = R;
		  R = W;
		  W = tmp;
	      }
	      if (R * W % X != 0) {
		  cout << "Case #" << i + 1 << ": " << "RICHARD\n";
		  continue;
		  }
		  if (X == 1 || X == 2)
			  cout << "Case #" << i + 1 << ": " << "GABRIEL\n";
		  if (X == 4) {
			  if (R < 3)
				  cout << "Case #" << i + 1 << ": " << "RICHARD\n";
			  else 
				  cout << "Case #" << i + 1 << ": " << "GABRIEL\n";
			}
		  if (X == 3) {
			  if (R == 1)
				 cout << "Case #" << i + 1 << ": " << "RICHARD\n";
			  else 
				  cout << "Case #" << i + 1 << ": " << "GABRIEL\n";
		  }
	  }
      fclose(stdout);
      fclose(stdin);
      return 0;
}