#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

unsigned int N;
ifstream inFile;
ofstream outFile;

int main(int argc, char const *argv[]){
	if(argc != 2){
		cout<<"Error in Input"<<endl;
		return 0;
	}
	inFile.open(argv[1]);
	outFile.open("output.txt", ios::trunc | ios::out);
	if(!(inFile.is_open() && outFile.is_open()) ){
		cout << "can't open files"<<endl;
		return 0;
	}

	unsigned int T;
	inFile >> T;
	cout << "Running through " << T << " Iterations" << endl;
	for(int count=0; count<T; count++){
		inFile >> N;

		int standing = 0;
		int extras   = 0;
		cout << "reading " << N << "chars" << endl;
		for(int n=0; n<=N; n++){
			char c;
			inFile >> c;
			cout << (int)(c-'0') << " ";
			if((standing+extras) < n && c!='0') extras += (n-(standing+extras));
			standing += (c-'0');
		}
		cout << endl;

		outFile << "Case #" << count+1 << ": ";
		outFile << extras;
		outFile << std::endl;
	}
	cout << "\n";
	inFile.close();
	outFile.close();
	return 0;
}
