#include <iostream>
#include <string>

void print_stack(bool* stack, int stack_size) {
	for (int i=0; i < stack_size; i++) {
		if (stack[i])
			std::cout << "+";
		else
			std::cout << "-";
	}
};


int main() {
	int T, t;
	std::cin >> T;
	
	for (t=0; t < T; t++ ) {
		std::string input;
		std::cin >> input;
		bool stack[input.length()];
		
		//Assign input sting to boolean stack representation
		//True = Happy
		//False = Blank

		for (int i=0; i < input.length(); i++) {
			if (input.at(i)=='+')
				stack[i] = true;
			else if (input.at(i)=='-')
				stack[i] = false;
			else std::cout << "Oopsie" << std::endl;
		}

		// Start Flipping
		//std::cout << "Inital Stack: ";
		//print_stack(stack, input.length());
		//std::cout << std::endl;
		int flips=0;
		for (int i=input.length()-1; i>=0; i--) {
			if (stack[i] == false) {
				for (int p=0; p <= i; p++) {
					stack[p] = !stack[p];
				}
				//std::cout << "Flip #" << flips << ": ";
				//print_stack(stack, input.length());
				//std::cout << std::endl;
				flips++;
			} else {
				//std::cout << "No Flip" << std::endl;
			}
		}
		std::cout << "Case #" << t+1 << ": " << flips << std::endl;
	}
	return true;
}
