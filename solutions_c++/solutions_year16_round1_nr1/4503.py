#include <fstream>
#include <string>
#include <iostream>
#include <bitset>
#include <list>

using namespace std;

int main() {
	ifstream in("C:/workplace/workspace/code-jam/tmp/1a/A-small-attempt1.in");
	ofstream out("C:/workplace/workspace/code-jam/tmp/1a/A-small-attempt1.out");

	int numTestCases;
	in >> numTestCases;

	for (int testCase = 1; testCase <= numTestCases; testCase++) {

		string letters;
		in >> letters;

		list<char> ans;
		string::iterator ch = letters.begin();
		ans.push_back(*ch++);
		for (; ch != letters.end(); ch++) {
			if (*ch >= ans.front()) {
				ans.push_front(*ch);
			}
			else {
				ans.push_back(*ch);
			}
		}
		out << "Case #" << testCase << ": ";
		
		for (list<char>::iterator ch = ans.begin(); ch != ans.end(); ch++) {
			out << *ch;
		}
		out << endl;
	}

	return 0;
}