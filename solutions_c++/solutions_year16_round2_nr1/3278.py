#include <fstream>
#include <string>

using namespace std;

int main () {
	int T;
	ifstream fin ("input.txt");
	ofstream fout ("output.txt");
	fin >> T;
	for (int t = 0; t < T; t++) {
		string s;
		string w[10] = {"ZERO", "SIX", "TWO", "EIGHT", "FOUR", "ONE", "THREE", "FIVE", "SEVEN", "NINE"};
		int q[10] = {0, 6, 2, 8, 4, 1, 3 ,5 ,7 ,9};
		fin >> s;
		int a[50], b[10];
		for (int i = 0; i < 50; i++) {
			a[i] = 0;
			if (i < 10) b[i] = 0;
		}
		for (int i = 0; i < s.length(); i++)
			a[s[i] - 'A']++;
		int i = 0;
		while (i < 10) {
			int c[50];
			for (int j = 0; j < 50; j++)
				c[j] = 0;
			for (int j = 0; j < w[i].length(); j++)
				c[w[i][j] - 'A']++;
			int k = 0;
			for (int  j = 0; j < 50; j++)
				if (a[j] < c[j]) {k = 1; break;}
			if (k == 1) i++;
				else {
					for (int j = 0; j < 50; j++)
						a[j] -= c[j];
					b[q[i]]++;
				} 
		}
		fout << "Case #" << t + 1 << ": ";
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < b[i]; j++)
				fout << i;
		fout << endl;
	}
	fin.close();
	fout.close();
	return 0;
}