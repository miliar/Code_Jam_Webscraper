/*************************************************************************
    > File Name: A.cpp
    > Author: hnu0314
    > Mail: hnu0314@126.com 
    > Created Time: 2013/4/13 10:44:03
 ************************************************************************/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
typedef long long LL;
const int MAXN = 1<<16; 
const int INF = 0;

int win_state[11];
int win_cnt;

void gen_win_state(char map[][4]){

	memset(win_state, 0, sizeof(win_state));
	win_cnt = 0;

	for(int i = 0; i < 4; ++i){
		int cnt_T(0);
		for(int j = 0; j < 4; ++j){
			if(map[i][j] == 'T')  ++cnt_T;
			win_state[win_cnt] |= 1<<(i * 4 + j);
		}
		if(cnt_T > 1)   win_state[win_cnt] = -1;
		++win_cnt;

		cnt_T = 0;
		for(int j = 0; j < 4; ++j){
			if(map[i][j] == 'T')  ++cnt_T;
			win_state[win_cnt] |= 1<<(j * 4 + i);
		}
		if(cnt_T > 1)  win_state[win_cnt] = -1;
		++win_cnt;
	}
	int cnt_T(0);
	for(int i = 0; i < 4; ++i){
		win_state[win_cnt] |= 1<<(i * 4 + i);
		if(map[i][i] == 'T') ++cnt_T;
	}
	if(cnt_T > 1)  win_state[win_cnt] = -1;
	++win_cnt;
	cnt_T = 0;
	for(int i = 0; i < 4; ++i){
		win_state[win_cnt] |= 1<<(i * 4 + (3 - i));
		if(map[i][3 - i] == 'T')  ++cnt_T;
	}
	if(cnt_T > 1) win_state[win_cnt] = -1;
	++win_cnt;
}


int state_o, state_x, state_t;

char map[4][4];

void solve(){
	
	state_o = state_x = state_t = 0;
	int cnt_point(0);
	for(int i = 0;i < 4; ++i){
		scanf("%s", map[i]);
		for(int j = 0; j < 4; ++j){
			if(map[i][j] == 'T')  state_t |= 1<<(i * 4 + j);
			if(map[i][j] == 'X')  state_x |= 1<<(i * 4 + j);
			if(map[i][j] == 'O')  state_o |= 1<<(i * 4 + j);
			if(map[i][j] == '.')  ++cnt_point;
		}
	}
	gen_win_state(map);
	int win(-2);
	for(int i = 0; i < win_cnt; ++i){
		if( (win_state[i] & ( state_t | state_o)) == win_state[i] )  win = 0;
		if( (win_state[i] & ( state_t | state_x)) == win_state[i] )  win = 1;
	}
	if(win == -2){
		if(cnt_point == 0)  puts("Draw");
		else  puts("Game has not completed");
	}else if(win == 0)  {
		puts("O won");
	}else {
		puts("X won");
	}

}

int main(){
//	freopen("A-large.in", "r", stdin);
//	freopen("A_large-0.out", "w", stdout);
   int cas(1), test;
   scanf("%d", &test);
   while(test--){
	   printf("Case #%d: ", cas++);
	   solve();

   }
		return 0;
}
