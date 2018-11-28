#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>
using namespace std;

unsigned long long GetNumberOfDigits(unsigned long long i)
{
	return i > 0 ? (int)log10((double)i) + 1 : 1;
}

string getN(long long number)
{
	if (number == 0)
		return "INSOMNIA";
	//get number.
	long long n = number;
	long long lastNumber = number,originalNumber=number;
	bool all[10] = { false };
	bool foundFlag = false;
	int ctr = 1;
	vector<int>digits;
	//repeat the process until either we get all digits or we get reach the max
	while (n <= INT_MAX){
		lastNumber = n;
		// split their digits
		int digitcount = GetNumberOfDigits(n);
		//cout << "Number= " << n << " ,Number of digits = " << digitcount << endl;
		while (digitcount != 0){
			digits.push_back(n % 10);
			n /= 10;
			digitcount--;
		}
		
		//check if we have all numbers in basket.

		for (int x = 0; x < digits.size(); x++)
		{
			for (int m = 0; m < 10; m++){
				if (digits.at(x) == m){
					all[m] = true;
					break;
				}
			}
		}

		bool AllFoundflag = true;
		for (int x = 0; x < 10; x++)
		{
			if (all[x] == false){
				AllFoundflag = false;
				break;
			}
		}
		n = originalNumber*ctr++;
		if (AllFoundflag == true){
			foundFlag = true;
			break;;
		}
		//cout << "n  = " << n << endl;
		//cout << "lastnumber = " << lastNumber << endl;
		

	}

	if (foundFlag == false){
		return "INSOMNIA";
	}
	else{
		return to_string(lastNumber);
	}
	
}

int main()
{
	ifstream inFile("A-large.in");
	ofstream output("outputLarge.txt");

	int T;

	inFile >> T;
	for (int x = 0; x < T; x++){
		long n;
		inFile >> n;
		output << "Case #" << x+1 << ": " << getN(n) << endl;
	}
	return 0;
}

