#include <fstream>
using namespace std;

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");

	int k;
	in >> k;

	for (int i=0;i<k;i++) {
		bool isfill=true;
		char s[4][4];
		for (int j=0;j<4;j++)
			for (int g=0;g<4;g++) {
				in >> s[j][g];
				if (s[j][g] == '.') isfill=false;
			}
		int win=0;
		pair<int,int> diag,diag1;
		for (int j=0;j<4;j++) {
			pair<int,int> h,v;
			for (int g=0;g<4;g++) {
				char gor=s[j][g];
				char vert=s[g][j];
				if (j+g==3) {
					if (gor == 'X') diag1.first++;
					if (gor == 'O') diag1.second++;
					if (gor == 'T') {diag1.first++; diag1.second++;}
				}
				if (j == g) {
					if (gor == 'X') diag.first++;
					if (gor == 'O') diag.second++;
					if (gor == 'T') {diag.first++; diag.second++;}
				}
				if (gor == 'X') h.first++;
				if (gor == 'O') h.second++;
				if (gor == 'T') {h.first++; h.second++;}
				if (vert == 'X') v.first++;
				if (vert == 'O') v.second++;
				if (vert == 'T') {v.first++; v.second++;}
			}
			if (h.first == 4 || v.first==4) win=1;
			if (h.second == 4 || v.second==4) win=2;
		}
		if (diag.first == 4 || diag1.first==4) win=1;
		if (diag.second == 4 || diag1.second==4) win=2;
		if (win == 0)
			if (isfill) out << "Case #" << i+1 << ": Draw" << endl; else out << "Case #" << i+1 << ": Game has not completed" << endl;
		if (win == 1) out << "Case #" << i+1 << ": X won" << endl;
		if (win == 2) out << "Case #" << i+1 << ": O won" << endl;
	}
	return 0;
}