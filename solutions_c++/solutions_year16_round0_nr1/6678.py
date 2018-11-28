#include <iostream>
#include <set>
using namespace std;

void main(){
	//Number of test cases
	int t;
	cin >> t;
	
	//Run test cases
	for (int i = 1; i <= t; i++){
		//Input values
		int n;
		cin >> n;
		
		//Zero case
		if (n == 0){
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		
		//Iterate until all numbers 0 - 9 seen (10 numbers total)
		else{
			unsigned long multiplier = 1;
			set<int> seenNumbers;
			unsigned long currentNumber;
			while (seenNumbers.size() < 10){
				currentNumber = multiplier * n;
				unsigned long tempNumber = currentNumber;
				while (tempNumber > 0){
					seenNumbers.insert(tempNumber % 10);
					tempNumber /= 10;
				}
				
				multiplier++;
			}
			
			cout << "Case #" << i << ": " << currentNumber << endl;
		}
	}
}
