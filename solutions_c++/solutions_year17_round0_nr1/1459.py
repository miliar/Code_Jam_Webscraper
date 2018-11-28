
#include <list>
#include <iostream>

void handle_case() {
	std::list<bool> pancakes;
	
	char c;
	while(true) {
		c = getchar();
		if(c == '+') pancakes.push_back(true);
		if(c == '-') pancakes.push_back(false);
		if(c == ' ') break;
	}
	int k;
	std::cin >> k;
	
	int flips = 0;
	while(pancakes.size() > 0) {
		if(pancakes.front()) {
			pancakes.pop_front();
		} else {
			if(pancakes.size() < k) {
				std::cout << "IMPOSSIBLE";
				return;
			} else {
				flips++;
				auto it = pancakes.begin();
				for(int i=0; i<k; i++) {
					*it = !(*it);
					it++;
				}
			}
		}
	}
	std::cout << flips;
}


int main() {
	int num_cases;
	std::cin >> num_cases;
	for(int tcase = 1; tcase <= num_cases; tcase++) {
		std::cout << "Case #" << tcase << ": ";
		handle_case();
		std::cout << std::endl;
	}
}


