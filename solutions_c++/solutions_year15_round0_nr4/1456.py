#include <iostream>

using namespace std;

main () { 
  int T,X,R,C;
  cin >> T;
  for (int t=1; t<=T; t++) {
    cin >> X >> R >> C;
    bool gabriel = false;
    if ( (((R*C) % X) == 0) // board is multiplum of X
	 && (X<=R || X<=C)     // cannnot create to wide piece
	 && ((X==1)
	     || (X==2)
	     || (X==3 && R>=2 && C>=2) 
	     || (X==4 && min(R,C)>=3))) 
      gabriel = true;    
    
    cout << "Case #" << t << ": " << (gabriel ? "GABRIEL" : "RICHARD") << endl;
  };
};
