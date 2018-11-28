#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <sstream>
#include <deque>

#define ll long long
using namespace std;

int gcd(int x, int y){ if(y == 0) return x; return gcd(y, x % y);}
int lcm(int x, int y){ return x * y / gcd(x, y); }

vector<int> getIntUntilEnter(){
    string line;
    getline(cin,line);
    vector<int> ins;
    int x;
    stringstream ss(line);
    while (ss >> x) ins.push_back(x);
	return ins;
}
int t,r,c,m;
int board[51][51];
bool in(int i, int j){
	return (0 <= i && i < r) && (0 <= j && j < c);
}
int dx[3] = {-1,-1,0};
int dy[3] = {0,-1,-1};

int di[8] = {-1,-1,0,1,1,1,0,-1};
int dj[8] = {0,1,1,1,0,-1,-1,-1};
const int INF = 100;
bool visit[51][51];
bool check(){
	memset(visit, 0, sizeof(visit));
	int start = -1;
	for(int i = 0; i < r; ++i)
		for(int j = 0; j < c; ++j)
			if(board[i][j] == 'c'){
				start = i * INF + j;
				visit[i][j] = true;
				break;
			}
	if(start == -1) {
		printf("start -1\n");
		return false;
	}
	int leftc = r * c - m - 1; 
	deque<int> q;
	q.push_back(start);
	while(q.size()){
		int cur = q[0], curi = cur / INF, curj = cur % INF;
		q.pop_front();
		int mcount = 0;
		for(int k = 0; k < 8; ++k){
			int ii = curi + di[k];
			int jj = curj + dj[k];
			if(in(ii, jj)){
				 if(board[ii][jj] == '*') ++mcount;
			}
		}
		if(mcount) continue;
		else {
			for(int k = 0; k < 8; ++k){
				int ii = curi + di[k];
				int jj = curj + dj[k];
				if(in(ii, jj) && !visit[ii][jj] && (board[ii][jj] == '.')){

					q.push_back(ii * INF+ jj);
					visit[ii][jj] = true;
					leftc--;
				} 
			}
		}
	}
/*
for(int i = 0; i < r; ++i){
	for(int j = 0; j < c; ++j){
		printf("%d",visit[i][j]);
	}
	printf("\n");
}
*/
	if(leftc) return false;
	else return true;	
}

void prt(){
printf("\n");
//printf("%d %d\n", r, c);
	for(int i = 0; i < r; ++i){
		for(int j = 0; j < c; ++j){
			printf("%c",board[i][j]);
		}
		printf("\n");
	}
printf("\n");
}

bool rec(int i, int left){
	if(!left) {
		if(board[r-1][c-1] == '*') return false;
		board[r-1][c-1] = 'c';
//prt();
		bool ret = check();
//		printf("%d\n", ret);
		return ret;
	} else if(i >= r) return false;
	for(int p = 0; p < c; ++p){
		board[i][p] = '*';
		if(rec(i + 1, left - p - 1)) return true;
	}
	for(int p = 0; p < c; ++p)
		board[i][p] = '.';
	return false;
}

int main(){
	scanf("%d", &t);
	for(int test = 1; test <= t; ++test){
		bool possibles = false;
		scanf("%d%d%d", &r,&c,&m);
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j)
				board[i][j] = '.';
		}
		int mines = m;
		possibles = rec(0, m);

//printf("%d %d %d\n", r,c,m);

		if(!possibles) printf("Case #%d:\nImpossible\n", test);
		else {
//		if(check() == false) printf("Wrong\n");
//		if(minecheck != m) printf("Mine\n");
		printf("Case #%d:\n", test);
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				printf("%c",board[i][j]);
			}
			printf("\n");
		}
		}
	}
	return 0;
}
