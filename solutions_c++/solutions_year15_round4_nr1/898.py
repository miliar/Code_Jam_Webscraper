#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <cassert>
#include <cmath>

#define INF 2000000000
#define MOD 1000000007

using namespace std;

char board[100][100];
int r, c;
char allDir[4] = {'<', '>', '^', 'v'};

pair<int, int> getDir(char c) {
	if (c == '<')
		return make_pair(0, -1);
	if (c == '>')
		return make_pair(0, 1);
	if (c == '^')
		return make_pair(-1, 0);
	if (c == 'v')
		return make_pair(1, 0);
	assert(false);
}

bool isInside(int a, int b) {
	return (a >= 0 && a < r && b >= 0 && b < c);
}

bool canBeGood(int a, int b) {
	bool isGood = false;
	int x = a, y = b;
	for (int i = 0; i < 4; i++) {
		a = x;
		b = y;
		pair<int, int> dir = getDir(allDir[i]);
		while (isInside(a + dir.first, b + dir.second)) {
			a += dir.first;
			b += dir.second;
			if (board[a][b] != '.') {
				isGood = true;
				break;
			}
		}
	}
	return isGood;
}	

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": ";
		cin >> r >> c;
		for (int i = 0; i < r; i++) {
			string s;
			cin >> s;
			for (int j = 0; j < s.length(); j++) {
				board[i][j] = s[j];
			}
		}
		int ans = 0;
		bool isPossible = true;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (board[i][j] == '.')
					continue;
				int a = i;
				int b = j;
				pair<int, int> dir = getDir(board[i][j]);
				bool hasArrow = false;
				while (isInside(a + dir.first, b + dir.second)) {
					a += dir.first;
					b += dir.second;
					if (board[a][b] != '.') {
						hasArrow = true;
						break;
					}
				}
				a = i;
				b = j;
				if (!hasArrow) {
					if (canBeGood(a, b))
						ans++;
					else
						isPossible = false;
				}
			}
		}
		if (!isPossible) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		cout << ans << endl;
	}
	return 0;
}
