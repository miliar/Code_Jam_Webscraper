#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <stdlib.h>
#include <assert.h>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;
typedef long long lint;
char mm[105][105];
int r, c, deg[105][105];
int cntr[105], cntc[105];

int dir[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int main() {
	int t;
	scanf("%d", &t);
	for(int cas = 1; cas <= t; cas++) {
		scanf("%d%d", &r, &c);
		for(int i = 0; i < r; i++) {
			scanf("%s", mm[i]);
		}
		memset(deg, 0, sizeof(deg));
		memset(cntr, 0, sizeof(cntr));
		memset(cntc, 0, sizeof(cntc));

		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				if(mm[i][j] != '.') {
					cntr[i]++;
					cntc[j]++;
					int dx, dy;
					if(mm[i][j] =='^') {
						dx = -1, dy = 0;
					}
					else if(mm[i][j] == 'v') {
						dx = 1, dy = 0;
					}
					else if(mm[i][j] == '<') {
						dx = 0, dy = -1;
					}
					else if(mm[i][j] == '>') {
						dx = 0, dy = 1;
					}

					for(int x = i + dx, y = j + dy; ; x += dx, y+= dy) {
						if(x >= 0 && x < r && y >= 0 && y < c) {
							if(mm[x][y] != '.') {
								deg[i][j] = 1;
								break;
							}
						}
						else {
							break;
						}
					}
				}
			}
		}
		bool ok = true;
		int ans = 0;
		for(int i = 0; i < r && ok; i++) {
			for(int j = 0; j < c; j++) {
				if(mm[i][j] != '.' && deg[i][j] == 0) {
					if(cntr[i] + cntc[j] > 2) {
						ans++;
					}
					else {
						ok = false;
						break;
					}
				}
			}
		}
		printf("Case #%d: ", cas);
		if(!ok) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}
