// cat input.in | ./a.out > output
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


typedef long long myint;

template <typename T>
std::vector<T> read_vector(int length, std::istream& in = std::cin) {
	std::vector<T> vector;
	for(; length>0; length--) {
		T item;
		in >> item;
		vector.push_back(item);
	}
	return vector;
}




void flip(std::string &stack, int n) { // flip first n pancakes
	std::reverse(stack.begin(), stack.begin()+n);
	for(int i=0; i<n; i++) {
		stack[i] = (stack[i] == '+' ? '-' : '+');
	}
	//std::cerr << "Flipped to " << stack << std::endl;
}


// has to print everything except "Case #n: " and eol \n
// read from std::cin
void handle_case() {
	std::string stack;
	std::cin >> stack;
	
	int num_moves = 0;
	int first_unhappy = 0;
	int last_unhappy = stack.size()-1; // bottommost
	while(last_unhappy>=0) {
		if(stack[last_unhappy] == '+') {
			last_unhappy--;
			continue;
		}
		if(first_unhappy < stack.size() && stack[first_unhappy] == '+') {
			first_unhappy++;
			continue;
		}
		
		// flip pancakes
		if(first_unhappy > 0) {
			flip(stack, first_unhappy);
			num_moves++;
		}
		flip(stack, last_unhappy+1);
		num_moves++;
		
		first_unhappy = 0;
	}
	std::cout << num_moves;
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
