#include <iostream>
#include <map>
#include <set>
#include <deque>


int main() { int cases; std::cin >> cases; std::cin.get(); // skip endline
	for (int n = 1; n <= cases; ++n) { std::cout << "Case #" << n << ": "; {
		std::string str; std::cin >> str;
		std::set<std::string> state;
		state.insert("");
		for (size_t i = 0; i < str.size(); ++i) {
			std::set<std::string> newState;
			for (auto s : state) {
				newState.insert(s + str[i]);
				newState.insert(str[i] + s);
			}
			// state.swap(newState);
			state.clear();
			state.insert( *newState.rbegin() );
			// std::cout << "X:" << str[i] << std::endl;
		}
		std::cout << *state.rbegin();
	}	std::cout << std::endl; }
}
