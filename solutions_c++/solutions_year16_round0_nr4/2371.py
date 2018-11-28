#include <iostream>
#include <fstream>
#include <strings.h>
using namespace std;
int main1() {
	char ch1[1000] = { "101" };
	char ch2[1000] = { 0 };

	int T = 2;
	for (int i = 0; i < T; i++) {
		char tempch[1000] = { 0 };

		for (unsigned int j = 0; j < strlen(ch1); j++)
			ch2[j] = '1';

		for (unsigned int j = 0; j < strlen(ch1); j++)
			if (ch1[j] == '0')
				strcat(tempch, ch1);
			else
				strcat(tempch, ch2);
		strcpy(ch1, tempch);
	}
	cout << ch1;
}

int main() {
	ifstream fin("D-small-attempt1.in", ios::in);
	ofstream fout("D-small-attempt1.out", ios::out);
	int T, N, K, S;

	fin >> T;
	for (int i = 0; i < T; i++) {
		fin >> N >> K >> S;
		fout << "Case #" << i + 1 << ":";
		if (K == 1 && S < N) {
			fout << " IMPOSSIBLE" << endl;
			continue;
		}
		if (K > 1 && S < N - 1) {
			fout << " IMPOSSIBLE" << endl;
			continue;
		}
		for (int i = 1; i <= N; i++)
			if (K > 1 && i == 1 && N!=1)
				continue;
			else
				fout << " " << i;
		fout << endl;
	}
}
