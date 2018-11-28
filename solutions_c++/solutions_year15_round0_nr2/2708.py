#include<fstream>
#include<iostream>
#include<string>

using namespace std;

int main() {
	string inputFileName = "B-large.in";
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
	long minutes[1001];
	
	for (int t = 1; t <= T; t++) {
		for (int i = 0; i < 1001; i++) {
			minutes[i] = i;
		}
		int D;
		int maxP = 0;
		fin >> D;
		int p;
		for (int i = 0; i < D; i++) {
			fin >> p;
			if (p>maxP) maxP = p;
			for (int j = 1; j <= p; j++) {
				minutes[j] += p / j;
				if (p%j == 0) {
					minutes[j]--;
				}
			}

		}
		long min = minutes[1];
		for (int i = 2; i <= maxP; i++) {
			if (min > minutes[i])
				min = minutes[i];
		}
		fout << "Case #" << t << ": " << min << endl;
	}
	cout << "PROBLEM COMPLETE!!!!!!!!!!" << endl;
	system("pause");
	return 0;
}