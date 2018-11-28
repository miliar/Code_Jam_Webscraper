# include <string>
# include <fstream>
# include <algorithm>
# include <vector>
using namespace std;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

int r, c;
int m;
char field[100][100];
bool open[10][10];


int cc(int i, int j) {
	int count = 0;
	for (int k = -1; k <= 1; k++)
	for (int l = -1; l <= 1; l++)
	if (abs(k) + abs(l) != 0 && i + k >= 0 && i + k < r && j + l >= 0 && j + l < c)
	if (field[i + k][j + l] == '*')
		count++;
	return count;
}
int startX;
int startY;

void dfs(int x, int y) {
	open[x][y] = true;
	for (int k = -1; k <= 1; k++)
	for (int l = -1; l <= 1; l++) {
		if (abs(k) + abs(l) != 0 && x + k >= 0 && y + l >= 0 && x + k < r && y + l < c && field[x + k][y + l] != '*' && !open[x + k][y + l])
		{
			if (cc(x + k, y + l) == 0)
				dfs(x + k, y + l);
			else
				open[x + k][y + l] = true;
		}
	}
}

bool check(int mask) {
	int bombs = 0;
	for (int i = 0; i < r * c; i++) {
		int x = i / c;
		int y = i % c;
		bool bomb = (mask & (1 << i));
		if (bomb)
			bombs++;
		if (bomb)
			field[x][y] = '*';
		else
			field[x][y] = '.';
	}
	if (bombs != m)
		return false;


	for (int i = 0; i < r; i++)
	for (int j = 0; j < c; j++) {
		if (field[i][j] != '.')
			continue;

		if (r * c - 1 == m) {
			startX = i;
			startY = j;
			return true;
		}

		bool ok = (cc(i, j) == 0);
		
		if (ok) {
			memset(open, false, sizeof(open));
			dfs(i, j);

			bool ansFound = true;
			for (int we = 0; we < r; we++)
			for (int re = 0; re < c; re++) 
			if (field[we][re] != '*' && !open[we][re])
				ansFound = false;

			if (ansFound) {
				startX = i;
				startY = j;
				return true;
			}
		}
	}
	return false;
}




int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cin >> r >> c;
		cin >> m;

		cout << "Case #" << test << ":" << endl;

		bool ansFound = false;
		for (int mask = 0; mask < (1 << (r * c)) && !ansFound; mask++) {
			if (check(mask)) {
				field[startX][startY] = 'c';
				for (int i = 0; i < r; i++) {
					
					for (int j = 0; j < c; j++)
						cout << field[i][j];

					cout << endl;

					ansFound = true;
				}
			}
		}

		if (!ansFound)
			cout << "Impossible" << endl;

		/*
		bool ok = false;

		char field[100][100];
		memset(field, '*', sizeof(field));

		int empty = r * c - m;
		if (empty == 1)
			ok = true;
		if (r == 1 || c == 1) {
			ok = true;
			for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (r == 1)
					field[i][j] = (j < empty ? '.' : '*');
				else
					field[i][j] = (i < empty ? '.' : '*');
			}
		}

		for (int a = 2; a <= r && !ok; a++)
		for (int b = 2; b <= c && !ok; b++) {
			if (a * b == empty) {
				ok = true;
				for (int i = 0; i < a; i++) for (int j = 0; j < b; j++)
					field[i][j] = '.';
				break;
			}
			else if (b > 2 && a * b > empty && a * (b - 1) + 1 < empty) {
				ok = true;
				for (int i = 0; i < a; i++) for (int j = 0; j < b; j++)
					field[i][j] = '.';
				for (int i = a - 1, j = 0; j < a * b - empty; j++, i--)
					field[i][b - 1] = '*';
				break;
			}
			else if (a > 2 && a * b > empty && (a - 1) * b + 1 < empty) {
				ok = true;
				for (int i = 0; i < a; i++) for (int j = 0; j < b; j++)
					field[i][j] = '.';
				for (int i = b - 1, j = 0; j < a * b - empty; j++, i--)
					field[a - 1][i] = '*';
			}
		}

		field[0][0] = 'c';

		if (!ok && m == 4 && r == 5 && c == 5) {
			ok = true;
			for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) field[i][j] = '.';
			field[0][c - 1] = field[0][0] = field[r - 1][0] = field[r - 1][c - 1] = '*';

			field[2][2] = 'c';
		}

		if (!ok && m == 3 && r == 4 && c == 4) {
			ok = true;
			for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) field[i][j] = '.';
			field[3][3] = field[2][3] = field[3][2] = '*';

			field[0][0] = 'c';
		}

		if (!ok && r * c - m != 5 && r * c - m != 7 && r * c - m != 2 && r * c - m != 3)
			cout << "Impossible" << " " << r * c - m << " " << r << " " << c << " " << m;
		else {
			continue;
			for (int i = 0; i < r; i++) {
				cout << endl;
				for (int j = 0; j < c; j++)
					cout << field[i][j];
			}
		}

		cout << endl;*/
	}

	return 0;
}