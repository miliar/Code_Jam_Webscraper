#include <iostream>
#include <algorithm>
#include <functional>
#include <iterator>
#include <string>
#include <bitset>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>

const unsigned N = 4;

const std::string BadMagician      = "Bad magician!";
const std::string VolunteerCheated = "Volunteer cheated!";

std::vector<unsigned> intersection(const std::vector<unsigned>& a, const std::vector<unsigned>& b) {
	std::vector<unsigned> c;
	
	if(a.size() < b.size()) {
		for(unsigned element : a) {
			if( std::find(b.begin(), b.end(), element) != b.end() )
				c.push_back(element);
		}
	} else {
		for(unsigned element : b) {
			if( std::find(a.begin(), a.end(), element) != a.end() )
				c.push_back(element);
		}
	}
	
	return c;
}

int main(void) {
	unsigned T;
	std::cin >> T;
	
	for(unsigned t=0; t<T; ++t) {
		unsigned d, p, q;
		std::vector<unsigned> cards1, cards2;
		
		std::cin >> p;
		for(unsigned r=0; r<N; ++r) {
			for(unsigned c=0; c<N; ++c) {
				std::cin >> d;
				if(r == p-1) cards1.push_back(d);
			}
		}
		
		std::cin >> q;
		for(unsigned r=0; r<N; ++r) {
			for(unsigned c=0; c<N; ++c) {
				std::cin >> d;
				if(r == q-1) cards2.push_back(d);
			}
		}
		
		std::vector<unsigned> cards = intersection(cards1, cards2);
		
		std::cout << "Case #" << (t+1) << ": ";
		if(cards.size() == 1) {
			std::cout << cards[0];
		}
		else if(cards.size() == 0) {
			std::cout << VolunteerCheated;
		}
		else {
			std::cout << BadMagician;
		}
		std::cout << std::endl;
	}
	
	return 0;
}
