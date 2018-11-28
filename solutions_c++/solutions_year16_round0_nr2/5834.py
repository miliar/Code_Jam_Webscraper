#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

unsigned int count_happy(string stack) {
	int sum = 0;
	for(unsigned int i =0;i<stack.length();i++) {
		if (stack[i] == '+') {
			sum++;
		}
	}
	return sum;
}

/**
 * flip from top to index
 */
void flip_stack(string& stack, int index) {
	int i=0;
	for(;i<=index;i++) {
		stack[i] = (stack[i] == '-' ? '+' : '-');
	}
}

int main() {
    std::ifstream fin("B-large.in");
  //  std::stringstream fin("5 - -+ +- +++ --+-");
	std::ofstream fout("B-large.out");
//	std::ifstream fin("A-small.in");
//	FILE *fout = freopen("A-small.out", "w", stdout);
	int T;
	string add;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "*******\n";
		string stack;
		int i,flips,sum;
		flips = 0;
		sum = 0;
		fin >> stack;
		int length = stack.length();
		for (i = length-1;i>=0;i--) {
			if (stack[i] == '+') {
				sum++;
			} else {
				flip_stack(stack, i);
				cout << stack << endl;
				flips++;
			}
			if (count_happy(stack) == stack.length()) {
				break;
			}
		}
		ostringstream convert;
		convert << flips;
		fout << "Case #" << t << ": ";
		fout << convert.str() << endl;
	}
	//exit(0);

	return 0;
}




