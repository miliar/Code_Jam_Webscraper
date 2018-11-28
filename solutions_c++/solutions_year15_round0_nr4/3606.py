#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;





int main() {
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("D-small-attempt0.out", "w", stdout);
  int T;
  //int ki = 0;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {

    //fflush(stdout);
	  int X; int R; int C; scanf("%d %d %d", &X, &R, &C);
	  if(X == 1)
	  {
		  printf("Case #%d: %s\n", Ti, "GABRIEL");
		  continue;
	  }
	  if( X > (R*C))
	  {
		  printf("Case #%d: %s\n", Ti, "RICHARD");
		  continue;
	  }


	  if(R * C == 16)
	  {
		  if(X == 3)
		  {
			  printf("Case #%d: %s\n", Ti, "RICHARD");
			  continue;
		  }
		  else
		  {
			  printf("Case #%d: %s\n", Ti, "GABRIEL");
			  continue;
		  }

	  }
	  if(R * C == 12)
	  {

		  printf("Case #%d: %s\n", Ti, "GABRIEL");
		  continue;


	  }
	  if(R * C == 9)
	  {
		  if( X == 3 || X == 1)
		  {
			  printf("Case #%d: %s\n", Ti, "GABRIEL");
			  continue;
		  }
		  else
		  {
			  printf("Case #%d: %s\n", Ti, "RICHARD");
			  continue;
		  }



	  }
	  if(R * C == 8)
	  {
		  if( X == 3 || X == 4)
		  {
			  printf("Case #%d: %s\n", Ti, "RICHARD");
			  continue;
		  }
		  else
		  {
			  printf("Case #%d: %s\n", Ti, "GABRIEL");
			  continue;
		  }

	  }
	  if(R * C == 6)
	  {
		  if( X == 4)
		  {
			  printf("Case #%d: %s\n", Ti, "RICHARD");
			  continue;
		  }
		  else
		  {
			  printf("Case #%d: %s\n", Ti, "GABRIEL");
			  continue;
		  }

	  }
	  if(R * C == 4)
	  {
		  if( X == 3 || X == 4)
		  {
			  printf("Case #%d: %s\n", Ti, "RICHARD");
			  continue;
		  }
		  else
		  {
			  printf("Case #%d: %s\n", Ti, "GABRIEL");
			  continue;
		  }

	  }

	  if(R * C == 3)
	  {
		  if( X == 2 || X == 3 || X == 4)
		  {
			  printf("Case #%d: %s\n", Ti, "RICHARD");
			  continue;
		  }
		  else
		  {
			  printf("Case #%d: %s\n", Ti, "GABRIEL");
			  continue;
		  }

	  }

	  if(R * C == 2)
	  {
		  if( X == 3 || X == 4)
		  {
			  printf("Case #%d: %s\n", Ti, "RICHARD");
			  continue;
		  }
		  else
		  {
			  printf("Case #%d: %s\n", Ti, "GABRIEL");
			  continue;
		  }
	  }

	  if(R * C == 1)
	  {
		  if( X == 1 )
		  {
			  printf("Case #%d: %s\n", Ti, "GABRIEL");
			  continue;
		  }
		  else
		  {
			  printf("Case #%d: %s\n", Ti, "RICHARD");
			  continue;
		  }
	  }

    fflush(stdout);

  }
   fflush(stdout);
  return 0;
}
