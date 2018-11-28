#include <iostream>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define forn(i, n) for(int i=0; i<(int)(n); i++)

int N, M;
enum Check { Row, Column };

int getIthValue(int **lawn, int index, int var, Check check) {
	switch (check) {
	case Row:
		return lawn[index][var];
	case Column:
		return lawn[var][index];
	default:
		cout << "unexpected check \n";
		return 0;
	}
}

bool checkHeight(int **lawn, int fixed_index, Check check) {
	int range = (check == Row) ? M : N;
	if (check == Column) {
		for (int var = 0; var < range; var++) {
			int h = getIthValue(lawn, fixed_index, var, check);
			if (h != 1)
				return false;
		}
	}

	int height = getIthValue(lawn, fixed_index, 0, check);
	if (height == 1) {
		for (int var = 1; var < range; var++) {
			int h = getIthValue(lawn, fixed_index, var, check);
			if (h != 1) {
				bool temp = true;
				for (int v = 0; v < range; v++)
					if (getIthValue(lawn, fixed_index, v, Row) == 1) {
						temp = temp && checkHeight(lawn, v, Column);
					}
				if (!temp) return false;
			}
		}
	} else {
		for (int var = 1; var < range; var++) {
			int h = getIthValue(lawn, fixed_index, var, check);
			if (h == 1)
				return checkHeight(lawn, var, Column);
		}
	}
	return true;
}

bool hasMowed(int **lawn) {
	bool isMowed = false;
	// Check rows and columns
	forn(i, N) {
		isMowed = checkHeight(lawn, i, Row);
		if (!isMowed) {
			return false;
		}
	}
	return true;
}

int main()
{
	int T;
	cin >> T;

	forn(i, T) {
		cin >> N >> M;
		int** lawn = new int*[N];
		forn(j, N)
			lawn[j] = new int[M];
		forn(j, N) {
			forn(k, M) {
				cin >> lawn[j][k];
				//cout << lawn[j][k];
			}
			//cout << endl;
		}
		cout << "Case #" << i + 1 << ": ";
		cout << ((hasMowed(lawn)) ? "YES" : "NO") << endl;
		
		forn(j, N)
			delete [] lawn[j];
	}

	return 0;
}
