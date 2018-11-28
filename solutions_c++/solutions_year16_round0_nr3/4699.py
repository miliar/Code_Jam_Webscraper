#include <fstream>
#include <string>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <bitset>
#include <math.h> 
using namespace std;
	
std::vector<unsigned long> primeNumbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

unsigned long getDivisor(unsigned long num) {
	for (unsigned long x = 0; x < primeNumbers.size(); ++x) {
		if (num % primeNumbers[x] == 0) return primeNumbers[x];
	}
	
	unsigned long UPPER_LIMIT = sqrt(num);
	for (unsigned long x = primeNumbers.back(); x <= UPPER_LIMIT; x = x+2) {
		if(num % x == 0) return x;
	}

	primeNumbers.push_back(num);
	return 0;
}

unsigned long convertToBaseN(bitset<16> input, int base) {
	unsigned long newNumInBase = 0;

	for(int i = 0; i < 16; ++i) {
		if (input[i])
			newNumInBase += input[i] * pow(base, i);
	}
	
	return newNumInBase;
}

int main()
{
	ofstream myfile;
	myfile.open("output.txt");
	ifstream file("C-small-attempt0.in");
    string str;
    
    if (file) {
        getline(file, str);
        int T = atoi(str.c_str());
		getline(file, str);
		char *line = &str[0];
		int N = atoi(strtok(line, " "));
		int J = atoi(strtok(NULL, " "));
		
		unsigned long JAM_MIN = (0b1 << (N-1)) + 0b1;
		unsigned long JAM_MAX = pow(2.0, N) - 1;
		vector<unsigned long> divisors;

		myfile << "Case #" << T << ":" << endl;
		
		for (unsigned long jam = JAM_MIN, j = 0; j < J; jam = jam + 0b10) {

			int x;
			unsigned long div = 0;
			divisors.clear();

			for (x = 2; x <= 10; ++x) {
				div = getDivisor(convertToBaseN(jam, x));
				if(div == 0) break;
				divisors.push_back(div);
			}
			
			if (x > 10) {
				++j;
				std::bitset<16> bits(jam);
				myfile << bits;
				
				for (x = 0; x < 9; ++x) {
					myfile << " " << divisors[x];
				}
				
				myfile << endl;
			}
		}

    }
	myfile.close();
    return 0;
}