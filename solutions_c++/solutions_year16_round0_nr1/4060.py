#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;



int main() {

	string line;
	ifstream inFile("in.txt");
	ofstream outFile("out.txt");
	getline(inFile, line);
	int T = stoi(line);
	int cnt = T;
	int result;

	int N, num;
	while (cnt-- && getline(inFile, line)) {
		int N = stoi(line);
		map<int, int> mapD;
		map<int, int> mapN;

		bool done = false;
		num = N;
		while (1) {
			// check mapN first
			if (mapN.find(num) != mapN.end()) {
				num = -1;
				goto done;
			}
			mapN[N] = 1;

			// put into mapD
			int digits = num;
			while (digits > 0) {
				mapD[digits % 10] ++;
				digits /= 10;
			}

			// check mapD
			if (mapD[0] && mapD[1] && mapD[2] && mapD[3] && mapD[4] &&
				mapD[5] && mapD[6] && mapD[7] && mapD[8] && mapD[9]) {
				goto done;
			}

			num += N;
		}

	done:
		if (num < 0) {
			//cout << "Case #" << T - cnt << ": " << "INSOMNIA" << endl;
			outFile << "Case #" << T - cnt << ": " << "INSOMNIA" << endl;
		} else {
			//cout << "Case #" << T - cnt << ": " << num << endl;
			outFile << "Case #" << T - cnt << ": " << num << endl;
		}
	}

	return 0;
}