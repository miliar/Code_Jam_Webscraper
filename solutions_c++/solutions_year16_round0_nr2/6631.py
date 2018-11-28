#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int recursion(string str, char flipTo) {
	char leftTo = '+';
	char firstright = str[str.length()-1];
	int leftCount = 0;
	int rightCount = 0;
	if (firstright != flipTo ) {
		rightCount = 1;
	}
	if (flipTo == '+') {
		leftTo = '-';
	}

	for (int i = str.length()-2; i >=0; i--) {
		if (str[i] != firstright) {
			string newStr = str.substr(0,i+1);
			leftCount = recursion(newStr, leftTo);
			break;
		}
	}

	return leftCount+rightCount;
}

int optFlip(string str) {
	char leftTo = '+';
	char firstright = str[str.length()-1];
	int leftCount = 0;
	int rightCount = 0;
	if (firstright=='-') {
		leftTo = '-';
		rightCount = 1;
	}

	for (int i = str.length()-2; i >=0; i--) {
		if (str[i] != firstright) {
			string newStr = str.substr(0,i+1);
			leftCount = recursion(newStr, leftTo);
			break;
		}
	}

	return leftCount+rightCount;
}

int main() {
  int t;
  string str;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> str;  // read n and then m.
    int out = optFlip(str);
	cout << "Case #" << i << ": " << out << endl;
    
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}