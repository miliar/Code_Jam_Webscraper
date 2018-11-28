#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

int have[40][3];
int s[40][6000];

int ans[6000];

void cal(int from, int to, int n, int move){
	if(from + 2 == to){
		if(move == 0) {
			ans[from] = 0;
			ans[from + 1] = 1;
		}
		if(move == 1) {
			ans[from] = 0;
			ans[from + 1] = 2;
		}
		if(move == 2) {
			ans[from] = 1;
			ans[from + 1] = 2;
		}
		return;
	}
	int a[2][3];
	for(int j = 0; j < 3; j++){
		a[0][j] = have[n - 1][(j + move) % 3];
		a[1][j] = have[n - 1][(j + 2 + move) % 3];
	}
	int ans = 0;
	for(int i = 0; i < 3; ++i){
		if(a[0][i] != a[1][i]){
			if(a[0][i] > a[1][i]) ans = 0;
			else ans = 1;
			break;
		}
	}
	if(ans == 0){
		cal(from, (from + to) / 2, n - 1, move);
		cal((from + to) / 2, to, n - 1, (move + 2) % 3);
	}else {
		cal(from, (from + to) / 2, n - 1, (move + 2) % 3);
		cal((from + to) / 2, to, n - 1, move);
	}
}

int main() {
	s[1][0] = 0;
	s[1][1] = 1;
	have[1][0] = have[1][1] = 1;
	for(int i = 2; i < 13; ++i){
		for(int j = 0; j < 3; j++){
			have[i][j] = have[i - 1][j] + have[i - 1][(j + 2) % 3];
		}
		for(int j = 0; j < (1<<i); j++){
			if(j % 2 == 0) {
				s[i][j] = s[i - 1][j / 2];
			} else {
				if(s[i - 1][j / 2] == 0) s[i][j] = 1;
				if(s[i - 1][j / 2] == 1) s[i][j] = 2;
				if(s[i - 1][j / 2] == 2) s[i][j] = 0;
			}
		}
	}
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		int n, a[5];
		scanf("%d%d%d%d", &n, a + 1, a, a + 2);
		int flag = 0;
		for(int i = 0; i < 3; ++i){
			int ok = 1;
			for(int j = 0; j < 3; ++j){
				if(a[j] != have[n][(j + i) % 3]) ok = 0;
			}
			if(ok == 1 && flag == 0){
				flag = 1;
				printf("Case #%d: ", cc);
				cal(0, (1<<n), n, i);
				for(int j = 0; j < (1<<n); j++) {
					if(ans[j] == 0){
						printf("P");
					}
					if(ans[j] == 1){
						printf("R");
					}
					if(ans[j] == 2){
						printf("S");
					}
				}
				printf("\n");
			}
		}
		if(flag == 0) printf("Case #%d: IMPOSSIBLE\n", cc);
	}
	return 0;
}



