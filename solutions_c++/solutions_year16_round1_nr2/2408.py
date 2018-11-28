#include <algorithm>
#include <bitset>
#include <cstdlib>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <sstream>
#include <set>
#include <map>
using namespace std;

const int HOR = 0;
const int VER = 1;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;

vi fill_vertical(const vii& L, vector<bool> used, int amountUsed, vii R, int nextColumn, pii blank);

vi get_line(vii R, int axis, int index) {
	if (axis == HOR)
		return R[index];
	vi ans(R.size());
	for (int i = 0; i < (int) R.size(); i++)
		ans[i] = R[i][index];
	return ans;
}

vi fill_horizontal(const vii& L, vector<bool> used, int amountUsed, vii R, int nextRow, pii blank) {
	if (nextRow == R.size()) {
		if (amountUsed == L.size() && blank.first >= 0) {
			// Return blank vector
			return get_line(R, blank.first, blank.second);
		} else {
			// Fill in the other direction
			return fill_vertical(L, used, amountUsed, R, 1, blank);
		}
	} else {
		// Place next row or check if correct
		vi ans(1, 0);
		vii NextR = R;
		int check = R[nextRow][0] == 0 ? 1 : 0;
		for (int i = 0; i < (int) L.size() && ans[0] == 0; i++) {
			if (L[i][check] == R[nextRow][check] && !used[i]) {
				bool matching = true;
				for (int j = 0; j < (int) L[i].size(); j++)
					if (R[nextRow][j] == 0)
						NextR[nextRow][j] = L[i][j];
					else if (R[nextRow][j] != L[i][j]) // If it doesn't match
						matching = false;
				if (matching) {
					used[i] = true;
					ans = fill_horizontal(L, used, amountUsed + 1, NextR, nextRow + 1, blank);
					used[i] = false;
				}
			}
		}
		// Leave row blank
		if (ans[0] == 0 && blank.first < 0)
			ans = fill_horizontal(L, used, amountUsed, R, nextRow + 1, make_pair(HOR, nextRow));
		return ans;
	}
}

vi fill_vertical(const vii& L, vector<bool> used, int amountUsed, vii R, int nextColumn, pii blank) {
	if (nextColumn == R.size()) {
		if (amountUsed == L.size() && blank.first >= 0) {
			// Return blank vector
			return get_line(R, blank.first, blank.second);
		} else {
			// Fill in the other direction
			return fill_horizontal(L, used, amountUsed, R, 1, blank);
		}
	} else {
		// Place next column or check if correct
		vi ans(1, 0);
		vii NextR = R;
		int check = R[0][nextColumn] == 0 ? 1 : 0;
		for (int i = 0; i < (int) L.size() && ans[0] == 0; i++) {
			if (L[i][check] == R[check][nextColumn] && !used[i]) {
				bool matching = true;
				for (int j = 0; j < (int) L[i].size(); j++)
					if (R[j][nextColumn] == 0)
						NextR[j][nextColumn] = L[i][j];
					else if (R[j][nextColumn] != L[i][j]) // If it doesn't match
						matching = false;
				if (matching) {
					used[i] = true;
					ans = fill_vertical(L, used, amountUsed + 1, NextR, nextColumn + 1, blank);
					used[i] = false;
				}
			}
		}
		// Leave column blank
		if (ans[0] == 0 && blank.first < 0)
			ans = fill_vertical(L, used, amountUsed, R, nextColumn + 1, make_pair(VER, nextColumn));
		return ans;
	}
}


int main() {
#ifdef TESTING
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
	int T;
	cin >> T;
	for (int caso = 1; caso <= T; caso++) {
		int N;
		cin >> N;
		vii L(2*N-1, vi(N));
		for (int i = 0; i < 2*N-1; i++)
			for (int j = 0; j < N; j++)
				cin >> L[i][j];
		sort(L.begin(), L.end());

		vii R(N, vi(N, 0));
		R[0] = L[0];
		vector<bool> used(2*N-1, false);
		used[0] = true;
		vi ans = fill_vertical(L, used, 1, R, 0, make_pair(-1, -1));
		if (ans[0] == 0) {
			for (int i = 0; i < N; i++) {
				R[0][i] = 0;
				R[i][0] = L[0][i];
			}
			ans = fill_horizontal(L, used, 1, R, 0, make_pair(-1, -1));
		}

		cout << "Case #" << caso << ":";
		for (int i = 0; i < N; i++)
			cout << " " << ans[i];
		cout << endl;
	}
	return 0;
}
