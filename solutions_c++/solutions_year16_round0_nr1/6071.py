// reading a text file
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
	string line;
	ifstream myfile ("A-small-attempt1.in");
	ofstream outfile;
	outfile.open ("output.txt");
	
	if (myfile.is_open())
	{
		getline (myfile,line);
		bool digitsSeen[10];
		int caseNum = 1, lastCase = line[0] - '0';
		std::cout << lastCase << std::endl;
		
		while ( getline (myfile,line))
		{
			int N = 0, digit, digitCount = 0;
		
			for(int i = 0; i < 10; i++) {
				digitsSeen[i] = false;
			}
			
			for(int i = 0; i < line.size(); i++) {
				digit = ((int)line[i] - '0');
				cout << digit;
				N *= 10;
				N += digit;
			}
			
			int tempN = N;
			while(digitCount < 10) {
				if(N == 0) {
					break;
				}
				
				int digitFinder = tempN;
				
				while(digitFinder && digitCount < 10) {
					digit = digitFinder % 10;
					
					if(!digitsSeen[digit]) {
						if(++digitCount >= 10) {
							outfile << "Case #" << caseNum << ": " << tempN << std::endl;
							std::cout << "Case #" << caseNum << ": " << tempN << std::endl;
						}
						digitsSeen[digit] = true;
					}
					
					digitFinder /= 10;
				}
				
				tempN += N;
			}
			
			if(digitCount < 10) {
				outfile << "Case #" << caseNum << ": INSOMNIA\n";
				std::cout << "Case #" << caseNum << ": INSOMNIA\n";
			}
			
			caseNum++;
		}
		myfile.close();
	}
	else cout << "Unable to open file"; 
	
	return 0;
}
