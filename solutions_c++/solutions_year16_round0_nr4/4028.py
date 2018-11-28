#include <fstream>
#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int main(){
	ifstream file("input.txt", ifstream::in);
	ofstream outfile("result.txt", ofstream::out);
	string s;
	int testCases;
	file >> testCases;
	for(int caseNo = 1; caseNo <= testCases; ++caseNo){
		int valK, valC, valS;
		file >> valK >> valC >> valS;
		if(valK == valS){
			cout << "Case #" << caseNo << ": ";
			outfile << "Case #" << caseNo << ":";
			for(int i = 1; i <= valK; ++i){
				cout << ' ' << i;
				outfile << ' ' << i;
			}
			cout << '\n';
			outfile << '\n';
		} else { 
			cout << "error\n";
			break;
		}
		//cout << "Case #" << caseNo << ": " <<  << "\n";
		//outfile << "Case #" << caseNo << ": " <<  << "\n";
	}
	
	return 0;
}