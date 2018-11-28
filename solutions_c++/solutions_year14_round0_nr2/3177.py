#include <iostream>
#include <algorithm>
#include <functional>
#include <deque>
#include <cstring>
#include <cstdio>
#include <cstdlib>


using namespace std;

int main()
{
  double C, F, X, curF, t;
  int T;
  

  cin >> T;
  for (int i = 0; i < T; ++i) {
    printf ("Case #%d: ", i+1);

    curF = 2;
    t = 0;
    cin >> C >> F >> X;
    
    while (true) {
      if (C >= X) {
	t += X/curF;
	break;
      }
 
      //      printf ("%f, %f, %f, %f, %f\n", C,F,X,curF,t);
      //      printf ("%f, %f, %f\n", X/curF, C/curF, X/(curF+F));
     
      if ( (X/curF) <=
	   ( (C/curF) + (X/(curF+F)))) {
	t += X/curF;
	break;
      } else {
	t += C/curF;
	curF += F;
      }
    }

    printf ("%f", t);

    printf ("\n");
  }
  
  return 0;
}

