#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, x, y) for(int i = (x); i <= (y); i++)
#define RFOR(i, x, y) for(int i = (x); i >= (y); i--)

#define REMIN(x, y) x = (x < (y)) ? x : (y)
#define REMAX(x, y) x = (x > (y)) ? x : (y)

//#define DEBUG

#ifndef DEBUG
#define ISDEBUG false
#define PRINT(x)
#else
#define ISDEBUG true
#define PRINT(x) cout << #x << ": " << x << endl
#endif
#define IFDEBUG() if(ISDEBUG)

using namespace std;

#define MAX 1024

int N, M, K, ans;
int _map[MAX][MAX], list[MAX * MAX][2], cl;

void read_input() {
	scanf("%d %d %d", &N, &M, &K);
}

void add_list(int x, int y) {
	_map[x][y] = 1;
	list[cl][0] = x;
	list[cl][1] = y;
	cl++;
}

void check_add_list(int x, int y) {
	if(x < 1 || x > N)return;
	if(y < 1 || y > M)return;
	if(_map[x][y] != 0)return;
	add_list(x, y);
}

int get_map(int x, int y) {
	if(x < 1 || x > N)return 0;
	if(y < 1 || y > M)return 0;
	return _map[x][y];
}

void check_enclose(int x, int y) {
	if(x < 1 || x > N)return;
	if(y < 1 || y > M)return;
	if(_map[x][y] != 2)return;
	if(get_map(x - 1, y) < 2)return;
	if(get_map(x + 1, y) < 2)return;
	if(get_map(x, y - 1) < 2)return;
	if(get_map(x, y + 1) < 2)return;
	ans--;
	_map[x][y] = 3;
}

void add_stone(int x, int y) {
	ans++;
	_map[x][y] = 2;

	check_enclose(x - 1, y);
	check_enclose(x + 1, y);
	check_enclose(x, y - 1);
	check_enclose(x, y + 1);

	check_add_list(x - 1, y);
	check_add_list(x + 1, y);
	check_add_list(x, y - 1);
	check_add_list(x, y + 1);

	check_add_list(x - 1, y - 1);
	check_add_list(x - 1, y + 1);
	check_add_list(x + 1, y - 1);
	check_add_list(x + 1, y + 1);
}

int get_score(int x, int y) {
	if(get_map(x - 1, y - 1) == 2 && get_map(x - 1, y) == 2 && get_map(x, y - 1) == 2)return 1000000000 + x * 1000 + y;

	if(get_map(x - 1, y - 1) == 2 && get_map(x, y - 1) == 2 && get_map(x + 1, y - 1) == 2)return 110000000 + x * 1000 + y;
	if(get_map(x - 1, y - 1) == 2 && get_map(x - 1, y) == 2 && get_map(x - 1, y + 1) == 2)return 100000000 + x * 1000 + y;

	int score = 0;

	score += get_map(x - 1, y);
	score += get_map(x + 1, y);
	score += get_map(x, y - 1);
	score += get_map(x, y + 1);

	score += get_map(x - 1, y - 1);
	score += get_map(x - 1, y + 1);
	score += get_map(x + 1, y - 1);
	score += get_map(x + 1, y + 1);

	return score;

//	if(get_map(x - 1, y) == 2 && get_map(x, y - 1) == 2)return 12000000 + x * 1000 + y;
//	if(get_map(x - 1, y) == 2 && get_map(x, y + 1) == 2)return 11000000 + x * 1000 + y;
//	if(get_map(x + 1, y) == 2 && get_map(x, y - 1) == 2)return 10000000 + x * 1000 + y;

//	return x * 1000 + y;
}

void next() {
	int b = 0;
	REP(i, cl) {
		if(i == 0)continue;
		if(get_score(list[b][0], list[b][1]) < get_score(list[i][0], list[i][1])) {
			b = i;
		}
	}

	add_stone(list[b][0], list[b][1]);
	cl--;
	list[b][0] = list[cl][0];
	list[b][1] = list[cl][1];
}

int find_ans() {
	read_input();

	if(N <= 2 || M <= 2)return K;
	if(K <= 4)return K;
	if(K == 5)return 4;
	if(N * M - K <= 4)return (N + M) * 2 - 4 - (N * M - K);

	ans = 4;
	cl = 0;

	FOR(i, 1, N) {
		FOR(j, 1, M) {
			_map[i][j] = 0;
		}
	}
	_map[1][2] = 2;
	_map[2][1] = 2;
	_map[2][2] = 3;
	_map[2][3] = 2;
	_map[3][2] = 2;

	add_list(3, 3);
	add_list(1, 3);
	add_list(3, 1);

	for(int k = 6; k <= K; k++) {
		next();
//		printf("\n");
//		FOR(i, 1, N) {
//			FOR(j, 1, M) {
//				printf("%d", _map[i][j]);
//			}
//			printf("\n");
//		}
	}

	return ans;
}

int main() {
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		printf("%d", find_ans());
		printf("\n");
	}

	return 0;
}
