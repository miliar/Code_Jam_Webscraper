#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

typedef vector<bool>::iterator iter;

void flip(iter beg, iter end) {
	for(iter i = beg; i < end; i++) {
		*i = !*i;
	}
	reverse(beg, end);
}

int fix(iter beg, iter end) {
	if(beg >= end) {
		return 0;
	} else if(*(end-1)) {
		return fix(beg, end-1);
	} else if (*beg) {
		iter temp=beg;
		while(*temp && temp < end) temp++;
		if(temp == end) return 0;
		flip(beg, temp);
		return 1 + fix(beg,end);
	} else {
		flip(beg, end);
		return 1 + fix(beg, end-1);
	}
}

int main() {
	ofstream out;
	ifstream in;

	const string name = "large";

	out.open(name+".out");
	in.open(name+".in");

	int T;
	in >> T;

	for(int i = 1; i <= T;i++) {
		vector<bool> stack;
		string tempIn;
		out << "Case #" << i << ": ";

		in >> tempIn;
		for(char c : tempIn) {
			if(c == '+') {
				stack.push_back(true);
			} else {
				stack.push_back(false);
			}
		}

		out << fix(stack.begin(), stack.end()) << endl;
	}
}