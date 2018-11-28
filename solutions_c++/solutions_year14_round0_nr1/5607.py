#include <fstream>
#include <vector>
#include <cassert>

using namespace std;

int a[5][5], b[5][5];
int fa[17], fb[17];

int main() {
	ifstream f("input.txt");
	ofstream g("output.txt");
	int t, r1, r2;
	f >> t;
	for(int testCase = 1; testCase <= t; testCase++) {
		f >> r1;
		for(int i = 1; i <= 4; i++) {
			for(int j = 1; j <= 4; j++) {
				f >> a[i][j];
			}
		}
		f >> r2;
		for(int i = 1; i <= 4; i++) {
			for(int j = 1; j <= 4; j++) {
				f >> b[i][j];
			}
		}
		memset(fa, 0, sizeof(fa));
		memset(fb, 0, sizeof(fb));
		for(int i = 1; i <= 4; i++) {
			fa[a[r1][i]]++;
			fb[b[r2][i]]++;
		}
		vector<int> commons;
		for(int i = 1; i <= 16; i++) {
			assert(0 <= fa[i] && fa[i] <= 1);
			assert(0 <= fb[i] && fb[i] <= 1);
			if(fa[i] == 1 && fb[i] == 1) {
				commons.push_back(i);
			}
		}
		g << "Case #" << testCase << ": ";
		if(commons.size() == 0) {
			g << "Volunteer cheated!" << endl;
		}
		else if(commons.size() == 1) {
			g << commons[0] << endl;
		}
		else {
			g << "Bad magician!" << endl;
		}
	}
	return 0;
}
