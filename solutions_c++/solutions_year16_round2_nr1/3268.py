#include <cstdio>
#include <iostream>
using namespace std;

int licz[200];
int ile[10];

int main() {
	ios_base::sync_with_stdio(0);
	string word;
	int tests;
	
	cin >> tests;
	for(int t = 1; t<=tests; t++) {
		cin >> word;
		int len = word.length();
		
		for(int i = 0; i < len; i++) {
			licz[word[i]]++;
		}
		
		ile[0] = licz[int('Z')];
		ile[2] = licz[int('W')];
		ile[4] = licz[int('U')];
		ile[6] = licz[int('X')];
		
		licz[int('S')] -= ile[6];
		licz[int('I')] -= ile[6];
		licz[int('X')] -= ile[6];
		
		licz[int('Z')] -= ile[0];
		licz[int('R')] -= ile[0];
		licz[int('E')] -= ile[0];
		licz[int('O')] -= ile[0];
		
		licz[int('T')] -= ile[2];
		licz[int('W')] -= ile[2];
		licz[int('O')] -= ile[2];
		
		licz[int('F')] -= ile[4];
		licz[int('O')] -= ile[4];
		licz[int('U')] -= ile[4];
		licz[int('R')] -= ile[4];
		
		ile[5] = licz[int('F')];
		
		licz[int('F')] -= ile[5];
		licz[int('I')] -= ile[5];
		licz[int('V')] -= ile[5];
		licz[int('E')] -= ile[5];
		
		ile[7] = licz[int('V')];
		
		licz[int('S')] -= ile[7];
		licz[int('E')] -= ile[7];
		licz[int('V')] -= ile[7];
		licz[int('E')] -= ile[7];
		licz[int('N')] -= ile[7];
		
		ile[1] = licz[int('O')];
		
		licz[int('O')] -= ile[1];
		licz[int('N')] -= ile[1];
		licz[int('E')] -= ile[1];
		
		ile[9] = licz[int('N')]/2;
		
		licz[int('N')] -= ile[9];
		licz[int('I')] -= ile[9];
		licz[int('N')] -= ile[9];
		licz[int('E')] -= ile[9];
		
		ile[8] = licz[int('G')];
		ile[3] = licz[int('R')];
		
		
		cout << "Case #" << t << ": ";
		
		for(int i = 0; i <= 9; i++) {
			for(int r = 0; r < ile[i]; r++) {
				cout << i;
			}
			ile[i] = 0;
		}
		
		for(int  i = 65; i<=90; i++) {
			licz[i] = 0;
		}
		cout << endl;
	}

	return 0;
}
