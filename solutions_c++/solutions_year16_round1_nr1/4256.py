/*
Programmer: Xinran Zheng
Make a permutation of a word that's the last word
*/

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

void inputs(ifstream& input, ofstream& output) {
	int cases;
	string word;
	input >> cases;
	for (int i = 1; i <= cases; i++) {
		output << "Case #" << i << ": ";
		input >> word;
		string thing = "";
		thing.push_back(word[0]);
		for (int i = 1; i < word.size(); i++) {
			if (word[i] >= thing[0]) {
				thing.insert(thing.begin(), word[i]);
			}
			else {
				thing.push_back(word[i]);
			}
		}
		output << thing << endl;
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
