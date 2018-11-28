#include <iostream>
#include <cstdio>
#include <cstring>
#include <string.h>
#include <memory>
#include <map>
#include <queue>
#include <algorithm>
#include <string>
#include <stdlib.h>
#include "sstream"

using namespace std;

string s;

int a[200][200];

const int dir[4][2] = {{0,-1}, {-1,0}, {1,0}, {0,1}};
int test, n, m;

bool encounter(int i, int j, int d) {
	i = i + dir[d][0]; j = j + dir[d][1];
	while (i >= 0 && i < n && j >= 0 && j< m) {
		if (a[i][j] != 4) return true;
		i = i + dir[d][0]; j = j + dir[d][1]; 
	}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> test;
	for (int tt = 1; tt <= test; tt++) {
		cin >> n >> m;
		char h;
		scanf("%c", &h);
		for (int i = 0; i < n; i++) {
			
			for (int j = 0; j < m; j++) {
				
				scanf("%c", &h);
				if (h == '.') a[i][j] = 4;
				if (h == '^') a[i][j] = 1;
				if (h == 'v') a[i][j] = 2;
				if (h == '<') a[i][j] = 0;
				if (h == '>') a[i][j] = 3;
 			}
			scanf("%c", &h);
		}
		// for (int i = 0; i < n; i++) {
		// 	for (int j = 0; j < m; j++) {
		// 		cout << a[i][j];
		// 	}
		// 	cout << endl;
		// }
		
		int ans = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (a[i][j] != 4) {
					if (!encounter(i, j, a[i][j])) {
						bool u = false;
						ans++;
						for (int k = 0; k < 4; k++) {
							if (a[i][j] != k && encounter(i, j, k)) {
								u = true;
								break;
							}
						}
						if (!u) {
							ans = -1;
							break;
						}
					}

				}
			}
			if (ans == -1) {
				break;
			}
		}
		if (ans == -1) {
			cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << tt << ": " << ans << endl;
		}
	}	

}