//Lawnmower
#include <iostream>
#include <string>

#define forn(i,n) for(int i=0;i<int(n);++i)
using namespace std;

int lawn[105][105];
int lawnS[105][105];
int maxFila[105];
int maxCol[105];
int N, M; // N filas

string resultado() {
	// comparar
	forn (y,N) {
		forn (x,M) {
			if (lawn[y][x] != lawnS[y][x])
				return "NO";
		}
	}
	return "YES";
}

int main() {
	int T;
	cin >> T;
	forn (caso, T) {
		cin >> N >> M;
		forn (y,N) {
			maxFila[y] = -1;
			forn (x,M) {
				cin >> lawn[y][x];
				maxFila[y] = max(maxFila[y], lawn[y][x]);
			}
		}

		forn (x,M) {
			maxCol[x] = -1;
			forn (y,N)
				maxCol[x] = max(maxCol[x], lawn[y][x]);
		}

		// simular y comparar!
		forn(y,N)
			forn(x,M)
				lawnS[y][x] = min(100,min(maxFila[y],maxCol[x]));

		cout << "Case #" << caso+1 << ": " << resultado() << endl;
	}
	return 0;
}
