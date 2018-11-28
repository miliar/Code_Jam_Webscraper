#include <iostream>     //std::vector
#include <fstream>      //std::cout and std::cin
#include <vector>       //std::vector
#include <algorithm>    //std::unique, std::distance
#include <sstream>      //std::ostringstream
#include <limits.h>     //INT_MAX

using namespace std;

int main(int argc, char ** argv)
{
	std::ifstream infile(argv[1]);
	std::ofstream outfile(argv[2]);

	if(!infile) {
		std::cout << "could not open " << infile << std::endl;
		return 0;
	}
	if(!outfile) {
		std::cout << "could not open " << outfile << std::endl;
		return 0;
	}

	unsigned short numberOf_testCases;
	unsigned int N;
	unsigned short countIteration;
	unsigned int latestNumber;
	std::string counted_digits; //Counted Digits

	infile >> numberOf_testCases;    //Number of Test Cases
	for(unsigned int i=1; i<=numberOf_testCases; i++) {
		infile >> N;            //N

		latestNumber = -N;
		bool breakedBool = false, firstIteration = true;
		counted_digits = "";
		if (N == 0) {
			outfile << "Case #" << i;
			outfile << ": INSOMNIA" << endl;
			continue;
		}
		while (true) {
			if (firstIteration) {latestNumber = N; firstIteration = false;}
			else latestNumber = latestNumber + N;

			ostringstream os; os << latestNumber;
			counted_digits = counted_digits + os.str();
			std::sort(counted_digits.begin(), counted_digits.end());
			counted_digits.erase( unique( counted_digits.begin(), counted_digits.end() ), counted_digits.end() );

			if (counted_digits.length() >= 10) {
				outfile << "Case #" << i;
				outfile << ": " << latestNumber << endl;
				breakedBool = true;
				break;
			}
		}
		if (!breakedBool) {
			outfile << "Case #" << i;
			outfile << ": INSOMNIA" << endl;
		}
	}

	return 0;   
}