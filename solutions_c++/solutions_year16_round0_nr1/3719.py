#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;


string solve(int n) {
	int ans = n;
  int m = 1; // multiplier. m * ans = new number
  string ns;
  size_t pos;

  

  if (n == 0) {
    return ("INSOMNIA");
  }

  int j;
  int len = 10;
  string d[10] = {"0","1","2","3","4","5","6","7","8","9"};

  while (len > 0) {
    //calculate number to look at
    ans = n * m;
    ns = to_string(ans);
    m++;



    // look for digits in the number 
    //len = number of digits left that need to be thought of

    for (j=0; j<len; j++) {
      pos = ns.find(d[j]);
      if (pos!= string::npos) {
        //found a digit! 


        d[j] = d[len-1]; //can get rid of the digit in the list
        len--;

        j--; //need to search same pos now that it has been replaced

      }
      // didn't find digit, look for next digit

    }

    
  }




	return (to_string(ans) );


}


int main(void) {
    /* number of test cases */
    unsigned short int t;


    int n;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
        
        cin >> n;

        // everything set. onto calculation

        cout << "Case #" << i << ": " << solve(n) << endl;

    }

    return 0;
}

