#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>

using namespace std;

bool isPalindrome(long next) {
	char str[240];
	sprintf(str, "%ld", next);
	int len = strlen(str);
  	//cout << str << "length : " << len << endl;
	for(int i=0; i<len/2; ++i) {
      	//cout << str[i] << ':' << str[len-1-i] << endl;
		if(str[i] != str[len-i-1])
			return false;
	}
	
	return true;
}

int main()
{
	int T;
	long A, B;
	cin >> T;
	for(int idx =1; idx <= T; idx++) {
		cin >> A >> B;
	
		long st = sqrt(A);		
		long next = st*st;
        while(next < A) {
          ++st;
          next = st*st;
        }
      
		unsigned int count = 0;
		while(next <= B) {
          if(isPalindrome(next) && isPalindrome(st)) {
			//cout << next << endl;	
            count++;
          }
          
          	st++;
			next = st*st;
		}
		
		cout << "Case #" << idx << ": " << count << endl;
	}
	return 0;
}