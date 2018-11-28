//============================================================================
// Name        : C_jamcoin.cpp
// Author      : Jonas
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

bool prime(__int128 n,  int k, long div[]){
	bool flag = true;
	if(n%2 == 0)
	  {
		  div[k] = 2;
		  return false;
	  }
	for(__int128 i=3;i<=sqrt(n) && (i < 80877);i = i+2)
	  {
	      if(n%i==0)
	      {
	    	  div[k] = i;
	          flag= false;
	          break;
	      }
	  }
	return flag;
}

__int128 power(__int128 val, int exp){
	__int128 out = 1;
	for(int i = 0; i < exp; i++){
		out = out * val;
	}
	return out;
}

int main () {
  int t;
  ifstream fin ("input.txt");
  ofstream fout ("output.txt");
  if (fin.is_open() && fout.is_open())
  {
    fin >> t;
    fout.precision(10);

    for(int i = 0; i < t ;i++){
    	fout << "Case #" << i+1 << ":"<< endl;
    	int n,jt;
    	fin >> n >> jt;
    	long div[9];
    	bool digits[n];
    	for(__int128 j = power(2,(n-1))+3; j < power(2,(n)) && jt > 0; j=j+2){
    		for(int k = 0; k < n; k++){
    			__int128 tmp = j / power(2,k);
    			digits[k] = (tmp % 2 == 1); //Construct 01-sequence
    		}

			bool isprime = false;
			for(int l = 2; l < 11 && !isprime; l++){
				__int128 sum = 0;
				for(int m = 0; m < n; m++){
					if(digits[m])
						sum = sum + power (l,m);
				}
				if(prime(sum, l-2, div)){
					isprime = true;
				}
			}
			if(!isprime){
				jt--;
				for(int l = 0; l < n ;l++){
					fout << digits[n-1-l];
				}
				for(int l = 0; l < 9; l++)
					fout << " " << div[l];
				fout << endl;

    		}
			cout << jt << endl;
    	}



    }
    cout << "Terminated" << endl;
    fin.close();
    fout.close();
  }

  else cout << "Unable to open file";

  return 0;
}
