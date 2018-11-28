#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

int r, c;

char m[200][200];

int col[200];
int row[200];


const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};
int dir[256];

void Load()
{
	cin >> r >> c;
	int i, j;
	memset(col, 0, sizeof(col));
	memset(row, 0, sizeof(row));	
	for (i = 1; i <= r; i++) {
		for (j = 1; j <= c; j++) {
			cin >> m[i][j];
			if (m[i][j] != '.') {
				row[i]++;
				col[j]++;
			}
		}
	}
}

void Solve()
{
	int i, j, k, l;
	int ans = 0;
	for (i = 1; i <= r; i++) {
		for (j = 1; j <= c; j++) {
			if (m[i][j] == '.') continue;
//			cerr << "cell " << i << ' ' << j << " " << m[i][j] <<"\n";
			int d = dir[(int)m[i][j]];
			k = i + dx[d];
			l = j + dy[d];
			bool good = false;
			while (k > 0 && k <= r && l > 0 && l <= c) {
//				cerr << k << ' ' << l << " " << m[k][l] << "\n";
				if (m[k][l] != '.') {
					good = true;
					break;
				}
				k += dx[d];
				l += dy[d];
			}
			if (!good) {
//				cerr << "bad\n";
				if (row[i] == 1 && col[j] == 1) {
					cout << "IMPOSSIBLE\n";
					return;
				}
				ans++;				
			}

		}
	}
	cout << ans << "\n";
}

int main()
{
	dir['^'] = 3;
	dir['>'] = 0;
	dir['v'] = 1;
	dir['<'] = 2;	
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
