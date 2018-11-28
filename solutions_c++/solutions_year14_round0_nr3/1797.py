#include <iostream>
#include <algorithm>
#include <cmath>

const double eps = 1e-7;

using namespace std;

int coutbit(int x) {
	if (x <= 0) return 0;
	return 1 + coutbit(x & (x - 1));
}

int d[25];

void dfs(int r, int c, int & t, int& R, int & C) {
	if ((t & (1 << (r * C + c))) != 0) return;
	t |= 1 << (r * C + c);
	if (d[r * C + c] != 0) return;
	for (int dx = -1; dx <= 1; dx ++)
		for (int dy = -1; dy <= 1; dy ++)
			if (r + dx >= 0 && r + dx < R && c + dy >= 0 && c + dy < C) {
				dfs(r + dx, c + dy, t, R, C);
			}
}

void go(int R, int C, int X) {

	if (X == R * C - 1) {
		for (int i = 0; i < R; i ++) {
			for (int j = 0; j < C; j ++) {
				if ((i + j) == 0) cout << 'c';
				else cout << '*';
			}
			cout << endl;
		}
		return;

	}

	int T = R * C;
	int dest = -1;

	for (int i = 0; i < (1 << T); i ++) {
		
		if (coutbit(i) == X){
			fill (d, d + T, 0);
			for (int k = 0; k < T; k ++) if ((i >> k) & 1) {
				int x = k / C;
				int y = k % C;
				for (int dx = -1; dx <= 1; dx ++)
					for (int dy = -1; dy <= 1; dy ++)
						if (x + dx >= 0 && x + dx < R && y + dy >= 0 && y + dy < C) {
							d[(x + dx) * C + y + dy] ++;
						}
				
			}
			for (int j = 0; j < T; j ++) if (d[j] == 0) {
				int t = 0;
				dfs(j / C, j % C, t, R, C);
				if ((t & i) == 0 && (t | i) == ((1 << T) - 1)){
					dest = i;
				}
				break;
			}
			if (dest != -1) break;
		}
	}
	if (dest == -1) {
		cout << "Impossible" << endl;
		return;
	}
	bool f = false;
	for (int r = 0; r < R; r ++){
		for (int c = 0; c < C; c ++){
			int i = r * C + c;
			if ((dest & (1 << i)) == 0) {
				if (d[i] == 0 && !f) {
					cout << 'c';
					f = true;
				} else cout << '.';
			} else cout << '*';
			
		}
		cout << endl;
	}

}
int main(int argc, char const *argv[])
{
	for (int r = 1; r < 5; r ++)
		for (int c = 1; c <= 5; c ++)
			for (int k = 0; k <= r * c; k ++) {
				//go(r, c, k);
			}
	int cases; cin >> cases;

	
	for (int tc = 1; tc <= cases; ++tc)
	{

		cout << "Case #" << tc << ":" << endl;

		int R, C, X;
		cin >> R >> C >> X;
		go(R, C, X);
		
	}
	return 0;
}