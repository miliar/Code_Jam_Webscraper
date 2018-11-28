// Shintero
// Problem B. Revenge of the Pancakes
#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int numberOfTests;

bool checkPancakes(string pancakesStack) {
	for(int i = 0; i < pancakesStack.length(); i++) {
		if (pancakesStack[i] == '-') {
			return false;
		}
	}
	
	return true;
}

int main() {
	ios_base::sync_with_stdio(0);
	
	cin >> numberOfTests;
	
	for (int i = 1; i <= numberOfTests; i++) {
		string currentPancakes;
		int numberOfMoves = 0, pancakesSize;
		
		cin >> currentPancakes;
		pancakesSize = currentPancakes.length();
		
		if (checkPancakes(currentPancakes) == true) {
			cout << "Case #" << i << ": " << numberOfMoves << "\n";
		}
		else {
			do {
				char sign = currentPancakes[0];
				
				for(int j = 1; j < pancakesSize; j++) {
					if(currentPancakes[j] != sign ) {
						for(int k = 0; k < j; k++) {
							if (sign == '-') {
								currentPancakes[k] = '+';
							}
							else {
								currentPancakes[k] = '-';
							}
						}
						
						numberOfMoves++;
						break;
					}
				}
			
			bool is = true;
			for (int j = 0; j < pancakesSize; j++) {
				if (currentPancakes[j] == '+') {
					is = false;
				}
			}
			
			if (is) {
				numberOfMoves++;
				for (int j = 0; j < pancakesSize; j++) {
					currentPancakes[j] = '+';
				}
			}
				
			} while (checkPancakes(currentPancakes) == false);
		
		cout << "Case #" << i << ": " << numberOfMoves << "\n";
		}
	}
	
	return 0;
}
