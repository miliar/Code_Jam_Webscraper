#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

char phabet[] = {'A','B','C','D','E','F','G','H','I','J','K', 'L', 'M', 'N', 'O', 'P', 
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t; fin >> t;

	for (int i = 0; i < t; ++i)
	{
		int n; fin >> n;
		int alph[26] = { 0 };
		int index01 = 0;
		int index02 = 0;
		
		

		for (int j = 0; j < n; j++) 
		{
			int k; fin >> k;
			alph[j] += k;
		}

		int max01 = 0;
		for (int j = 0; j < 26; j++) {
			if (max01 < alph[j]) {
				max01 = alph[j];
				index01 = j;
			}
		}

		int max02 = 0;
		for (int j = 0; j < 26; j++) {
			if (max02 < alph[j]) {
				if (j != index01) {
					max02 = alph[j];
					index02 = j;
				}
			}
		}

		int d = max01 - max02;
		string mmax = ""; 
		for (int j = 0; j < d; j++) {
			if (j != 3) {
				alph[index01]--;
				mmax += phabet[index01];
			}
			else 
				break;
		}
		
		fout << "Case " << "#" << (i+1) << ": ";
		fout << mmax << " ";

		for (int j = 0; j < 26; j++) {
			if (j != index01 && j != index02) {
				for (int g = 0; g < alph[j]; g++) fout << phabet[j] << " ";
			}
		}

		for (int j = 0; j < max02; j++) {
			fout << phabet[index01] << phabet[index02] << " ";
		}
		
		fout << endl;
	}

	return 0;
}
