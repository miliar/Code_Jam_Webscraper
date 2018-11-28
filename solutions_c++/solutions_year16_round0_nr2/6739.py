#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    unsigned int n;
    ios::sync_with_stdio(false);
    
    cin >> n;
    for (unsigned int i = 0; i < n; i++) {
	string stack;
        cin >> stack;
	
	unsigned int len = stack.size();
	unsigned int turn = 0;
	char c = stack[0];
	for (unsigned int j = 1; j < len; j++) {
	    if (stack[j] != c) {
		turn++;
		c = stack[j];
	    }
	}
	if (c == '-') {
	    turn++;
	}
      
        cout << "Case #" << i+1 << ": " << turn << endl;
    }
    return 0;
}