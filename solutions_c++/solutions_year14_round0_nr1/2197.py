#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <streambuf>
#include <cstdint>
#include <assert.h>
#include <set>


int main() {

	int n;

	std::cin >> n;

	for(int _n=0; _n<n; ++_n) {
		std::cout << "Case #" << (_n+1) << ": ";

		int row, r=1;
		std::cin >> row;

		for(; r<row; ++r) {
			int dump;
			std::cin >> dump >> dump >> dump >> dump;
		}

		std::set<int> cards, f;
		for(int i=0; i<4; ++i) {
			int c;
			std::cin >> c;
			cards.insert(c);
		}

		for(++r; r<5; ++r) {
			int dump;
			std::cin >> dump >> dump >> dump >> dump;
		}

		r=1;

		std::cin >> row;

		for(; r<row; ++r) {
			int dump;
			std::cin >> dump >> dump >> dump >> dump;
		}

		for(int i=0; i<4; ++i) {
			int c;
			std::cin >> c;
			if(cards.find(c) != cards.end()) {
				f.insert(c);
			}
		}

		for(++r; r<5; ++r) {
			int dump;
			std::cin >> dump >> dump >> dump >> dump;
		}

		if(f.size() == 1) {
			std::cout << *f.begin() << std::endl;
		}
		else if(f.empty()) {
			std::cout << "Volunteer cheated!" << std::endl;
		}
		else {
			std::cout << "Bad magician!" << std::endl;
		}
	}



	return 0;
}