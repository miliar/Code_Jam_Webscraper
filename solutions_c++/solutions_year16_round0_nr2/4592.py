#include <iostream>
#include <string>
using namespace std;
bool checkHappySide(string S) {
	for (int i = 0; i < S.length(); i++) {
		if (S.at(i) == '-')
			return false;
	}
	return true;
}
void reverseSide(string &S, int end) {
	switch (S.at(0)) {
	case '+':
		for (int i = 0; i < end; i++)
			S.at(i) = '-';
		break;
	case '-':
		for (int i = 0; i < end; i++)
			S.at(i) = '+';
		break;
	}
}
int main(void) {
	int T;
	string S;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> S;
		int count = 0;
		while (!checkHappySide(S)) {
			char currentSide = S.at(0);
			int j;
			for (j = 1; j < S.length(); j++) {
				if (currentSide != S.at(j))
					break;
			}
			reverseSide(S, j);
			count++;
		}
		cout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}