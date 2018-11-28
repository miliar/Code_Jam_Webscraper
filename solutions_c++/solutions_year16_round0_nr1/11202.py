#include<iostream>
#include<string>
#include<fstream>

using namespace std;

/*
Assumptions
1. n >= 0

*/
string lastNumSeen(int n) {
	if (n == 0)
		return string("INSOMNIA");
	else if (n < 0)
		return ("invalid number (test case)");


	int tempN, i = 1, count = 0, lastNumSeen, digtoCheck;
	bool seen[10];

	for (int i = 0; i < 10; i++)
		seen[i] = false;

	while (true) {
		tempN = i * n;
		lastNumSeen = tempN;

		while (tempN > 0) {

			digtoCheck = tempN % 10;
			if (!seen[digtoCheck]) {
				count++;
				seen[digtoCheck] = true;
			}
			tempN /= 10;

		}

		if (count >= 10)
			return to_string(lastNumSeen);

		i++;
	}

}

int main() {
	int testCaseCount, initialNumPicked;
	string line;

	cin >> testCaseCount;
	
	for (int i = 1; i <= testCaseCount; i++) {
		
		cin >> initialNumPicked;
		cout << "Case #" << i << ": " << lastNumSeen(initialNumPicked) << endl;
	}

	return 0;
}