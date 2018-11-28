// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool count(vector<bool> &MAP, long long n){
  while (n > 0){
	long long k = n % 10;
	MAP[k] = true;
	n /= 10;
  }
  for (int i = 0; i < 10; i++){
	if (!MAP[i]) return false;
  }
  return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	long long n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
	  cin >> n ;  // read n and then m.
	  if (n == 0){
		cout << "Case #" << i << ": INSOMNIA"<< endl;
	  }
	  else{
		vector<bool> MAP(10, false);
		bool slept = false;
		long long m;
		for (int j = 1; !slept; j++){
		  m = n * j;
		  slept = count(MAP, m);
		}
		cout << "Case #" << i << ": " <<m << endl;
	  }
	  // cout knows that n + m and n * m are ints, and prints them accordingly.
	  // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
	return 0;
}

