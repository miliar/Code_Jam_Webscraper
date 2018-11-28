#include <iostream>
#include <string>
using namespace std;


int main() {
	int cases;
	cin >> cases;
	for(int i = 1;i <= cases; ++i) {
		string stack;
		cin >> stack;
		int turn = 0;
		char last = '+';
		for(int j = stack.size() - 1; j >= 0; j--) {
			if(stack[j] != last) {
				last = stack[j];
				++turn;
			}
		}
		cout << "Case #" << i << ": " << turn << endl;
	}
}