#include <iostream>
#include <fstream>

using namespace std;

//This problem is equivalent to
//"count how many groups of pancakes there are"
//(ignoring any happy pancakes on the very bottom)

int main(int argc, char* argv[]) {
	if(argc != 2) {
		cout << "Usage: use this program correctly" << endl;
		return 0;
	}
	ofstream os("out.txt");
	ifstream is(argv[1]);
	int numTestCases;
	is >> numTestCases;
	is.get(); //burn newline
	for(int i = 1; i <= numTestCases; ++i) {
		os << "Case #" << i << ": ";
		char stack[256];
		is.getline(stack, sizeof(stack));

		int groups = 0;
		//setting to something other than '+' or '-'
		//so that first char is recognized as a group
		char prevChar = ' ';
		char currChar = ' ';
		char* it = stack;
		while(*it != '\0') {
			prevChar = currChar;
			currChar = *it;
			if(currChar != prevChar)
				++groups;
			++it;
		}
		//ignore happy pancakes on the very bottom
		if(currChar == '+')
			--groups;
		os << groups << endl;
	}
}