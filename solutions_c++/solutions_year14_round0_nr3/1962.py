#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <ctime>
#include <cstring>

using namespace std;

const int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[] = {-1, 0, 1, 1, -1, -1, 0, 1};

int xstack[6];
bool otv[6][6], use[6][6], free_space[6][6];
int n, m, filled;
bool can;

bool is_good() {
	for(int i = 0;i < 6;i++){
		for(int j = 0;j < 6;j++){
			use[i][j] = false;
			free_space[i][j] = false;
		}
	}
	int cur_space = 0;
	for (int i = 0; i < n; i++) {
		cur_space += xstack[i];
		for (int j = 0; j < xstack[i]; j++) {
			free_space[i][j] = true;
			use[i][j] = true;
		}
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (!use[i][j]) {
				bool ok = false;
				for (int k = 0; k < 8; k++){
					if((i + dx[k]) < n && (j + dy[k]) < m && (i + dx[k]) > -1 && (j + dy[k]) > -1)
						if (use[i + dx[k]][j + dy[k]]) ok = true;
				}
				if (ok) {
					free_space[i][j] = true;
					cur_space++;
				}
			}
			if (cur_space == n * m - filled) {
				for (int i = 0; i < n; i++)
					for (int j = 0; j < m; j++) otv[i][j] = free_space[i][j];
				return true;
			}
			return false;
}

void try_solve(int len) {
	if (can) return;
	if (len == n - 1) {
		if (is_good()) can = true;
		return;
	}
	for (int i = (len == 0) ? 1 : 0; i < m; i++) {
		xstack[len] = i;
		try_solve(len + 1);
		xstack[len] = 0;
	}
}

void print(){
	for (int k = 0; k < n; k++) {
		for (int j = 0; j < m; j++) {
			if (k == 0 && j == 0) {
				cout << 'c';
				continue;
			}
			if (otv[k][j]) 
				cout << '.';
			else cout << '*';
		}
		cout << endl;
	}
}

int main(){
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);
	int t;
	cin >> t;
	for(int ti = 0;ti < t;ti++){
		cout << "Case #" << (ti + 1) << ": " << endl;
		cin >> n >> m >> filled;
		for(int i = 0;i < 6;i++)
			for(int j = 0;j < 6;j++)
				otv[i][j] = false;
		for(int i = 0;i < 6;i++)
			xstack[i] = 0;
		if (filled == n * m - 1) {
			print();
			continue;
		}
		if (n == 1) {
			for (int k = 0; k < n * m - filled; k++) 
				otv[0][k] = true;
			print();
			continue;
		}
		if (m == 1) {
			for (int k = 0; k < n * m - filled; k++) 
				otv[k][0] = true;
			print();
			continue;
		}
		can = false;
		try_solve(0);
		if (!can) {
			cout << "Impossible" << endl;
			continue;
		}
		print();
	}
	return 0;
}