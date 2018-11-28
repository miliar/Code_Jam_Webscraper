#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool isPalindrome(long long A) {
	char buffer[200];
	string s = itoa(A, buffer, 10);
	int size = s.length();
	for(int i=0; i<size/2; i++) {
		if(s[i]!=s[size-1-i]) {
			return false;
		}
	}
	return true;
}

bool isSquare(long long A) {
	double real = sqrt(A);
	long long num = (long long) real;
	if((real==num)&&(isPalindrome(num))) return true;
	return false;
}

long long cal(long long A, long long B) {
	long long count = 0;
	for(int i=A; i<=B; i++) {
		if(isPalindrome(i)&&isSquare(i)) count++;
	}
	return count;
}

int main()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("C-small.out");
	long long T, A, B;
	in >> T;
	for(int i=0; i<T; i++) {
		in >> A >> B;
		out << "Case #" << i+1 << ": " << cal(A, B) << endl;
	}
	in.close();
	out.close();
	return 0;
}