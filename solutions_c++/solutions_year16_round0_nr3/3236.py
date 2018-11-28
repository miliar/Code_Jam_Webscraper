#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;


string int_array_to_string(int int_array[], int size_of_array) {
  string str = "";
  for (int i=0;i<size_of_array;i++) {
    str = str + to_string(int_array[i]);
  }

  return str;
}


string divs_to_string(unsigned long long divs[]) {
  string str = "";
  for (int i=0;i<8;i++) {
    str = str + to_string(divs[i]) + " ";
    //cout << divs[i] << " ";
  }
  str = str + to_string(divs[8]);
  //cout << divs[8] << endl;

  return str;
}


string solve(int n, int j) {
	
  string all = "";
  string jcs = "";
  string tmpjc = "";
  int p; //pos
  int b; //base
  int found = 0;
  int nflag = 0; 
  int pass;
  unsigned long long divs[9];
  int primes[168] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997};

  //use array to hold divisors
  //use array to hold the jamcoin
  
  // first with length, initial 1...1 with all 0s in btwn
  // 
  //tentatively add digit -> by using random and flipping a bit??
  // calc in base 
  //     brute force divide 2,3,5,7 ( % == 0)
  //     if no, (% != 0) try another digit
  //     use random to pick digits to flip btwen pos 1 and 14 (0 and 15 set)


  int k;
  int u;
  //initialize the jamcoin minimum 
  int jc[n];
  for (k=0;k<n;k++) {
    if (k==0) {
      jc[k] = 1;
    }
    else if (k==n-1) {
      jc[k] = 1;
    }
    else {
      jc[k] = 0;
    }
  }
  unsigned long long tmp[11];
  // holding values of jamcoin minimum converted into the respective bases
  // pos 2 -> base 2 ... 10 -> base 10 ; pos 0-1 in array but will not be used
  for (k=0; k<11; k++) {
    tmp[k] = (pow(k,(n-1)) + 1);
    //cout << "tmp[b]: " << tmp[k] << " for b = " << k << endl;

  }


  while (found < j) { //need to find some numbersss

    pass = 0;
    while (pass == 0 ) {


      //random p to flip
      p = (rand() % (n-2)) + 1;

      if (jc[p] == 1) { //flip!
        jc[p] = 0;
        nflag = 1;
      }
      else {
        jc[p] = 1;
        nflag = 0;
      }

      //cout << "possible jamcoin: " << int_array_to_string(jc,n) << endl;
      //cout << "testing.." << endl;

      // having flipped a bit, calc new values in tmp

      for (b=2; b<11; b++) {
        if (nflag) {
          tmp[b] = tmp[b] - pow(b,(n-p-1));
        }
        else {
          tmp[b] = tmp[b] + pow(b,(n-p-1));
        
        //cout << "tmp[b]: " << tmp[b] << " for b = " << b << endl;

        }

      }

      for (b=2; b<11; b++) {
       
        //cout << "number repr in base " << b << " is " << tmp[b] << endl;

       // divide, if fail all reloop to try again, else add divisor to array divs

        for (u = 0; u<168; u++) {
          if ((tmp[b] % primes[u] == 0 ) && (tmp[b] != primes[u]) ){
            //cout << tmp[b] << " divisible by " << primes[u] << "!" << endl;
            divs[b-2] = primes[u];
            pass = 1;
            break;
          }
        }
        if (u == 168) { //didnt find any
          pass = 0;
          break;
        }
        
        //cout << "divs[b-2]: " << divs[b-2] << " for b = " << b << endl;

      }


    }


    //when here, have successfully found a jamcoin
    //check for duplicates?

    tmpjc = int_array_to_string(jc,n);

    if (jcs.find(tmpjc) == string::npos) {

      found++;
      jcs = jcs + tmpjc + " ";
      all = all + tmpjc + " " + divs_to_string(divs) + "\n";
      // concat jc (in string form) to all, concat divisors to all, concat \n

    }

    // else, look again



    // done...?

  }




	return (all );


}


int main(void) {
    /* number of test cases */
    unsigned short int t;


    int n;
    int j;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
        
        cin >> n;
        cin >> j;

        // everything set. onto calculation

        cout << "Case #" << i << ": " << endl;
        cout << solve(n, j) << endl;

    }

    return 0;
}

