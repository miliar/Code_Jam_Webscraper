#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:30000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <queue>
#include <vector>

using namespace std;

const double EPS = 1E-8;
const int INF = (int)1E+9;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;
typedef long double ld;

const int fieldSize = 4;
char field[fieldSize][fieldSize];

bool check(const char & c, const int & sx, const int & sy, const int & dx, const int & dy) {
	int x = sx;
	int y = sy;
	int t_count = 0;
	int c_count = 0;

	while (x >= 0 && x < fieldSize && y >= 0 && y < fieldSize) {
		if (field[x][y] == c)
			c_count++;
		if (field[x][y] == 'T')
			t_count++;
		x += dx;
		y += dy;
	}

	return (t_count <= 1 && c_count + t_count == fieldSize);
}

bool check(const char & c) {
	forn(i, fieldSize)
	{
		if (check(c, i, 0, 0, +1))
			return true;
		if (check(c, 0, i, +1, 0))
			return true;
	}
	if (check(c, 0, 0, +1, +1))
		return true;
	if (check(c, 0, fieldSize - 1, +1, -1))
		return true;
	return false;
}

int main() {
	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int tests;
	cin >> tests;
	forn(test, tests) {
		string str;
		getline(cin, str);
		bool incomplite = false;
		forn(i, fieldSize) {
			getline(cin, str);
			forn(j, fieldSize) {
				field[i][j] = str[j];
				incomplite |= (str[j] == '.');
			}
		}
		bool win1 = check('X');
		bool win2 = check('O');
		cout << "Case #" << test + 1 << ": ";
		if (win1 && !win2)
			cout << "X won";
		else if (!win1 && win2)
			cout << "O won";
		else {
			if (incomplite)
				cout << "Game has not completed";
			else
				cout << "Draw";
			}
		cout << "\n";
	}
	return 0;
}
