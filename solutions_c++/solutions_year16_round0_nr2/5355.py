#include <iostream>
#include <string>

using namespace std;

unsigned long long getManeuverNumber(string str){
	unsigned long long result = 0;
	bool happy = true;
	int i = str.size() - 1;
	
	if(i == -1) {
		return 0;
	}

	if (str[i] == '-') {
		++result;
		happy = false;
	} 

	--i;
	
	while (i != -1) {
		if (str[i] == '-') {
			if (happy) {
				++result;
				happy = false;
			}
		} else if (!happy) {
			++result;
			happy = true;
		}

		--i;
	}

	return result;
}

int main() {
	ios::sync_with_stdio(false);

	int T;
	int caseNumber = 1;
	string input;
	cin >> T;

	if (T == 0) {
		return 0;
	}
	++T;
	while (caseNumber != T) {
		cin >> input;
		cout << "Case #" << caseNumber <<  ": " <<  getManeuverNumber(input) << "\n";
		++caseNumber;
	}
	return 0;
}