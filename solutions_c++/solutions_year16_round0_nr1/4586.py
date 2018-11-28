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



using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool isFilled(bool * arr){
	bool b = true;
	for (int i=0; i<10;i++){
		b = b&&arr[i];
	}
	return b;
}

long lastNumber(long n){
	bool digits[10];
	for (int i=0; i<10; i++){
		digits[i] = false;
	}

	long mul;
	long number;
	

    long m = 0 ; 
    while(!isFilled(digits)){
    	++m;
    	mul=m*n;
    	number = mul;
		while (number>0)
	    {
	        digits[number % 10] = true;
	        number /= 10;
	    }
    }
	return mul;
}



int main() {
  long n;
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n ;  // read n and then m.
    if(n!=0){
    	cout << "Case #" << i << ": " << lastNumber(n) << endl;
    }else{
    	cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
    //cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}

