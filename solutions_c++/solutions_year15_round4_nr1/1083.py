#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int T, r, c;
string M[143];

int search(int i, int j, char op) {
	int d[2];
	d[0] = 0, d[1] = 0;
	switch (op) {
		case '^': d[1] = -1; break;
		case '>': d[0] = 1; break;
		case '<': d[0] = -1; break;
		case 'v': d[1] = 1; break;
		default: return 0;
	}
	int rr = i + d[1], cc = j + d[0];
	int flag = -1;
	while (rr >= 0 && rr < r && cc >= 0 && cc < c){
		if (M[rr][cc] != '.') {
			flag = 0; return 0;
		}
		rr += d[1], cc += d[0];
	}
	if (flag < 0) return -1;
	//cout << i << " " << j << " " << op << endl;
	return 0;
}

int main() {
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cin >> r >> c;
		bool imp = false;
		int res = 0;
		for (int i = 0; i < r; i++) cin >> M[i];
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				

				int flag = search(i, j, M[i][j]);
				int ans = -1;
				if (flag == -1) {
					if (M[i][j] != '^') ans = search(i, j, '^');
					if (ans >= 0) {
						res += 1;
						continue;
					}
					if (M[i][j] != '>') ans = search(i, j, '>');
					if (ans >= 0) {
						res += 1;
						continue;;
					}					
					if (M[i][j] != '<') ans = search(i, j, '<');
					if (ans >= 0) {
						res += 1;
						continue;
					}
					if (M[i][j] != 'v') ans = search(i, j, 'v');
					if (ans >= 0) {
						res += 1;
						continue;
					}
					imp = true;
					break;
				}
				
			}
			if (imp) break;
		}

		if (imp) {
			cout << "Case #" << test << ": IMPOSSIBLE"<< endl; 	
		}
		else
			cout << "Case #" << test << ": " << res << endl; 
	}
	return 0;
}
