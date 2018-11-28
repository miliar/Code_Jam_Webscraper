#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<complex>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)
// #define dprintf(...)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}

char board[4][4];

void doit(int q){
	bool full = true;
	for(int i=0; i<4; ++i){
		scanf("\n");
		for(int j=0; j<4; ++j){
			scanf("%c", &board[i][j]);
			if(board[i][j] == '.') full=false;
		};
	};

	for(int i=0; i<4; ++i){
		int X=0, O=0, T=0;
		for(int j=0; j<4; ++j){
			if(board[i][j] == 'X') X++;
			else if(board[i][j] == 'O') O++;
			else if(board[i][j] == 'T') T++;
		};
		if(X+T >= 4) {
			printf("Case #%d: X won\n", q);
			return;
		}else if(O+T >= 4){
			printf("Case #%d: O won\n", q);
			return;
		};
	};
	for(int i=0; i<4; ++i){
		int X=0, O=0, T=0;
		for(int j=0; j<4; ++j){
			if(board[j][i] == 'X') X++;
			else if(board[j][i] == 'O') O++;
			else if(board[j][i] == 'T') T++;
		};
		if(X+T >= 4) {
			printf("Case #%d: X won\n", q);
			return;
		}else if(O+T >= 4){
			printf("Case #%d: O won\n", q);
			return;
		};
	};
	int X=0, O=0, T=0;
	for(int i=0; i<4; ++i){
		if(board[i][i] == 'X') X++;
		else if(board[i][i] == 'O') O++;
		else if(board[i][i] == 'T') T++;
	};
	if(X+T >= 4) {
		printf("Case #%d: X won\n", q);
		return;
	}else if(O+T >= 4){
		printf("Case #%d: O won\n", q);
		return;
	};
	X=0, O=0, T=0;
	for(int i=0; i<4; ++i){
		if(board[3-i][i] == 'X') X++;
		else if(board[3-i][i] == 'O') O++;
		else if(board[3-i][i] == 'T') T++;
	};
	if(X+T >= 4) {
		printf("Case #%d: X won\n", q);
		return;
	} else if(O+T >= 4){
		printf("Case #%d: O won\n", q);
		return;
	};
	if(full){
		printf("Case #%d: Draw\n", q);
	}else{
		printf("Case #%d: Game has not completed\n", q);
	};
};

int main() {
	int T;
	scanf("%d", &T);
	for(int i=1; i<=T; ++i){
		doit(i);
	};
	return 0;
}

