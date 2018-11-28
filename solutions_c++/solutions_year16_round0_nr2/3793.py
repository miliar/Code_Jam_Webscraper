#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;


int solve(int runs, int fr, int bk) {
	int count = 0;


  while (runs > 0) {
    if (fr) {
      // if front positive, flip front
      count++;
      fr = 0;
    }
    if (!fr) {
      // if front negative and 1+ runs,
      //flip
      count++;
      runs--;
      // if back was negative,
      fr = 1;
    }
  }



	return (count );


}


int main(void) {
    /* number of test cases */
    unsigned short int t;
    int fr, bk, tmp;
    int runs;
    size_t ps;
    string s;
    string c;

    cin >> t;
    getline(cin, s);

    for(int i=1; i <= t; i++) { //loops for each case
        c = "-";
        runs = 0;
 
        getline(cin, s);
        ps = s.find(c);

        while (ps != string::npos) {
          //if negative, found run
          if (c == "-") {
            runs++;
            c = "+";
          }
          else { // look for next run
            c = "-";
          }
          
          ps = s.find(c, ps+1);

        }

        // now have found # of runs.
        // set flags
        if (s[0] == '+') {
          fr = 1;
        }
        else {
          fr = 0;
        }

        if (s[s.length()-1] == '+') {
          bk = 1;
        }
        else {
          bk = 0;
        }

        // everything set. onto calculation

        cout << "Case #" << i << ": " << solve(runs,fr,bk) << endl;

    }

    return 0;
}

