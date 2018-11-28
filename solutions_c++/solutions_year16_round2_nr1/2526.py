#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

typedef vector<int> vi;

string text;
vi results;
vi vals;
int N;

void mark_string(string& pat, char unq, int digit) {
	bool found_pat = false;
	for (int i = 0; i < N; ++i) {
		if (text[i] == unq && vals[i] == 0) {
			found_pat = true;
			break;
		}
	}
	//cout << found_pat << endl;
	while(found_pat) {
		for (int j = 0; j < pat.size(); ++j) {
			bool found = false;
			for (int i = 0; i < N; ++i){
				if (text[i] == pat[j] && vals[i] == 0) {
					found = true;
					vals[i] = 1;
					break;
				}
			}
		}
		results.push_back(digit);

		found_pat = false;
		for (int i = 0; i < N; ++i) {
			if (text[i] == unq && vals[i] == 0) {
				found_pat = true;
				break;
			}
		}
		//cout << found_pat << endl;
	}
	

}

int main() {
	int T;
	int nt = 1;
	cin >> T;
	
	while(nt <= T) {
		cin >> text;
		N = text.size();
		results.clear();
		vals.clear();
		vals.assign(N, 0);
		
		vector<string> digits;
		vector<char> uniques;
		digits.push_back("ZERO");
		digits.push_back("ONE");
		digits.push_back("TWO");
		digits.push_back("THREE");
		digits.push_back("FOUR");
		digits.push_back("FIVE");
		digits.push_back("SIX");
		digits.push_back("SEVEN");
		digits.push_back("EIGHT");
		digits.push_back("NINE");
		
		//cout << "mark Z" << endl;
		mark_string(digits[0], 'Z', 0);
		//cout << "mark Z" << endl;
		mark_string(digits[4], 'U', 4);
		mark_string(digits[6], 'X', 6);
		mark_string(digits[8], 'G', 8);
		mark_string(digits[5], 'F', 5);
		mark_string(digits[7], 'V', 7);
		mark_string(digits[9], 'I', 9);
		mark_string(digits[3], 'H', 3);
		mark_string(digits[2], 'W', 2);
		mark_string(digits[1], 'N', 1);

		sort(results.begin(), results.end());
		cout << "Case #" << nt << ": ";
		for (int i = 0; i < results.size(); ++i)
		{
			cout << results[i];
		}
		cout << endl;
		nt++;
	}

	return 0;
}