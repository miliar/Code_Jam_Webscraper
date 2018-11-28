#include <fstream>

using namespace std;

bool h[17];

int main() {
	ifstream fin("a.in");
	ofstream fout("a.out");
	int t, x, y, tt1, tt2, i, j, k;
	fin >> t;
	for(x = 1; x <= t; x++) {
		for(i = 0; i < 17; i++) h[i] = false;
		fin >> tt1;
		for(i = 0; i < 4; i++) for(j = 0; j < 4; j++) {
			fin >> tt2;
			if(tt1 == i + 1) h[tt2] = true;
		}
		y = -1;
		fin >> tt1;
		for(i = 0; i < 4; i++) for(j = 0; j < 4; j++) {
			fin >> tt2;
			if(h[tt2] && tt1 == i + 1) {
				if(y < 0) y = tt2;
				else y = 17;
			}
		}
		fout << "Case #" << x << ": "; 
		if(y < 0) fout << "Volunteer cheated!\n";
		else if(y > 16) fout << "Bad magician!\n";
		else fout << y << "\n";
	}
	return 0;
} 
