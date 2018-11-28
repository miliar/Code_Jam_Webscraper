#include <iostream>
#include <string>

using namespace std;

int caseNumber = 1;

void printLastName (unsigned long long num) {
	if (num == 0) {
		cout << "Case #" << caseNumber << ": " << "INSOMNIA" << "\n";
		return;
	}
	
	bool result[10] = {false,false,false,false,false,false,false,false,false,false};
	unsigned long long temp = num;
	string strRep;

	while (true) {
		strRep = to_string(num);
		
		for (unsigned int i = 0; i != strRep.size(); ++i) {
		
				result[strRep[i] - '0'] = true;
		}

		if (result[0] && result[1] && result[2] && result[3] && result[4] && result[5] && result[6] && result[7] && result[8] && result[9]) {
			break;
		}
		num += temp;
	}

	cout << "Case #" << caseNumber << ": " << num << "\n";

}

int main() {
	ios::sync_with_stdio(false);

	int T;
	unsigned long long num;

	cin >> T;
	if (T == 0) {
		return 0;
	}

	++T;
	
	while(caseNumber != T) {
		cin >> num;

		printLastName(num);
		++caseNumber;
	}

	return 0;
}