#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int GetSolution(int);

int main(void) {
	int t, n, nResult;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;// >> m;  // read n and then m.

		nResult = GetSolution(n);

		cout << "Case #" << i << ": ";
		if (nResult) 
			cout << nResult;
		else
			cout << "INSOMNIA";
		cout << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}

	return 0;
}

int GetSolution(int n) {
	int nRet = 0;
	bool arrDigits[10] = { false, };

	int nCount = 0;
	int nPrevSheepNumber = 0;
	while (true) {
		int nSheepNumber = ++nCount * n;
		if (nSheepNumber > nPrevSheepNumber) {
			nPrevSheepNumber = nSheepNumber;

			while (nSheepNumber > 0) {
				arrDigits[nSheepNumber % 10] = true;
				nSheepNumber /= 10;
			}

			if (arrDigits[0] && 
				arrDigits[1] && 
				arrDigits[2] && 
				arrDigits[3] && 
				arrDigits[4] && 
				arrDigits[5] && 
				arrDigits[6] && 
				arrDigits[7] && 
				arrDigits[8] && 
				arrDigits[9]) 
			{
				nRet = nPrevSheepNumber;
				break;
			}
		} else {
			break;
		}
	}

	return nRet;
}
