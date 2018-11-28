#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>

char buf[150][150];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int R, C;
		scanf("%d %d", &R, &C);
		for (int i=0; i<R; i++) {
			scanf("%s", buf[i]);
		}
		int cnt = 0;
		for (int i=0; i<R && cnt >= 0; i++) {
			for (int j=0; j<C && cnt >= 0; j++) {
				bool death = false;
				if (buf[i][j] == '^') {
					death = true;
					for (int k=i-1; k>=0; k--) {
						if (buf[k][j] != '.') {
							death = false;
							break;
						}
					}
				} else if (buf[i][j] == 'v') {
					death = true;
					for (int k=i+1; k<R; k++) {
						if (buf[k][j] != '.') {
							death = false;
							break;
						}
					}
				} else if (buf[i][j] == '<') {
					death = true;
					for (int k=j-1; k>=0; k--) {
						if (buf[i][k] != '.') {
							death = false;
							break;
						}
					}
				} else if (buf[i][j] == '>') {
					death = true;
					for (int k=j+1; k<C; k++) {
						if (buf[i][k] != '.') {
							death = false;
							break;
						}
					}
				}
				if (death) {
					for (int k=i-1; k>=0; k--) {
						if (buf[k][j] != '.') {
							death = false;
							break;
						}
					}
					for (int k=i+1; k<R; k++) {
						if (buf[k][j] != '.') {
							death = false;
							break;
						}
					}
					for (int k=j-1; k>=0; k--) {
						if (buf[i][k] != '.') {
							death = false;
							break;
						}
					}
					for (int k=j+1; k<C; k++) {
						if (buf[i][k] != '.') {
							death = false;
							break;
						}
					}
					if (death) {
						cnt = -1;
					} else {
						cnt++;
					}
				}
			}
		}
		if (cnt < 0) {
			printf("Case #%d: IMPOSSIBLE\n", t);	
		} else {
			printf("Case #%d: %d\n", t, cnt);
		}
	}
	return 0;
}
