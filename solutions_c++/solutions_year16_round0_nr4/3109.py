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


string arr_to_string(int divs[], int len) {
  string str = "";
  for (int i=0;i<len-1;i++) {
    str = str + to_string(divs[i]) + " ";
    //cout << divs[i] << " ";
  }
  str = str + to_string(divs[len-1]);
  //cout << divs[8] << endl;

  return str;
}


string solve(int k, int c, int s) {
	int det = k-s;
  int tmp = 0;
  int look[s];
  int flag = 0;
  string ans;
  
  if (c == 1) {
    if (det == 0) {
      for (int i=0; i<s; i++) {
        look[i] = i+1;
      }
      ans = arr_to_string(look, s);
    
    }
    else {
      ans = "IMPOSSIBLE";
    }

  }  


  else {
    //c > 1

    look[0] = 2;
    for (int i=1; i <s; i++) {
      look[i] = look[i-1] + (k+1);
    }
    if (det > 1) {
      ans = "IMPOSSIBLE";
    }
    else {
      ans = arr_to_string(look,k-1);
    }

  }


	return (ans );


}


int main(void) {
    /* number of test cases */
    unsigned short int t;


    int k;
    int c;
    int s;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
        
        cin >> k;
        cin >> c;
        cin >> s;

        // everything set. onto calculation

        cout << "Case #" << i << ": " << solve(k,c,s) << endl;

    }

    return 0;
}

