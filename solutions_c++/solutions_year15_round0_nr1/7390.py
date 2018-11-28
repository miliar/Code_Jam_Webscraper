#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

void outputResult(ostream& ofile, int c, int m){
	ofile << "Case #" << c << ": " << m << endl;
}

int main(int argc, char* argv[]){
	
	ofstream ofile(argv[2]);
	ifstream myfile(argv[1]);    
    string myline;
    getline(myfile, myline);
    istringstream iss(myline);
	int cases; 
	iss >> cases;
	cout << cases << endl;
	int max;
	string input;
	getline(myfile, myline);
	iss.str(myline);
	iss.clear();
	
	for(int i = 0; i < cases; i++){
		getline(myfile, myline);
		iss >> max;
		iss >> input;
		cout << endl << max << " " << input << endl;
		iss.str(myline);
		iss.clear();
		int needed = 0;
		int aud = 0;
		for(int j = 0; j <= max; j++){
			cout << "j: " << j << endl << "input: " << input[j] << "aud: " << aud << endl;
			if(input[j] > 0 && j > aud){
				if(j - aud > needed){
					needed = j - aud;
				}
			}
			aud += input[j] - '0';
		}
		outputResult(ofile, i+1, needed);
	}


	return 0;
}