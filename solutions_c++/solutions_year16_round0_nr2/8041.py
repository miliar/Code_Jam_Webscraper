#include <iostream>
#include <cstring>


using namespace std;


int main() {
	int test_case, result, inputLength;
	string input;
	freopen("B-large.in","r",stdin);
	
	cin >> test_case;
	
	for (int curCase = 1; curCase <= test_case; curCase++) {
		cin >> input;
		result = 0;
		
		inputLength = input.length();
		// Algorithm implementation
		for (int i = 0; i < inputLength; i++) {
			if (input[i] == '-') {
				if (i == inputLength - 1)
					result++;
				if (i > 0 && input[i-1] == '+')
					result++;
			}
			if (i > 0 && input[i] == '+') {
				if (input[i - 1] == '-')
					result++;
			}
		}
				
		cout << "Case #" << curCase << ": " << result << endl; 
	}
	
	return 0;
}
