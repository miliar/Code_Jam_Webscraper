#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <iomanip>
#include <bitset>
#include <string>
#include <sstream>
using namespace std;

const double epsilon  = 1e-9;
typedef long long ll;
typedef long double ld;

const int SECURED = 1;
const int DANGER = 2;
const int TO_PROCESS = 3;
int main() {
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for (int testCounter = 1; testCounter <= numTests; testCounter++) {
		printf("Case #%d: ", testCounter);
		int r, c;
		cin >> r >> c;
		vector<string> mat(r + 2);
		mat[0].resize(c + 2, '.');
		mat[r + 1].resize(c + 2, '.');
		for(int i = 0; i < r; i++) {
			cin >> mat[i + 1];
			mat[i + 1] = "." + mat[i + 1] + ".";
		}
		vector<vector<int> > secured(r + 2);
		vector<vector<bool> > processed(r + 2);
		for (int i = 0; i < r + 2; i++) {
			secured[i].resize(c + 2, TO_PROCESS);
			processed[i].resize(c + 2, false);
		}
		for (int i = 0; i < r + 2; i++) {
			secured[i][0] = secured[i][c + 1] = DANGER;
			processed[i][0] = processed[i][c + 1] = true;
		}
		for (int i = 0; i < c + 2; i++) {
			secured[0][i] = secured[r + 1][i] = DANGER;
			processed[0][i] = processed[r + 1][i] = true;
		}

		queue<pair<int, int> > toProcess;
		for (int i = 0; i < r; i++) {
			toProcess.push(make_pair(i + 1, 1));
			toProcess.push(make_pair(i, c));
		}
		for (int i = 0; i < c; i++) {
			toProcess.push(make_pair(0, i + 1));
			toProcess.push(make_pair(r, i + 1));
		}
		pair<int, int> cur;
		int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
		map<char, int> m;
		m['^'] = 3;
		m['v'] = 2;
		m['<'] = 1;
		m['>'] = 0;
		int x, y;
		int cnt = 0;
		bool fail = false;
		while(!toProcess.empty() && !fail) {
			cur = toProcess.front();
			toProcess.pop();
			if (processed[cur.first][cur.second])
				continue;
			processed[cur.first][cur.second] = true;
			for (int i = 0; i < 4; i++) {
				x = cur.first + dir[i][0];
				y = cur.second + dir[i][1];
				if (!processed[x][y])
					toProcess.push(make_pair(x, y));
			}
			if (mat[cur.first][cur.second] == '.')
				continue;
			int idx = m[mat[cur.first][cur.second]];
			x = cur.first + dir[idx][0];
			y = cur.second + dir[idx][1];
			while(x > 0 && x < r + 1 && y > 0 && y < c + 1 && mat[x][y] == '.')
			{
				x += dir[idx][0];
		    	y += dir[idx][1];
			}
			if (secured[x][y] != DANGER) {
				continue;
			}
			int i;
			for (i = 0; i < 4; i++) {
				if (i == idx)
					continue;
				x = cur.first + dir[i][0];
				y = cur.second + dir[i][1];
				while(x > 0 && x < r + 1 && y > 0 && y < c + 1 && mat[x][y] == '.')
				{
					x += dir[i][0];
		    		y += dir[i][1];
				}
				if (secured[x][y] != DANGER) {
					cnt++;
					break;
				}
			}
			if (i == 4)
			{
				fail = true;
				break;
			}
		}
		if (fail) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		} else {
			cout << cnt << endl;
		}
	}
	return 0;
}
