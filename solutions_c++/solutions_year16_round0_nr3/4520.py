#include <iostream>
#include <string>
#include <vector>
#include <algorithm> 

using namespace std;

string nextNumberPart(string * s) {
	return "";
}

void fillZeros(std::vector<string> * s, int length) {
	for (int i=0; i<length; i++) {
		(*s).push_back("0");
	}
}

string concat(std::vector<string> * s, int length) {
	string result = "";
	for (int i=0; i<length; i++) {
		result = result + (*s)[i];
	}	
	return result;
}

unsigned long int findDivisor(unsigned long int number) {
	int upto = number / 2;
	int start = 2;
	int result = 1;

	if(number % 2 == 0) {
		return 2;
	} else {
		for (int i=3; i<= upto; i=i+2) {
			if(number % i == 0) {
				result = i;
				break;
			}
		}
	}

	return result;
}


int main(int argc, char* argv[]) 
{
/*
	
	string mychars[] = {"0","0", "0", "0"};
	
	do {
	    std::cout << mychars[0] << mychars[1] << mychars[2] << mychars[3] << '\n';
	 } while ( std::next_permutation(mychars,mychars+4) );
	std::cout << mychars[0] << mychars[1] << mychars[2] << mychars[3] << '\n';
	*/		
	/*
	int base;
	string str, str1;
	cin >> str;
	cin >> base;
	int num = std::stoi(str, nullptr, base);
	cout << num << "\n";

	*/	

	int cases, length, Jdifferent, trackOneCount=0, base;
	unsigned long int baseResult[] = {0,1,2,3,4,5,6,7,8,9,10};
	string testStr, partStr;
	unsigned long int testNumber, testResult;
	cin >> cases;

	for(int i=1; i<=cases; i++) {
		cin >> length;
		cin >> Jdifferent;
		

		length = length - 2;
		std::vector<string> parts;
		//string parts[length];
		fillZeros(&parts, length);
		//cout << concat(&parts, length);

		//cout << "Case #" << i << ":\n";	

		while (Jdifferent > 0) {
			do { //Add 1 in parts
				do { //test all permutations
				    partStr = concat(&parts, length);
				    //cout << partStr << " : Part String  \n";
					testStr = "1" + partStr + "1";
					//cout << testStr << " : Test String  \n";
					for( base=2; base<=10; base++) {
						testNumber = std::stoul(testStr, nullptr, base);
						//cout<< testNumber << " Number \n";
						testResult = findDivisor(testNumber);
						//cout<< testResult << " Divisor \n";
						if(testResult == 1) {
							break;
						} else {
							baseResult[base] = testResult;
						}
					}
					//cout << " ************** BASE ********* " << base << "\n";
					if(base == 11 && testResult != 1) {
						cout << testStr << " " 
								<< baseResult[2] << " " 
								<< baseResult[3] << " " 
								<< baseResult[4] << " " 
								<< baseResult[5] << " " 
								<< baseResult[6] << " " 
								<< baseResult[7] << " " 
								<< baseResult[8] << " " 
								<< baseResult[9] << " " 
								<< baseResult[10] << "\n";
						Jdifferent--;
					}

					if(Jdifferent == 0) {
						break;
					}

				 } while ( std::next_permutation(parts.begin(),parts.end()) );


				if(Jdifferent == 0) {
						break;
				}

				parts[trackOneCount] = "1";
				trackOneCount++;
			} while(trackOneCount < length);

		}
	}

}