#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	string vowels("aeiou");
	int cases = 0;
	cin >> cases;
	for (int caseNum = 1; caseNum <= cases; caseNum++) {
		char dummy[100];
		cin.getline(dummy, 99);
		vector<char> name;
		char temp;
		while (true) {
			cin.get(temp);
			if (temp == ' ')
			break;
			name.push_back(temp);
		}
		int N = 0;
		cin >> N;
		long length = name.size();
		long nVal =0;
		long currentStart = 0;
		long conCons = 0; // # of consecutive consonants to this point
		if (N == 0)
			nVal = length * (length + 1) / 2L;
		else {
		for (int pos = 0; pos < (long)name.size(); pos++) {
			if (vowels.find_first_of(name.at(pos)) == string::npos) {
				conCons += 1;
			}
			else {
				conCons = 0;
			}
			if (conCons >= N) {
				nVal += (length - pos) * (2 + pos - N - currentStart);
				currentStart = 2 + pos - N;
			}
		}//for pos
		}// if N == 0
		cout << "Case #" << caseNum << ": " << nVal << endl;
	}
	return 0;
}
