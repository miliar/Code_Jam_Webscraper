#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
using namespace std;

int t, a[4], cnt, tmp, x, ans;

int main () {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	int cases = 0;
	while(t--) {
		cnt = 0;
		scanf("%d", &tmp);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &x);
				if (i+1 == tmp) {
					a[j] = x;
				}
			}
		}
		scanf("%d", &tmp);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &x);
				if (i+1 == tmp) {
					for (int k = 0; k < 4; k++) {
						if (a[k] == x) {
							cnt ++;
							ans = x;
							break;
						}
					}	
				}
			}
		}
		printf("Case #%d: ", ++cases);
		if (cnt == 1) {
			printf("%d\n", ans);
		} else if (cnt > 1) {
			puts("Bad magician!");
		} else {
			puts("Volunteer cheated!");
		}
	}
	return 0;
}
