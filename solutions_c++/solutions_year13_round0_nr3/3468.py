#include <iostream>
#include <string>
#include <iomanip>
#include <limits>
#include <sstream>
#include <math.h>

using namespace std;

bool isPalindrome(string possiblePalindrome);
string numberToString(int n);

int main()
{
	int numCase;
	cin >> numCase;
	double A,B;

	for (int num = 0; num < numCase; num++)
	{

		// Create boundary intervals [a,b]=[ceil(sqrt(A)),floor(sqrt(B))]
		cin >> A;
		cin >> B;
		
		int a=sqrt(A);
		int b=sqrt(B);
		if(sqrt(A)-a>1E-10) {a+=1;}
		if(b-sqrt(B)>1E-10) {b-=1;}
		
		int count=0;
		for(int i=a;i<=b;i++) { // Note: String representation is mainly to keep for later submissions
			if(isPalindrome(numberToString(i)) && isPalindrome(numberToString(i*i))) {
				count++;
			}
		}
		
		// Print outcome
		cout << "Case #" << (num+1) << ": " << count << endl;
	}
	return 0;
}

string numberToString(int n) {
	string s="";
	stringstream out;
	out << n;
	s+= out.str();
	return s;
}

bool isPalindrome(string possiblePalindrome) {
	int len=possiblePalindrome.length();
	for(int i=0;i<len/2;i++) {
		if(possiblePalindrome[i]!=possiblePalindrome[len-1-i]) {return false;}
	}
	return true;
}