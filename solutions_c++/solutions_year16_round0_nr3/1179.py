#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("CIn.txt");
ofstream fout("COut.txt");

#define cin fin
#define cout fout


int main() {
	int T;
	cin >> T;
	for (int TC = 1; TC <= T; TC++) {
		int N, J;
		cin >> N >> J;

		cout << "Case #" << TC << ": " << endl;
		for (int i = 0; i < J; i++) {
			cout << 11;
			int u = i;
			for (int j = 0; j < (N - 4) / 2; j++) {
				if (u % 2) {
					cout << 11;
				}
				else {
					cout << "00";
				}
				u /= 2;
			}
			cout << 11;
			for (int j = 3; j <= 11; j++) {
				cout << " " << j;
			}
			cout << endl;
		}
	}
}