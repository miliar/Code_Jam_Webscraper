#include <iostream>
#include <cstdio>

using namespace std;

#define forsn(i,s,n) for(int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)

int pasto[128][128];
int rows, columns;
int base;

//Esto es feo, pero bueh.
bool tryToCutRow(int row) {
	int mini = 101;
	int maxi = 0;
	forn(col, columns) {
		if (pasto[row][col] != 0) {
			mini = min(mini, pasto[row][col]);
			maxi = max(maxi, pasto[row][col]);
		}
	}
	if (base == mini && mini == maxi) {
		forn(col, columns) {
			pasto[row][col] = 0;
		}
		return true;
	}
	return false;
}

//Esto es feo, pero bueh.
bool tryToCutCol(int col) {
	int mini = 101;
	int maxi = 0;
	forn(row, rows) {
		if (pasto[row][col] != 0) {
			mini = min(mini, pasto[row][col]);
			maxi = max(maxi, pasto[row][col]);
		}
	}
	if (base == mini && mini == maxi) {
		forn(row, rows) {
			pasto[row][col] = 0;
		}
		return true;
	}
	return false;
}

int main() {
	freopen("lawnlarge.in","r",stdin);
	freopen("lawnlarge.out","w",stdout);
	int T;
	cin >> T;
	forn(caso, T){
		cin >> rows >> columns;
		forn(row, rows) forn(col, columns) cin >> pasto[row][col];
		int rescued = 1;
		for(base = 0;base < 101;base++) {
			rescued = 0;
			forn(row, rows) {
				rescued += tryToCutRow(row);
			}
			forn(col, columns) {
				rescued += tryToCutCol(col);
			}
		}
		bool someoneLeft = false;
		forn(row, rows) forn(col, columns) someoneLeft = someoneLeft || pasto[row][col];
		cout << "Case #" << caso + 1 << ": " << (someoneLeft ? "NO" : "YES") << endl;
	}
}
