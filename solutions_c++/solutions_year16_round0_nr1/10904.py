#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void printArray(bool array[], int iterValue){
	cout << iterValue << ": Array values [";
	for (int i = 0; i < 10; ++i)
	{
		cout << array[i] << " ";
	}
	cout << "\b]" << endl;
}

string BleatrixSleep(int input){
	int increment = input;
	bool knownDigits[10] = {false};
	bool digitCountSucceeded = false;

	if(input == 0){
		return "INSOMNIA";
	}
	
	while(!digitCountSucceeded){
		// printArray(knownDigits, input);
		int digitCount = 0;

		stringstream ss;
		ss << input;
		string s = ss.str();
		// cout << input << ":" << s <<  " :: "; 
		for (int i = 0; i < s.length(); i++)
		{
			short digit = (s[i] - '0');
			// cout << digit << " ";
			knownDigits[digit] = true;
		}
		// cout << endl;
		// check whether test completes..
		for (int i = 0; i < 10; i++)
		{
			if(knownDigits[i]){
				digitCount++;
			}
			if(digitCount >= 10){
				digitCountSucceeded = true;
			}
		}
		input += increment;
	}

	stringstream ss;
	ss << input - increment;
	string s = ss.str();
	return s;
}

int main() {
  int t, n;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    // cout << ":::::::::::::::" << n << endl;
    cout << "Case #" << i << ": " << BleatrixSleep(n) << endl;
  
  
  }

  return 0;
}