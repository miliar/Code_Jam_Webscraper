/*
 * Google_code_jam_1.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: Anoshak
 */

#include <iostream>
#include <unordered_set>

#define MAX 50000
using namespace std;

int main() {
  int t, n,dig,j;
  long int no;
  cin >> t;
  unordered_set<int> myset;
  for (int i = 1; i <= t; ++i) {
	myset.clear();
    cin >> n;
    for(j=1;j < MAX; j++)
    {
    	no = n * j;
    	while(no)
    	{
    		dig = no%10;
    		myset.insert(dig);
    		no = no/10;
    	}
    	if(myset.size()==10)
    		break;
    }
    if(j == MAX)
    	cout << "Case #" << i <<": INSOMNIA" << endl;
    else
    	cout << "Case #" << i <<": " << n*j << endl;

  }
  return 0;
}


