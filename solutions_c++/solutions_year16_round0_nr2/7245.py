/*
 * Google_code_jam_1.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: Anoshak
 */

#include <iostream>

#define MAX 50000
using namespace std;

int main() {
  int t,j,count;
  string s;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> s;
    count = 0;
    for(j=1;j < s.length(); j++)
    {
    	if(s[j] != s[j-1])
    		count++;
    }
    if(s[s.length()-1] == '-')
    	count++;
   	cout << "Case #" << i <<": " << count << endl;

  }
  return 0;
}


