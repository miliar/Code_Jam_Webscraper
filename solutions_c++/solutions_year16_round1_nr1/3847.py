#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>
#include <deque>

using namespace std;

int main() {
	
	ifstream input("A-large.in");
	ofstream output("A-large.out");

	int T; //test cases
	input >> T;
	for (int i = 1; i <= T; ++i){
		string word;
		input >> word;
		deque<char> lastWord;
		char lastLetter;
		for (auto a : word) {
			if (lastWord.size() == 0) {
				lastWord.push_front(a);
			}
			else{
				if (a >= lastWord.front()) {
					lastWord.push_front(a);
				}
				else{
					lastWord.push_back(a);
				}
			}
		}

		string lastWordStr = "";
		for (auto iter = begin(lastWord); iter != end(lastWord); ++iter){
			lastWordStr += *iter;
		}

		output << "Case #" << i << ": " << lastWordStr << endl;

	}
	output.close();

	return 0;
}