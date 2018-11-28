#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <memory.h>
using namespace std;

char s[6][6];
int direct[4][2] = {1 , 0 , 0 , 1 , 1 , 1 , 1 , -1};

bool search(int x , int y , char c) {
	int cnt = 0;
	for (int i=0 ; i<4 ; i++) {
		cnt = 0;
		for (int j=0 ; j<4 ; j++) {
			int tempx = x + j * direct[i][0];
			int tempy = y + j * direct[i][1];
			if (tempx >= 0 && tempx < 4 && tempy>=0 && tempy<4) {
				if (s[tempx][tempy] == c || s[tempx][tempy] == 'T') {
					cnt++;
				}
				else break;
			}
			else break;
		}
		if (cnt == 4) return true;
	}
	return false;
}

bool isEnd() {
	for (int i=0 ; i<4 ; i++) {
		for (int j=0 ; j<4 ; j++) {
			if (s[i][j] == '.') return false;
		}
	}
	return true;
}

int main() {
//	freopen("1001.in" , "r" , stdin);
//	freopen("1001.out" , "w" , stdout);
	int T;
	int cas = 0;

	scanf("%d" , &T);	
	while (T--) {
		cas++;
		printf("Case #%d: " , cas);
		for (int i=0 ; i<4 ; i++) {
			scanf("%s" , s[i]);
		}

		bool ans = false;
		for (int i=0 ; i<4 ; i++) {
			for (int j=0 ; j<4 ; j++) {
				if (s[i][j] == 'T' || s[i][j] == 'X') {
					ans = search(i , j , 'X');
					if (ans) break;
				}
			}
			if (ans) break;
		}

		if (ans) {
			printf("X won\n");
			continue;
		}
		
		for (int i=0 ; i<4 ; i++) {
			for (int j=0 ; j<4 ; j++) {
				if (s[i][j] == 'T' || s[i][j] == 'O') {
					ans = search(i , j , 'O');
					if (ans) break;
				}
			}
			if (ans) break;
		}

		if (ans) {
			printf("O won\n");
			continue;
		}
		
		if (isEnd()) {
			printf("Draw\n");
			continue;
		}
		else {
			printf("Game has not completed\n");
			continue;
		}
	}
	return 0;
}
