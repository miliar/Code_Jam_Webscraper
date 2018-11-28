#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void main(){
	//Number of test cases
	int t;
	cin >> t;
	
	//Run test cases
	cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
	for (int i = 1; i <= t; i++){
		//Input pancake stack
		string pancakeStack;
		getline(cin, pancakeStack);
		
		//Count number of flips
		//It works by groupings of same type of pancake
		//1. Count number of groupings
		//2. If stack ends with happy face up, result is numGroupings - 1
		//   Else if stack ends with happy face down, result is numGroupings
		int numGroupings = 1;
		char currentSymbol = pancakeStack[0];
		int currentPancakeIndex = 1;
		while (currentPancakeIndex < pancakeStack.length()){
			if (pancakeStack[currentPancakeIndex] != currentSymbol){
				numGroupings++;
				currentSymbol = pancakeStack[currentPancakeIndex];
			}
			
			currentPancakeIndex++;
		}
		
		int numFlips = numGroupings;
		if (currentSymbol == '+'){
			numFlips -= 1;
		}
		
		cout << "Case #" << i << ": " << numFlips << endl;
	}
}
