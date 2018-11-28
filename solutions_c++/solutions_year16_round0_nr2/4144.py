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
	while (cnt-- && getline(inFile, line)) {
		
		int s[100] = { 0 };
		int L = line.length();
		for (int i = 0; i < L; i++) {
			s[i] = (line.at(i) == '-')  ? - 1 : 1;
		}
		int result = 0;

		while (1) {
			/*
			if all 1
			done
			else
			if L is 0
			make them 1
			else
			make them 0
			*/
			int sum = 0;
			for (int i = 0; i < L; i++) {
				sum += s[i];
			}
			if (sum == L)
				goto done;

			if (s[0] == -1) {
				for (int i = 0; i < L; i++) {
					if (s[i] == -1)
						s[i] = 1;
					else
						break;
				}
			} else {
				for (int i = 0; i < L; i++) {
					if (s[i] == 1)
						s[i] = -1;
					else
						break;
				}
			}
			result++;
		}
done:
		//cout << "Case #" << T - cnt << ": " << result << endl;
		outFile << "Case #" << T - cnt << ": " << result << endl;
	}

	return 0;
}