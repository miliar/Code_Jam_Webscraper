#include <iostream>
using namespace std;


void newproblem(int c, string s) {
    int nummoves = 0;


    bool minusmode = false;
    bool seenaplus = false;
    for (int i = 0; i < s.length(); i++) {
         if (!minusmode) {
	         if (s[i] == '-') {
 		     minusmode = true;
	             if (seenaplus) {
			  nummoves += 2;
 		     } else {
	                   nummoves++;
                     }
	         }
		 else {
		     minusmode = false;
		     seenaplus = true;
	         }
	} else {
 		if (s[i] == '-') {
 		     minusmode = true;
	         }
		 else {
		     seenaplus = true;
                     minusmode = false;
	         }
	}
    }
   
    cout << "Case #" << c << ": " << nummoves << endl;    
}

main() {
  int t;
  string s;
  cin >> t;  
  for (int i = 1; i <= t; ++i) {
    cin >> s; 
    newproblem(i, s);    
  }        
}