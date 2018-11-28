#include <iostream>
#include <fstream>
using namespace std;

long long pow(long long base ,int e) {
	long long ret = 1;
	for (int i = 0; i < e; i++)
		ret *= base;
	return ret;
}

int main(){
	ofstream file;
	ifstream inf;
	inf.open("D-small-attempt3.in");
	file.open("output.txt");
	int T;
	inf >> T;

	for (int t = 1; t <= T; t++) {
		file << "Case #" << t << ":";
		int k, c, s;
		inf >> k >> c >> s;
		int need = k / c + (k % c ? 1 : 0);
		if (need > s) {
			file << " IMPOSSIBLE";
		} else {
			for (int i = 1; i <= s; i++)
				file << ' ' << i;
			/*int base = 1;
			for (int i = 0; i < need; i++) {
				long long num = 0;
				for (int cnt = 1; cnt <= c; cnt++) {
					int chose = base > k ? 1 : base;
					num += pow(k,c - cnt) * (chose - 1);
					//num = chose - 1;
					base++;
				}
				file << ' ' << num + 1;
			}*/

		}
		file << endl;
	}
	return 0;
}