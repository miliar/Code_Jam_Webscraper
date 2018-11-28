/*
Programmer: Xinran Zheng
Falling asleep when counted all the digits
*/

#include <unordered_map>
#include <fstream>
#include <iostream>
using namespace std;

int counting(int number){
	unordered_map<int, int> digits;
	int digit;
	int counter = 0;
	int num = number;
	int num2 = number;
	while (true) {
		while (num > 0) {
			digit = num % 10;
			num = num / 10;
			if (digits.find(digit) == digits.end()) {
				//cout << digit << endl;
				digits[digit] = 0;
				counter++;
			}
		}
		if (counter == 10) {
			break;
		}
		else {
			num2 = num2 + number;
			num = num2;
		}
	}
	return num2;
}

void inputs(ifstream& input, ofstream& output) {
	int cases;
	int number;
	input >> cases;
	for (int i = 1; i <= cases; i++) {
		input >> number;
		output << "Case #" << i << ": ";
		if (number != 0) {
			output << counting(number) << endl;
		}
		else {
			output << "INSOMNIA" << endl;
		}
	}
}

int main() {
	ifstream input; 
	input.open("A-large.in");
	if (!input) {
		cerr << "Cannot open file";
		exit(0);
	}
	ofstream output;
	output.open("output.txt"); 
	inputs(input, output);
	input.close();
	output.close();
}