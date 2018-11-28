#include <iostream>
#include <utility>

#define GET(mask, i, j) ((mask) & 1 << ((i) * c + (j)))

using namespace std;

typedef pair<int, int> PII;
typedef pair<PII, int> PIII;

int r, c;
int lovers[300];
bool grid[100][100];

PIII lover_to_motion(int a) {
	int idx = 0;
	PII pos;
	int dir = 0; // N E S W

	if (a <= c) {
		idx = a - 1;
		pos = make_pair(0, idx);
		dir = 2;
	}
	else if (a <= r + c) {
		idx = a - c - 1;
		pos = make_pair(idx, c - 1);
		dir = 3;
	}
	else if (a <= r + 2 * c) {
		idx = a - r - c - 1;
		idx = c - 1 - idx;
		pos = make_pair(r - 1, idx);
		dir = 0;
	}
	else {
		idx = a - r - 2 * c - 1;
		idx = r - 1 - idx;
		pos = make_pair(idx, 0);
		dir = 1;
	}
	return make_pair(pos, dir);
}

bool in_bounds(PII pos) {
	return (0 <= pos.first && pos.first < r &&
		    0 <= pos.second && pos.second < c);
}

bool works(int mask) {
	// 0: \
	// 1: /
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			grid[i][j] = GET(mask, i, j);
		}
	}
	for (int i = 0; i < 2 * (r + c); i += 2) {
		int a = lovers[i];
		int b = lovers[i+1];

		PIII aa = lover_to_motion(a);
		PIII bb = lover_to_motion(b);

		while (in_bounds(aa.first)) {
			if (grid[aa.first.first][aa.first.second]) { // /
				if (aa.second == 0) aa.second = 1;
				else if (aa.second == 1) aa.second = 0;
				else if (aa.second == 2) aa.second = 3;
				else if (aa.second == 3) aa.second = 2;
			}
			else { // \ 
				if (aa.second == 0) aa.second = 3;
				else if (aa.second == 1) aa.second = 2;
				else if (aa.second == 2) aa.second = 1;
				else if (aa.second == 3) aa.second = 0;
			}
			switch (aa.second) { // advance
				case 0: aa.first.first--; break;
				case 1: aa.first.second++; break;
				case 2: aa.first.first++; break;
				case 3: aa.first.second--; break;
			}
		}
		aa.second ^= 2; // flip the direction
		switch (aa.second) { // advance
			case 0: aa.first.first--; break;
			case 1: aa.first.second++; break;
			case 2: aa.first.first++; break;
			case 3: aa.first.second--; break;
		}
		if (aa != bb) return false;
	}
	return true;
}

int main() {
	int t; cin >> t;
	for (int test = 1; test <= t; ++test) {
		cin >> r >> c;
		for (int i = 0; i < 2 * (r + c); ++i) {
			cin >> lovers[i];
		}
		int n = r * c;

		int maskmask = -1;
		for (int mask = 0; mask < (1 << n); ++mask) {
			if (works(mask)) {
				maskmask = mask; break;
			}
		}
		cout << "Case #" << test << ":" << endl;
		if (maskmask >= 0) {
			for (int i = 0; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					cout << (GET(maskmask, i, j) ? '/' : '\\');
				}
				cout << endl;
			}
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}