#include <fstream>
#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int main(){
	ifstream file("test.txt", ifstream::in);
	ofstream outfile("result.txt", ofstream::out);
	string s;
	int testCases;
	file >> testCases;
	for(int i = 1; i <= testCases; ++i){
		long long num;
		file >> num;
		long mult = 1;
		unsigned int bitCheck = 1023;
		bool found = false;
		long long numTested;
		while(true){
			numTested = num * mult;
			long long testnum = num * mult;
			assert(testnum >= 0);
			while(true){
				
				int digit = testnum %10;
				
				bitCheck = bitCheck & ~(1 << digit);
				
				testnum /= 10;
				if(testnum == 0) break;
					
			}
			
			if(!bitCheck){
				found = true;
				break;
			}
			if(testnum == num){
				break;
			}
			++mult;
		}
		
		if(!found){
			cout << "Case #" << i << ": " << "INSOMNIA\n";
			outfile << "Case #" << i << ": " << "INSOMNIA\n";
		} else {
			cout << "Case #" << i << ": " << numTested << "\n";
			outfile << "Case #" << i << ": " << numTested << "\n";
		}
			
		
		
		
	}
	
	
	
}