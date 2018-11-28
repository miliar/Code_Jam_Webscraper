#include <iostream>

using namespace std;

int
main() {
  int T;


  cin >> T;

  for(int c = 1; c <= T; c++) {
    int R, C, X;

    cin >> X >> R >> C;

    if(C > R) {
      int tmp = C;
      C = R;
      R = tmp;
    }

    int result = 0;

    if(R*C >= X) {
      switch(X) {
	case 1:
	  result = 1;
	  break;

	case 2:
	  {
	    int nw = R*C/2;
	    int nb = R*C - nw;
	    if(nw == nb) {
	      result = 1;
	    }
	  }
	  break;

	case 3:
	  if(((R == 3) && ((C == 2) || (C == 3))) || ((R == 4) && (C == 3))) {
	    result = 1;
	  }
	  break;

	case 4:
	  if((R == 4) && ((C == 3) || (C == 4))) {
	    result = 1;
	  }
	  break;
      }
    }

    cout << "Case #" << c << ": " << (result == 1 ? "GABRIEL" : "RICHARD") << endl;
  }

  return 0;
}

