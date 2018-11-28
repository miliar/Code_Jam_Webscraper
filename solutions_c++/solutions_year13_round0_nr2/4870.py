#include <iostream>
#include <fstream>

using namespace std;

ifstream inp("01.in");
ofstream out("01.out");

int dat[100][100];
int w, h;

bool check(int sx, int sy) {
	int o = dat[sx][sy];
	bool chk1 = true;
	bool chk2 = true;
	for (int i = 0; i < w; i++) {
		if (dat[i][sy] > o) {
			chk1 = false;
			break;
		}
	}
	for (int i = 0; i < h; i++) {
		if (dat[sx][i] > o) {
			chk2 = false;
			break;
		}
	}
	return (chk1 || chk2);
}

int main() {

	int n;
	inp >> n;

	for (int c = 0; c < n; c++) {

		inp >> h >> w;

		int max = 0;
		int min = 100;

		for (int j = 0; j < h; j++) {
			for (int i = 0; i < w; i++) {
				inp >> dat[i][j];
				if (dat[i][j] < min) {
					min = dat[i][j];
				}
				if (dat[i][j] > max) {
					max = dat[i][j];
				}
			}
		}

		bool chk = true;
		for (int i = 0; i < w; i++) {
			for (int j = 0; j < h; j++) {
				chk &= check(i, j);
				if (!chk) break;
			}
			if (!chk) break;
		}

		out << "Case #" << c+1 << ": " << (chk ? "YES" : "NO") << endl;

	}

	return 0;
}
