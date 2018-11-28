#include <iostream>
#include <fstream>
using namespace std;


void flipK(string& s, int k, int current){

	for(int i = current; i < current+k; i++){

		if(s[i] == '+') s[i] = '-';
		else if(s[i] == '-') s[i] = '+';

	}
}

int main(){

	int T;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> T;

	for(int t = 0; t < T ; t++){
		string s;
		int k, count = 0;
		bool possible = true;
		fin >> s >> k;
		int n = s.length();
		for(int i = 0; i < n-k+1; i++){
			if(s[i] == '-'){ flipK(s, k, i); count++; }
		}

		for(int i = n-k+1; i < n; i++){
			if(s[i] == '-'){ possible = false; }
		}

		if(possible) fout << "Case #" << t+1 << ": " << count <<endl;
		else fout << "Case #" << t+1 << ": " << "IMPOSSIBLE" <<endl;
	}

	fin.close();
	fout.close();

	return 0;
}
