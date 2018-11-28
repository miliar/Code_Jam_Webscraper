#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

void Flip(char str[], int N) {
	for (int i = 0; i < N; i++)
		(str[i] == '+') ? str[i] = '-' : str[i] = '+';
}
int main() {
	ifstream fin("B-large.in", ios::in);
	ofstream fout("B-large.out", ios::out);
	int T;
	char IP[1000];
	fin >> T;

	for (int t = 0; t < T; t++) {
		int flips = 0;
		fin >> IP;
		for (int i = strlen(IP); i > 0; i--)
			if (IP[i - 1] == '-') {
				Flip(IP, i);
				flips++;
			}
		fout<<"Case #"<<t+1<<": "<<flips<<'\n';
	}
}
