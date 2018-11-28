#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int GetSolution(char*);

int main(void) {
	int t, nResult;
	char buf[101] = { 0, };
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> buf;// >> m;  // read n and then m.

		nResult = GetSolution(buf);

		cout << "Case #" << i << ": ";
		cout << nResult << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}

	return 0;
}

void Flip(char* buf, int nCount) {
	int nLastPos = nCount-1;
	for (int i=0; i<nCount/2; i++) {
		char temp = buf[i];
		buf[i] = buf[nLastPos-i];
		buf[nLastPos-i] = temp;
	}
	for (int i=0; i<nCount; i++) {
		buf[i] = (buf[i] == '+') ? '-' : '+';
	}
}

int GetSolution(char* buf) {
	int nRet = 0;

	int nLength = strlen(buf);

	for (int i=0; i<nLength-1; i++) {
		// check
		if (buf[i] != buf[i+1]) {
			// flip
			Flip(buf, i+1);
			nRet++;
		}
	}
	if (buf[0] == '-') {
		//Flip(buf, nLength);
		nRet++;
	}

	return nRet;
}
