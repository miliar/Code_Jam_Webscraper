#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int sy, sx;

char board[110][110];

char maxY[101];
char maxX[101];

bool is_valid() {
	for (int y = 1; y <= sy; y++) {
		for (int x = 1; x <= sx; x++) {
			int cur_val = board[y][x];
			if (cur_val < maxY[y] &&
					cur_val < maxX[x]) {
				return false;
			}
		}
	}
	return true;
}

int main() {
	int tc; cin >> tc;
	
	for (int ctc = 1; ctc <= tc; ctc++) {
		memset(maxY, 0, sizeof maxY);
		memset(maxX, 0, sizeof maxX);
		cin >> sy >> sx;
		
		for (int y = 1; y <= sy; y++) {
			for (int x = 1; x <= sx; x++) {
				cin >> board[y][x];
				maxY[y] = max(maxY[y], board[y][x]);
				maxX[x] = max(maxX[x], board[y][x]);
			}
		}
		
		cout << "Case #" << ctc << ": " << (is_valid() ? "YES" : "NO") << endl;
	}
}
