#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <queue>
#include <map>
#include <set>
 

using namespace std;


int t;
string s[1001];


int main() {
	freopen("inputtt.txt", "r", stdin);
	freopen("outputtt.txt", "w", stdout);
	cin >> t;
	for (int iii = 0; iii < t; iii++) {
		int r, c;
		cin >> r >> c;
		for (int i = 0; i < r; i++) {
			cin >> s[i];
		}
		int ans = 0;
		bool hhh = true;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (s[i][j] != '.') {
					if (s[i][j] == '>') {
						bool b = true;
						for (int i1 = j + 1; i1 < c; i1++) {
							if (s[i][i1] != '.') {
								b = false;
								break;
							}
						}
						ans += b;
					}
					if (s[i][j] == '<') {
						bool b = true;
						for (int i1 = 0; i1 < j; i1++) {
							if (s[i][i1] != '.') {
								b = false;
								break;
							}
						}
						ans += b;
					}
					if (s[i][j] == '^') {
						bool b = true;
						for (int i1 = 0; i1 < i; i1++) {
							if (s[i1][j] != '.') {
								b = false;
								break;
							}
						}
						ans += b;
					}
					if (s[i][j] == 'v') {
						bool b = true;
						for (int i1 = i + 1; i1 < r; i1++) {
							if (s[i1][j] != '.') {
								b = false;
								break;
							}
						}
						ans += b;
					}
					int h = 0;
					for (int i1 = 0; i1 < c; i1++) {
						if (s[i][i1] != '.') {
							h++;
						}
					}
					int h1 = 0;
					for (int i1 = 0; i1 < r; i1++) {
						if (s[i1][j] != '.') {
							h1++;
						}
					}
					if (h + h1 == 2) {
						hhh = false;
					} 
 				}
			}
		}
		if (hhh) {
			printf("Case #%d: %d\n", iii + 1, ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", iii + 1);
		}
	}
 	return 0;
}
