//#include "storeCredit.h"
//#include "reverseWords.h"
//#include "t9Spelling.h"
//#include "minimumScalarProduct.h"
//#include "milkshakes.h"

#include <set>
#include <algorithm>
#include <iostream>
#include <iterator>

void solve(int testcase) {
	std::set<short> a, b;
	short choice;
	std::cin >> choice;
	for (auto i = 0; i < 4; i++) {
		for (auto j = 0; j < 4; j++) {
			short buf;
			std::cin >> buf;
			if (i + 1 == choice)
				a.insert(buf);
		}
	}
	std::cin >> choice;
	for (auto i = 0; i < 4; i++) {
		for (auto j = 0; j < 4; j++) {
			short buf;
			std::cin >> buf;
			if (i + 1 == choice)
				b.insert(buf);
		}
	}
	std::set<short> c;
	std::set_intersection(a.begin(), a.end(), b.begin(), b.end(), std::inserter(c, c.begin()));
	std::cout << "Case #" << testcase << ": ";
	if (c.size() == 1)
		std::cout << *c.begin();
	else if (c.size() == 0)
		std::cout << "Volunteer cheated!";
	else
		std::cout << "Bad magician!";
	std::cout << std::endl;
}

void run() {
	int nTest;
	std::cin >> nTest;
	for (auto i = 0; i < nTest; i++) {
		solve(i + 1);
	}
}

int main() {
	//StoreCredit inst;
	//ReverseWords inst;
	//T9Spelling inst;
	//MinimumScalarProduct inst;
	//Milkshakes inst;
	//inst.run();
	run();
	return 0;
}
