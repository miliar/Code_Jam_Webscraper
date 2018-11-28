#include <iostream>
#include <cstring>
#include <cstdlib>
#include <sstream>

using namespace std;


void solve_case(string stack, int case_num) {
  	stringstream answer;

  	int flips = 0;
  	int index = 0;

  	char currChar = stack.at(0);

  	while (++index < stack.size()) {
  		if (currChar != stack.at(index)) {
  			currChar = stack.at(index);
  			flips++;
  		}
	}
	if (currChar == '-') flips++;

	answer << flips;

  	cout << "Case #" << case_num+1 << ": " << answer.str() << "\n";
}

int main() {
  	int T;
  	cin >> T;
  	for (int i = 0; i < T; i++) {
		string stack;
		cin >> stack;
   	 	solve_case(stack, i);
  	}
}



