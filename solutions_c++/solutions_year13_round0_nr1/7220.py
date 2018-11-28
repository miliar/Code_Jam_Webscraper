
#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

char tab[4][4];

string result()
{
	int x, o, c = 1;
	for (int k = 0; k < 2; ++k) {
		for (int i = 0; i < 4; ++i) {
			x = o = 1;
			for (int j = 0; j < 4; ++j) {
				int ki = i, kj = j;
				if (k) {
					swap(ki, kj);
					c &= tab[ki][kj] != '.';
				}
				x &= (tab[ki][kj] == 'X' || tab[ki][kj] == 'T');
				o &= (tab[ki][kj] == 'O' || tab[ki][kj] == 'T');
			}
			if (x)
				return "X won";
			if (o)
				return "O won";
		}
		x = o = 1;
		for (int i = 0; i < 4; ++i) {
			int di = i;
			if (k)
				di = 3 - i;
			x &= (tab[i][di] == 'X' || tab[i][di] == 'T');
			o &= (tab[i][di] == 'O' || tab[i][di] == 'T');
		}
		if (x)
			return "X won";
		if (o)
			return "O won";
	}
	if (c)
		return "Draw";
	return "Game has not completed";
}

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k) {
		for (int i = 0; i < 4; ++i) {
			string row;
			cin >> row;
			for (int j = 0; j < 4; ++j)
				tab[i][j] = row[j];
		}
		cout << "Case #" << k << ": " << result() << endl;
	}
	return 0;
}
