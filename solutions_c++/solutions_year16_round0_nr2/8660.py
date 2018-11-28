#include <iostream>
#include <string>
#include <fstream>

using namespace std;

//[]
//{}

int main() {
	ifstream inFile;
	inFile.open("B-large.in");
	ofstream outFile;
	outFile.open("output.txt");
	
	int a;
	inFile >> a;
	string b[a];
	
	for(int i = 0; i < a; i++)
		inFile >> b[i];
	inFile.close();
	int counter;
	string line;
	
	for(int i = 0; i < a; i++){
		counter = 0;
		line = b[i];
		
		if(line.length() == 1){
			if(line == "+"){
				cout << "Case #" << i+1 << ": " << 0 << endl;
				outFile << "Case #" << i+1 << ": " << 0 << endl;
			}	
			else{
				cout << "Case #" << i+1 << ": " << 1 << endl;
				outFile << "Case #" << i+1 << ": " << 1 << endl;
			}
		}
		else{
			for(int j = 0; j < line.length() - 1; j++)
				if(line[j] != line[j+1])
			 		counter++;

			if(line[line.length() - 1] == '-')
				counter++;
			
			cout << "Case #" << i+1 << ": " << counter << endl;
			outFile << "Case #" << i+1 << ": " << counter << endl;
		}
	}
	
	outFile.close();
	
	return 0;
}
