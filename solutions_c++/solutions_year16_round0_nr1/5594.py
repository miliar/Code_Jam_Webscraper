// Shintero
//Problem A. Counting Sheep
#include <iostream>
#include <cstdio>
using namespace std;

long long nOfTests;

int main() {
	ios_base::sync_with_stdio(0);
	
	cin >> nOfTests;
	
	for (long long i = 1; i <= nOfTests; i++) {
		long long startingNumber, counter, currentNumber;
		bool visitedNumbers[10];
		counter = 10;
		
		for (long long j = 0; j < 10; j++) {
			visitedNumbers[j] = false;
		}
		
		cin >> startingNumber;
		
		currentNumber = startingNumber;
		
		if (startingNumber == 0) {
			cout << "Case #" << i << ": INSOMNIA\n";
		}
		else {
			while(counter != 0) {
				int aux = currentNumber;
				
				while(aux != 0) {
				    if (visitedNumbers[aux % 10] == false) {
				    	visitedNumbers[aux % 10] = true;
				    	counter--;
					}
				
				    aux /= 10;
				}
				
				if(counter != 0) {
				    currentNumber += startingNumber;
				}
			}
		
		    cout << "Case #" << i << ": " << currentNumber << "\n";
		}
	}
	
	return 0;	
}
