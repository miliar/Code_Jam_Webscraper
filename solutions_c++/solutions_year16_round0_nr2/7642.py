#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int findN (string S){
	int turns = 0;
	for ( int i = S.length()-1; i >= 0; i -- ){
		if (S.substr(i, 1) == "-" and turns%2 == 0) turns++; 
		if (S.substr(i, 1) == "+" and turns%2 == 1) turns++; 
		
		//cout << S.substr(i, 1) << " " << turns << endl;
	}
	return turns;
}

int main() {
	ofstream fout ("test.out");
	ifstream fin ("B-large.in");
	int T;
	string S;
	//fin >> T;
	fin >> T;
	for ( int i = 0; i < T; i++){
		fin >> S;
		fout << "Case #" << (i+1) <<": " << findN(S) << endl;
	}
	return 0;
}