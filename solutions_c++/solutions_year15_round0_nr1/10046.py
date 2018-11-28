#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	// your code goes here
	int numTests;
	cin >> numTests;
	
	for(int test = 0; test < numTests; ++test) {
		int maxShy;
		string shyLevels;
		cin >> maxShy >> shyLevels;
		
		int numStanders = 0;
		int numPlants = 0;
		for (int i = 0; i < shyLevels.size(); ++i) {
			if (numStanders < i) {
				numPlants += i - numStanders;
				numStanders = i;
			}
			
			numStanders += shyLevels[i] - '0';
		}
		
		cout << "Case #" << test + 1 << ": " << numPlants << endl;
	}
	
	return 0;
}