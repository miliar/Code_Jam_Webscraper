#include <iostream>
#include <fstream>
#include <string>
#include <vector>

typedef long long int bignum;

using namespace std;

int main(){
	ifstream fin("B-large.in");
	ofstream fout("B-output.txt");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++){
		string s;
		fin >> s;

		char old = s[0];
		int changes = 0;
		for (int i = 1; i < s.length(); i++){
			if (s[i] != old){
				changes++;
				old = s[i];
			}
		}
		if (s[s.length() - 1] == '-'){
			changes++;
		}
		fout << "Case #" << t << ": " << changes << endl;
	}

	fout.close();
	return 0;
}