#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
char ch[150];
bool isPalindrome(int i) {
	int length = 0;
	while(i>0) {
		ch[length++] = i%10;
		i /= 10;
	}
	for (int j=0;j<length/2;j++) {
		if (ch[j] != ch[length-1-j]) return false;
	}
	return true;
}
bool isSquare(int i) {
	double sq = sqrt(i);
	if (sq == floor(sq) && isPalindrome(sq)) return true;
	else return false;
}
bool check(int i) {
	return isPalindrome(i) && isSquare(i);
}
int main () {
	int num,result,a,b;

	ifstream infile;
	infile.open ("D:/in.txt");
	ofstream outfile;
	outfile.open ("D:/C.txt");

	infile >> num;

	for (int i=1;i<=num;i++) {
		infile >> a; infile >> b;
		result= 0;
		for (int i=a;i<=b;i++) {
			if(check(i)) result++;
		}
		outfile << "Case #"<< i << ": " << result << endl;
		cout << "   " << i << endl;
	}

	outfile.close();
	infile.close();

	return 0;
}