#include <iostream>
#include <set>
using namespace std;

int main(){

	int no_of_tests = 1000000;
	cin >> no_of_tests;

	int test_index = 0;
	int input;
	int iterations;
	int current_number;
	int temp;

	while (test_index++ < no_of_tests){
		
		cin >> input;
	
		cout << "Case #" << test_index << ": ";

		if(input > 0){
			iterations = 1;
			set<int> numbers_seen;
			
			do{
				temp = current_number = input * iterations++;
				do{
					int digit = temp % 10;
					numbers_seen.insert(digit);
					temp = temp / 10;
				} while(temp > 0);
				
			} while(numbers_seen.size() < 10);

			cout << current_number;
		}
		else{
			cout << "INSOMNIA";
		}
		cout << endl;
	}
}