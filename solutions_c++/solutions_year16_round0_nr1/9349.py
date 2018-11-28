#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <iomanip>
#include <vector>

using namespace std;

bool checkDone(int digits[10]) {
 for (int i = 0; i < 10; ++i) {
 	if (digits[i] == 0) {
 		return false;
 	}
 }
 return true;
}

int main() {
	ifstream inData("small.in");
	ofstream outData("output-small.txt");
	int num;
	inData >> num;
	for(int i = 0; i < num; i++){
		int n;
		inData >> n;
		if (n == 0) { 
			outData << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		int digits[10] = { 0 };
		int current = 0;
		while (!checkDone(digits)) {
			current++;
			int temp = n*current;
			while (temp > 0) {
				int digit = temp % 10;
				digits[digit] = 1;
				temp /= 10;
			}
		}
		outData << "Case #" << i+1 << ": " << n*current << endl;
	}
	return 0;
}

