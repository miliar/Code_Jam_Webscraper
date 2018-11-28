#include <iostream>
#include <string>
#include <cstdlib>
#include <sstream>

using namespace std;

string last_num(string line);

int main() {
	int num_test_cases;
	string line;
	getline(cin, line);
	istringstream convert(line);
	convert >> num_test_cases;
	//cout << "Num cases: " << num_test_cases << endl;
	for (int i = 0; i < num_test_cases; i++) {
		getline(cin, line);
		string answer = last_num(line);
		cout << "Case #" << i+1 << ": " << answer << endl;
	}
	return 0;
}

string last_num(string line) {
	long num = stoi(line);

	if (num == 0) {
		return "INSOMNIA";
	}
	bool *has_seen;

	// Start off with all digits = 0
	has_seen = (bool*) calloc(10, 1);

	int i = 1;
	// Continue to multiply 
	while(true) {
		long num_c = num * i;

		// Get string of candidate
		string str_c;
		ostringstream convert;
		convert << num_c;
		str_c = convert.str();

		// Add seen digits 
		for (unsigned i = 0; i < str_c.size(); i++) {
			int digit = str_c[i] - '0';
			has_seen[digit] = 1;
		}

		// Print bool array
		/*
		cout << "[";
		for (int i = 0; i < 9; i++) {
			cout << has_seen[i] << ", ";
		}
		cout << has_seen[9] << "]" << endl;
		*/
	
		// Check if bool array filled
		bool filled = 1;
		for (int i = 0; i < 10; i++) {
			if  (!has_seen[i]) {
				filled = 0;
			}
		}

		if (filled) {
			//cout << "filled" << endl;
			return str_c;
		}

		//if (i > 5) { return "end\n"; }
		i++;
	}
}
