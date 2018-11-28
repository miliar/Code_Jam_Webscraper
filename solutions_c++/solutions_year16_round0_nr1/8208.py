#include <iostream>
using namespace std;


int sleep_number(int num) {
	
	// declare 10 size array;
	int arr[10] = {0};
	
	int count = 1;
	
	int number = num;
	
	int flag = 0;
	
	int last_number;
	
	// numbers loop starting from num
	while(!flag) {
		
		// extract all digits in num
		last_number = number;
		
		//cout << last_number << endl;
		
		while(number > 0){
			
			int digit;
			digit = number % 10;
			number = number / 10;
			
			// mark true for all those digits in array positions
			arr[digit] = 1;
			
			// check if all true in array
			for (int j = 0; j < 10; j++) {
				if (arr[j] != 1) {
					// else go on
					break;
				}
				
				if ( j == 9 ) 
					flag = 1;
			}
			
		} // end 2nd while
		
		number = (count++) * num;
		
	}
	
	return last_number;
}

int main() {
	// declare variables
	int t, n;
	
	// input test cases
	cin >> t;
	
	// loop for test cases
	for ( int i = 1; i <= t; i++ ) {
		//inputs
		cin >> n;
		
		if (n == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA" <<endl;
		}
		else {
			// print ith test case result
			cout << "Case #" << i << ": " << sleep_number(n) <<endl;
		}
		
	}
	
	return 0;
} 