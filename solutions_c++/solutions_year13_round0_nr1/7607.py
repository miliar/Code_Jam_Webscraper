#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <queue>
#include <algorithm>
#include <stack>
using namespace std;
 
typedef long long LL;
 
const int MAXN = 55;
const int inf = 0x7f7f7f7f;
 

char str[10][10];


void input() {
	for(int i = 0; i < 4; i++) {
		scanf("%s", str[i]);
	}
}

int solve() {

	for(int i = 0; i < 4; i++) {
		int cx = 0, co = 0, ct = 0;
		for(int j = 0; j < 4; j++) {
			if(str[i][j] == 'T') ct++;
			else if(str[i][j] == 'X') cx++;
			else if(str[i][j] == 'O') co++;
		}
		if(cx == 4 || cx == 3 && ct == 1) return 1;
		if(co == 4 || co == 3 && ct == 1) return 2;
	}

	for(int i = 0; i < 4; i++) {
		int cx = 0, co = 0, ct = 0;
		for(int j = 0; j < 4; j++) {
			if(str[j][i] == 'T') ct++;
			else if(str[j][i] == 'X') cx++;
			else if(str[j][i] == 'O') co++;
		}
		if(cx == 4 || cx == 3 && ct == 1) return 1;
		if(co == 4 || co == 3 && ct == 1) return 2;
	}

	int cx = 0, co = 0, ct = 0;
	for(int i = 0; i < 4; i++) {
		if(str[i][i] == 'T') ct++;
		else if(str[i][i] == 'X') cx++;
		else if(str[i][i] == 'O') co++;
	}
	if(cx == 4 || cx == 3 && ct == 1) return 1;
	if(co == 4 || co == 3 && ct == 1) return 2;

	cx = 0, co = 0, ct = 0;
	for(int i = 0, j = 3; i < 4; i++, j--) {
		if(str[i][j] == 'T') ct++;
		else if(str[i][j] == 'X') cx++;
		else if(str[i][j] == 'O') co++;
	}
	if(cx == 4 || cx == 3 && ct == 1) return 1;
	if(co == 4 || co == 3 && ct == 1) return 2;


	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(str[i][j] == '.') return 3;
		}
	}
	return 4;
}

int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("output.out", "w", stdout);
	int T;
	scanf("%d", &T);
	while(T--) {
		input();
		int ans = solve();
		static int cas = 1;
		printf("Case #%d: ", cas++);
		if(ans == 1) printf("X won");
		else if(ans == 2) printf("O won");
		else if(ans == 3) printf("Game has not completed");
		else printf("Draw");
		printf("\n");
	}

}