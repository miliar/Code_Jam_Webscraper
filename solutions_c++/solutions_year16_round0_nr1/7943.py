#include <iostream>


using namespace std;


int main() {
	int test_case, startingNumber, result;
	int digitList[10], matched;
	freopen("A-large.in","r",stdin);
	
	cin >> test_case;
	
	for (int curCase = 1; curCase <= test_case; curCase++) {
		cin >> startingNumber;
		result = 0;
		matched = 0;
		
		// Reset the digit list fisrt
		for (int i = 0; i < 10; i ++) {
			digitList[i] = 0;
		}
		
		// Algorithm implementation
		if (startingNumber != startingNumber * 2) {
			for (int i = 1; i < 1000; i ++) {
				result = startingNumber * i;
				int temp = result;
				int curDigit = 0;
				while (temp > 0) {
					curDigit = temp % 10;
					if (digitList[curDigit] == 0) {
						matched++;
						digitList[curDigit] = 1;
						if (matched == 10) {
							break;
						}
					}
					temp = temp/10;	
				}
				if (matched == 10)
							break;
			}
		}
		
		if (result != 0)
			cout << "Case #" << curCase << ": " << result << endl; 
		else
			cout << "Case #" << curCase << ": INSOMNIA" << endl;  
	}
	
	return 0;
}
