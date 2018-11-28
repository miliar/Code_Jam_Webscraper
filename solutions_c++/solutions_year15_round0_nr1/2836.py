#include<fstream>
#include<iostream>
#include<string>

using namespace std;

int main() {
	string inputFileName = "A-large.in";
	ifstream fin;
	fin.open(inputFileName);
	if (!fin.is_open()){
		cout << "failed to open file " << inputFileName;
	}
	string outputFileName = "output.txt";
	ofstream fout;
	fout.open(outputFileName);
	if (!fin.is_open()){
		cout << "failed to open file " << outputFileName;
	}

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++) {
		int Smax;
		fin >> Smax;
		string values;
		fin >> values;
		long standing = 0;
		long invites = 0;
		for (int i = 0; i <= Smax; i++) {
			if (i > standing) {
				invites += i - standing;
				standing += i - standing;
				
			}
			standing += values.at(i)-'0';
			if (standing > Smax) {
				break;
			}

		}


		fout << "Case #" << t << ": " << invites << endl;

	}
	return 0;
}