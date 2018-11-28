#include <cstdlib>
#include <algorithm>
#include <assert.h>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef struct XX {
	vector<string> x;
	int cls;
};
vector<XX> xoms;

vector<XX> get_xoms(int x) {
	vector<XX> ret;
	if (x == 1) {
		ret.push_back({vector<string>(
			{"1"}), 0});
		return ret;
	}
	if (x == 2) {
		ret.push_back({vector<string>(
			{"11"}), 0});
		ret.push_back({vector<string>(
			{"1", "1"}), 0});
		return ret;
	}
	if (x == 3) {
		ret.push_back({vector<string>(
			{ "11",
				"10"}),
			0});
		ret.push_back({vector<string>(
			{ "11",
				"01"}),
			0});
		ret.push_back({vector<string>(
			{ "01",
				"11"}),
			0});
		ret.push_back({vector<string>(
			{ "10",
				"11"}),
			0});
		ret.push_back({vector<string>(
			{ "111",}),
			1});
		ret.push_back({vector<string>(
			{ "1",
				"1",
				"1"}),
			1});
		return ret;
	}
	if (x == 4) {
		ret.push_back({vector<string>(
			{ "1111",}),
			0});
		ret.push_back({vector<string>(
			{ "1",
				"1",
				"1",
				"1"}),
			0});
		ret.push_back({vector<string>(
			{ "11",
				"11"}),
			1});
		ret.push_back({vector<string>(
			{ "111",
				"010"}),
			2});
		ret.push_back({vector<string>(
			{ "010",
				"111"}),
			2});
		ret.push_back({vector<string>(
			{ "010",
				"110",
				"010"}),
			2});
		ret.push_back({vector<string>(
			{ "010",
				"011",
				"010"}),
			2});
		ret.push_back({vector<string>(
			{ "110",
				"011"}),
			3});
		ret.push_back({vector<string>(
			{ "011",
				"110"}),
			3});
		ret.push_back({vector<string>(
			{ "010",
				"110",
				"100"}),
			3});
		ret.push_back({vector<string>(
			{ "100",
				"110",
				"010"}),
			3});
		ret.push_back({vector<string>(
			{ "10",
				"10",
				"11"}),
			4});
		ret.push_back({vector<string>(
			{ "01",
				"01",
				"11"}),
			4});
		ret.push_back({vector<string>(
			{ "11",
				"10",
				"10"}),
			4});
		ret.push_back({vector<string>(
			{ "11",
				"01",
				"01"}),
			4});
		ret.push_back({vector<string>(
			{ "111",
				"100"}),
			4});
		ret.push_back({vector<string>(
			{ "100",
				"111"}),
			4});
		ret.push_back({vector<string>(
			{ "001",
				"111"}),
			4});
		ret.push_back({vector<string>(
			{ "111",
				"001"}),
			4});
		return ret;
	}
}

int G[4][4];
int R, C, X;

bool can_fill(int force) {
	bool filled = true;
#if 0
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) cout << G[i][j];
		cout << endl;
	}
	cout << endl;
#endif
	for (int i = 0; i < R; ++i) for (int j = 0; j < C; ++j) if (G[i][j] == 0) filled = false;
	if (filled) return true;
	int imin = 0, imax = xoms.size();
	if (force != -1) {
		imin = force;
		imax = imin + 1;
	}
	for (int i0 = 0; i0 < R; ++i0)
		for (int j0 = 0; j0 < C; ++j0) {
		
			for (int ii = imin; ii < imax; ++ii) {
//			cout << "trying " << i0 << " " << j0  << " ii " << ii << endl;
				int oldG[4][4];
				for (int i2 = 0; i2 < R; ++i2) for (int j2 = 0; j2 < C; ++j2) oldG[i2][j2] = G[i2][j2];

				for (int i1 = 0; i1 < xoms[ii].x.size(); ++i1)
					for (int j1 = 0; j1 < xoms[ii].x[0].size(); ++j1) {
						if (xoms[ii].x[i1][j1] == '1' && (i0 + i1 >= R || j0 + j1 >= C)) goto next_xom;
						if (G[i0 + i1][j0 + j1] && xoms[ii].x[i1][j1] == '1') goto next_xom;
						G[i0 + i1][j0 + j1] |= (xoms[ii].x[i1][j1] == '1');
					}
				if (can_fill(-1))
					return true;
next_xom:
				for (int i2 = 0; i2 < R; ++i2) for (int j2 = 0; j2 < C; ++j2) G[i2][j2] = oldG[i2][j2];

				continue;
			}
		}
	return false;
}

void print_xom(XX x) {
	for (int i = 0; i < x.x.size(); ++i)
		cout << x.x[i] << endl;
	cout << endl;
}

int main(int argc, char** argv) {

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {

		cin >> X >> R >> C;
		xoms = get_xoms(X);
		int max_cls = 0;
		for (int i = 0; i < xoms.size(); ++i) max_cls = max(max_cls, xoms[i].cls);
		bool can_fill_cls[5] = {0,};
		for (int i = 0; i < xoms.size(); ++i) {
//			cout << "Checking " << endl;
//			print_xom(xoms[i]);
			for (int i1 = 0; i1 < R; ++i1) for (int j1 = 0; j1 < C; ++j1) G[i1][j1] = 0;
			if (can_fill(i))
				can_fill_cls[xoms[i].cls] = 1;
//			cout << "Done" << endl << endl;
		}
		for (int i = 0; i <= max_cls; ++i)
			if (!can_fill_cls[i]) {
				cout << "Case #" << t << ": RICHARD" << endl;
				goto next;
			}
		cout << "Case #" << t << ": GABRIEL" << endl;
next:
		continue;
	}
	return 0;
}

