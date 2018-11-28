#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int T = 0;
	fin >> T;
	for (int k = 0; k < T; k++) {
		string res = "Case #" + to_string(k + 1) + ": ";
		long long s;
		fin >> s;
		if (s == 0) {
			res += "INSOMNIA";
		}
		else {
			int mas[10];
			for (int i = 0; i < 10; i++) {
				mas[i] = 0;
			}

			//int N = 1;
			long long t = 0;
			for (long long i = 1; i < 10 ^ 6; i++) {
				t += s;
				long long q = t;
				while (q > 0) {
					mas[q % 10] = 1;
					q /= 10;
				}
				bool end = true;
				for (int j = 0; j < 10; j++) {
					if (mas[j] == 0) {
						end = false;
					}
				}
				if (end) {
					res += to_string(t);
					break;
				}

			}

		}

		fout << res << endl;

	}
	fin.close();
	fout.close();
}