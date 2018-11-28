#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <unordered_set>

using namespace std;

int main() {
	
	ifstream input("A-large.in");
	ofstream output("output-large.txt");

	int T; //test cases
	input >> T;
	for (int i = 1; i <= T; ++i) {
		int num;
		string str;
		input >> str;
		num = std::stoi(str);
		int numJ = num;
		int numDigits = str.length();
		unordered_set<int> digits;
		
		if (num == 0) {
			output << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
		else {
			for (int j = 1; digits.size() < 10; ++j) {
				numJ = num * j;
				str = to_string(numJ);
				for (auto c : str) {
					digits.insert(atoi(&c));
				}
			}
			output << "Case #" << i << ": " << numJ << endl;
		}
	}
	output.close();

	return 0;
}