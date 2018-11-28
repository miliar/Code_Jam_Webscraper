#include <iostream>
#include <vector>
#include <iomanip>
#include <queue>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <climits>
#include <stdint.h>
#include <utility>
#include <set>
#include <stack>
#define DEBUG 0
#define LOG if(DEBUG)
using namespace std;
typedef int64_t intt;
#define MAX_VAL	LLONG_MAX 
#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((y) > (x) ? (x) : (y))
template <typename T>
void printvec(vector<T> v) {
	for(typename vector<T>::iterator it = v.begin(); it != v.end(); it++) {
		cout << *it << ' ';
	}
}

int dx[] = {0, 1, -1, 0, 0};
int dy[] = {0, 0, 0, 1, -1};

int R, C;

bool valid(int x, int y) {
	return x >= 0 && x < R && y >= 0 && y < C;
}

void code() {
	cin >> R >> C;
	vector<vector<int> > g(R, vector<int>(C, 0));
	for(int i = 0; i < R; i++) {
		string s;
		cin >> s;
		for(int j = 0; j < C; j++) {
			int v = 0;
			switch(s[j]) {
			case '>': v = 3; break;
			case '^': v = 2; break;
			case '<': v = 4; break;
			case 'v': v = 1; break;
			default: v = 0; break;
			}
			g[i][j] = v;
		}
	}

	int num = 0;
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			if(g[i][j] != 0) {
				int nj = j + dy[g[i][j]], ni = i + dx[g[i][j]];
				while(valid(ni, nj) && g[ni][nj] == 0) {
					ni += dx[g[i][j]];
					nj += dy[g[i][j]];
				}
				if(!valid(ni, nj)) {
					int d = 1;
					for(; d <= 4; d++) {
						nj = j + dy[d]; ni = i + dx[d];
						while(valid(ni, nj) && g[ni][nj] == 0) {
							ni += dx[d];
							nj += dy[d];
						}
						if(valid(ni, nj)) {
							num++;
							break;
						}
					}
					if(d == 5) {
						cout << "IMPOSSIBLE" << endl;
						return;
					}
				}
			}
		}
	}

	cout << num << endl;
}

int main(int argc, char **argv) {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		code();
	}
}

