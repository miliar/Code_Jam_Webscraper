#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-OutputL.txt");
	int T; fin >> T;
	for (int t = 1; t <= T; t++) {
		long N; fin >> N;
		if (N == 0) {
			cout << "Case #" << t << ": INSOMNIA" << endl;
			fout << "Case #" << t << ": INSOMNIA" << endl;
			continue;
		}
		long number = N;
		int count = 0;
		bool digits[10]{};
		while (count < 10) {
			string num = to_string(number);
			for (int c = 0; c < num.length(); c++) {
				int digit = num[c] - '0';
				if (!digits[digit]) {
					digits[digit] = true;
					count++;
				}
			}
			number += N;
		}
		number -= N;
		cout << "Case #" << t << ": " << number << endl;
		fout << "Case #" << t << ": " << number << endl;
	}
	fin.close();
	fout.close();
	system("pause");//remove
}
