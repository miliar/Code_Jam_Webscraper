#include <iostream>

using namespace std;

int handleCase();

int main() {
    int T, S;
    cin >> T;
    for (int casenum=0; casenum < T; casenum++) {
    	int turns = handleCase();
		cout << "Case #" << (casenum + 1) << ": " << turns << endl;   
    }
    return 0;
}

int handleCase() {
	string cookieStack;
	cin >> cookieStack;
	int i = 0, len = cookieStack.length();

	int turns = 0;
	char last = 'x';  
	while (i < len) {
		if (cookieStack[i] != last) {
			if(cookieStack[i] == '-') {
				if (last == 'x') {
					turns += 1;
				}
				else if (last == '+') {
					turns += 2;
				}
			}
		} 

		last = cookieStack[i];
		i++;
	}

	return turns;
}