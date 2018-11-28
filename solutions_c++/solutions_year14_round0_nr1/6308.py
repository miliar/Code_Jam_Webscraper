#include <iostream>
#include <fstream>
using namespace std;

int f[17], n, p, t, ans, num;

int main() {
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	fin >> p;
	
	for (int test=1; test<=p; test++) {
		for (int i=1; i<=16; i++)
			f[i] = 0;
		num = 0;
		fin >> n;
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++) {
				fin >> t;
				if (i == n) f[t] = 1;
			}
		
		fin >> n;
		for (int i=1; i<=4; i++)
			for (int j=1; j<=4; j++) {
				fin >> t;
				if (i == n && f[t]) {
					num ++;
					ans = t;
				}
			}
		fout << "Case #" << test << ": ";
		if (num == 1) fout << ans << endl;
		else if (num > 1) fout << "Bad magician!\n";
		else fout << "Volunteer cheated!\n";
	}
	fin.close();
	fout.close();
}
