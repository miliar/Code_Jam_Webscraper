#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("D-small-attempt3.in", "r", stdin);
	freopen("outputagrvai.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test<=t; test++) {
		int x, r, c;
		bool gab = false;
		scanf(" %d %d %d", &x, &r, &c);
		//printf(" %d %d %d\n", x, r, c);
		if(r<c) swap(r, c);
		if(x == 1) {
			//printf("111 ");
			gab = true;
		}
		else if(x == 2) {
			//printf("222 ");
			if(r%2 == 0 || c%2 == 0) {
				gab = true;
			}
			else {
				gab = false;
			}
		}
		else if(x == 3) {
			//printf("333 ");
			if((r*c)%3 == 0 && c>=2) gab = true;
			else gab = false;
		}
		else {
			if(r == 4 && (c == 3 || c == 4)) gab = true;
			else gab = false;
		}
		printf("Case #%d: %s\n", test, gab?"GABRIEL":"RICHARD");
	}
	return 0;
}