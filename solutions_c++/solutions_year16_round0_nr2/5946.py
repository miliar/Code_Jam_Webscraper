#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string flip(const string &S, const int &Bpluses) {
	string temp = S;
	for (int i = 0; i < (S.length()-Bpluses); i++){
		if (S[S.length() - 1 - Bpluses- i] == '+') temp[i] = '-';
		else temp[i] = '+';
	}
	return temp;
}

int count(string &S){
	int moves = 0;
	int Bpluses = 0;
	while (Bpluses != S.length()){
		while (S[S.length() - 1 - Bpluses] == '+') { Bpluses++; if (Bpluses == S.length()) break; }
		if (Bpluses == S.length()) break;
		int Fpluses = 0;
		while (S[Fpluses] == '+') Fpluses++;
		if (Fpluses > 0) { S = flip(S, S.length() - Fpluses); moves++; }
		int Bpluses = 0;
		while (S[S.length() - 1 - Bpluses] == '+') { Bpluses++; if (Bpluses == S.length()) break; }
		if (Bpluses == S.length()) break;
		else { S = flip(S, Bpluses); moves++; }
		while (S[S.length() - 1 - Bpluses] == '+') { Bpluses++; if (Bpluses == S.length()) break; }
	}
	return moves;
}


int main(){
	ifstream infile;
	infile.open("B-large.in");
	if (!infile.is_open()) cout << "Failed to load file!" << endl;

	ofstream outfile;
	outfile.open("output1.txt");
	int T;
	infile >> T;

	string S;

	for (int i = 1; i <= T; i++){
		infile >> S;
		outfile << "Case #" << i << ": " << count(S) << endl;
	}
	infile.close();
	outfile.close();
	system("pause");
	return 0;
}
	