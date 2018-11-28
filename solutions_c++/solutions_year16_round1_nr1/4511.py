// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int main () {
	string line;
	ifstream myfile ("A-small-attempt1.in");
	ofstream outfile;
	outfile.open ("output.txt");
	
	if (myfile.is_open())
	{
		getline (myfile,line);
		long long caseNum = 1;
		
		while ( getline (myfile,line))
		{
			
			std::string last_word = "";
			long long N = 0, J = 0;
			for(long long i = 0; i < line.size(); i++) {
				if(last_word.size() == 0) {
					last_word = line[i];
				} else if( line[i] >= last_word[0] ) {
					last_word = line[i] + last_word;
				} else {
					last_word += line[i];
				}
			}
			
			outfile << "Case #" << caseNum << ": " << last_word << "\n";
			cout << "Case #" << caseNum << ": " << last_word << "\n";
			caseNum++;
		}
		
		myfile.close();
	}
	else cout << "Unable to open file"; 
	
	return 0;
}
