#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main() {

	int T, K,C,S;
	//ifstream fin("input.txt");

	ifstream fin("input1.in");
	ofstream fout("output.txt");
	
	fin >> T;

	for (int i = 0;i < T;i++) {
		fin >> K;
		fin >> C;
		fin >> S;
		if (K == 1) {
			cout << "Case #" << i + 1 << ": 1"<< endl;
			fout << "Case #" << i + 1 << ": 1"<< endl;
		}
		else if (K>1 && C==1 && S<K) {
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
			fout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		}
		else if (K>1 && C == 1 && S==K) {
			cout << "Case #" << i + 1 << ":";
			fout << "Case #" << i + 1 << ":";
			for (int j = 1;j <= K;j++) {
				cout << " " << j;
				fout << " " << j;
			}
			cout << endl;
			fout << endl;
		}
		else {
			cout << "Case #" << i + 1 << ": 2";
			fout << "Case #" << i + 1 << ": 2";

			for (int j = 2;j <= K - 1;j++) {
				cout << " " << j*K;
				fout << " " << j*K;
			}
			cout << endl;
			fout << endl;
		}
	}

	system("pause");
	return 0;
}