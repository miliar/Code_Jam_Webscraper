#include <iostream>
#include <iomanip>
#include <map>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

void solve(int);

int main () {

	ios::sync_with_stdio(false);
	
	int test_num;
	cin >> test_num;
	for (int case_id = 1;case_id <= test_num;case_id++) {
		solve(case_id);
	}

	return 0;
}

const int DI[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
const int R = 210;
const int C = 210;

map< pair<int, int>, int> mp_pos;
pair<int, int> pos[R*C];

int di[R*C];
int ans[R][C];

int data[R*C];
int r, c;
bool err = false;

int search(int x, int y, int di) {
	x += DI[di][0];
	y += DI[di][1];
	if( x < 0 or y < 0 or x >= r or y >= c ) {
		return mp_pos[{x, y}];
	}
	if(ans[x][y] == 1) {
		if(di == 0) return search(x, y, 3);
		if(di == 1) return search(x, y, 2);
		if(di == 2) return search(x, y, 1);
		if(di == 3) return search(x, y, 0);
	}else {
		if(di == 0) return search(x, y, 2);
		if(di == 1) return search(x, y, 3);
		if(di == 2) return search(x, y, 0);
		if(di == 3) return search(x, y, 1);
	}
}
bool check(void) {
	bool err = false;
	for(int i = 0;i < 2*(r+c);i+=2) {
		int val = data[i];
		int x = search(pos[val].first, pos[val].second, di[val]);
		if ( x != data[i+1]) {
			err = true;
			break;
		}
	}
	return not err;
}
void solve ( int case_id ) {

	cin >> r >> c;
	for (int i = 0;i < 2 * (r+c);i++) {
		cin >> data[i];
	}

	cout << "Case #" << case_id << ": " << endl;
	
	mp_pos.clear();
	for(int i = 1;i <= 2 * (r+c);i++) {
		if(i <= c) {
			pos[i] = {-1, i-1};
			di[i] = 0;
		} else if (i <= c+r) {
			pos[i] = {i-c-1, c};
			di[i] = 3;
		} else if (i <= 2*c+r) {
			pos[i] = {r, c-(i-(c+r))};
			di[i] = 1;
		} else {
			pos[i] = {r - (i - (2*c+r)), -1};
			di[i] = 2;
		}
		mp_pos[pos[i]] = i;
	}
	bool found = false;
	for (int i = 0;i < (1 << (r*c));i++) {
		for(int j = 0;j < r*c;j++) {
			int x = j / c, y = j % c;
			ans[x][y] = (i >> j) & 1;
		}
		if( check() ) {
			found = true;
			for(int i = 0;i < r;i++) {
				for(int j = 0;j < c;j++) {
					cout << (ans[i][j] ? '/' : '\\');
				}
				cout << endl;
			}
			break;
		}
	}


	if ( not found ) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}

}