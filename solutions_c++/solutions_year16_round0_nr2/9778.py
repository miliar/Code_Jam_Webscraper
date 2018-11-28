/*
Programmer: Xinran Zheng
Flipping pancakes until they are all + side up
*/

#include <vector>
#include <fstream>
#include <iostream>
using namespace std;

char opo(char thing) {
	if (thing == '+') {
		return '-';
	}
	return '+';
}

void flip(vector<char>& pancakes, int end) {
	int begin = 0;
	int index = 0;
	while (true) {
		if (pancakes[index] == '-') {
			break;
		}
		pancakes[index] = '-';
		index++;
	}
	while (begin < end) {
		char tmp = pancakes[begin];
		pancakes[begin] = opo(pancakes[end]);
		pancakes[end] = opo(tmp);
		begin++;
		end--;
	}
	if (begin == end) {
		pancakes[begin] = opo(pancakes[begin]);
	}
}

int findEnd(const vector<char>& pancakes, int end) {
	for (int i = end; i >= 0; i--) {
		if (pancakes[i] == '-') {
			return i;
		}
	}
	return -1;
}

void inputs(ifstream& input, ofstream& output) {
	int cases;
	string x;
	vector<char> pancakes;
	int counter;
	input >> cases;
	for (int i = 1; i <= cases; i++){
		output << "Case #" << i << ": ";
		input >> x;
		cout << x << endl;
		for (char pancake : x) {
			pancakes.push_back(pancake);
		}
		int end = pancakes.size();
		while (true) {
			end = findEnd(pancakes, end);
			if (end == -1) {
				break;
			}
			if (pancakes[0] == '+') {
				counter++;
			}
			flip(pancakes, end);
			counter++;
		}
		output << counter << endl;
		pancakes.clear();
		counter = 0;
	}
	
}

int main() {
	ifstream input; 
	input.open("B-large.in");
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