#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;

bool isPalindrome(long long num) {
     long long n = num, digit, rev=0;
     do
     {
         digit = num % 10;
         rev = (rev*10) + digit;
         num = num/10;
     } while (num!=0);

     return  n == rev;
}

bool isSquare(int n){
    int h = n & 0xF;

    if (h > 9) {
		return false;
	}

    if (h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8){
        int t = (int) floor( sqrt((double) n) + 0.5 );
        return t*t == n;
    }

    return false;
}

unsigned long long int getGameStatus(long long A, long long B) {
	unsigned long long int counter = 0;
	for(int i=A; i<= B; i++) {
		//cout << i << " squrel: " << isSquare(i)  <<endl;
		//cout << i << " palindrome: " << isPalindrome(i)  <<endl;
		if (isSquare(i) && isPalindrome(i) && isPalindrome(sqrt(i))) {
			//cout << i << endl;
			counter++;
		}
	}
	return counter;
}

int main(void) {
	unsigned short int t;
	unsigned long long int A, B;
	cin >> t; //number of test cases

	for(int i=1; i <= t; i++){ //loops for each case
		cin >> A >> B;
		cout << "Case #" << i << ": " << getGameStatus(A, B) << endl;
	}

	return 0;
}
