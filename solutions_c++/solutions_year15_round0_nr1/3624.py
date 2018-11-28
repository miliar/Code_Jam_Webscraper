#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int ctoi( char ch ) {
	return ch - '0';
}

int main() {
	ifstream cin("a.in");
	ofstream cout("a.out");

	int caseCount;
	cin >> caseCount;

	caseCount++;
	for (int casei = 1; casei < caseCount; casei++) {
		int result = 0;

		int len;
		string data;
		cin >> len >> data;

		int standers = 0;

		len++;
		for (int k = 0; k < len; k++) {
			int currStanders = ctoi(data.at(k));

			if (k >= standers && currStanders != 0) {
				int invitedStanders = k - standers;

				result += invitedStanders;
				standers += invitedStanders;
			}

			standers += currStanders;
		}

		cout << "Case #" << casei << ": " << result << endl;
	}

    return 0;
}
