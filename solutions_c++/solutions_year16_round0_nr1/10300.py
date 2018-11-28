#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	
	ifstream inputFile ("A-large.in");
	string line;
	int T, N;
	
	if (inputFile.is_open()) {
		// Read the first line and assign to T: number of test cases
		getline (inputFile, line);
		stringstream ss(line);
		ss >> T;
		ss.clear();
		
		//cout << T << endl;
		
		// Go through each test case
		for (int i = 1; i <= T; i++) {
			getline (inputFile, line);
			stringstream ss(line);
			ss >> N;
			
			int j = 1;
			vector<int> digits;
			
			if (N == 0)
				cout << "Case #" << i << ": INSOMNIA" << endl;
			else {
				// Loop to check each N*j for digits
				while ((find(digits.begin(), digits.end(), 0) == digits.end()) || (find(digits.begin(), digits.end(), 1) == digits.end()) ||
						(find(digits.begin(), digits.end(), 2) == digits.end()) || (find(digits.begin(), digits.end(), 3) == digits.end()) ||
						(find(digits.begin(), digits.end(), 4) == digits.end()) || (find(digits.begin(), digits.end(), 5) == digits.end()) ||
						(find(digits.begin(), digits.end(), 6) == digits.end()) || (find(digits.begin(), digits.end(), 7) == digits.end()) ||
						(find(digits.begin(), digits.end(), 8) == digits.end()) || (find(digits.begin(), digits.end(), 9) == digits.end())) {
									
						int temp = N*j;
				
						while (temp) {
							digits.push_back(temp % 10);
							temp /= 10;
						}
						
						//cout << N*j << endl;
						
						j++;
			}
			
			ss.clear();
			cout << "Case #" << i << ": " << N*(j-1) << endl;
				
				
				
				
			}
			
			
		}
		
		inputFile.close();
	}
	else cout << "Unable to open file.";
	
	
	//system("pause");
	return 0;
}
