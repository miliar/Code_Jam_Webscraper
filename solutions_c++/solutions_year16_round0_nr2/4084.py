#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <unordered_set>

using namespace std;

int main() {
	
	ifstream input("B-large.in");
	ofstream output("output-large.txt");

	int T; //test cases
	input >> T;
	for (int i = 1; i <= T; ++i){
		string str;
		input >> str;
		int num = 0;
		int top = 0;
		for (unsigned int j = 0; j < str.size(); j++) {
			if (j == str.size() - 1) {
				if (str[j] == '-'){
					num += 1;
				}
			}
			else if (str[j] != str[j + 1]) {
				if (str[j] == '-') {
					num += 1;
				}
				else {
					num += 1;
				}
			}

		}
		
		output << "Case #" << i << ": " << num <<endl;

	}
	output.close();

	return 0;
}