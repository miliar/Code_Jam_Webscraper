#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<math.h>
#include<string>
#include<map>
#include<set>
//#pragma comment(linker, "/STACK:36777216") //if stack overflow
using namespace std;

#define LarN 100000
typedef long long LL;
const double d_pi = 57.2957795;

template<class T> inline void ReMin(T &a,T b){if(b<a) a=b;}
template<class T> inline void ReMax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}

char board[105][105];
bool sig[105][105];
int R,C;
pair<int, int> findNext(int r, int c, int dir){

	if(dir == 0){
		for(int i = r-1; i >= 1; i --){
			if(board[i][c] != '.'){
				return make_pair(i, c);
			}
		}
	}
	else if(dir == 1){
		for(int i = c + 1; i <= C; i ++){
			if(board[r][i] != '.'){
				return make_pair(r, i);
			}
		}
	}
	else if(dir == 2){
		for(int i = r + 1; i <= R; i ++){
			if(board[i][c] != '.'){
				return make_pair(i, c);
			}
		}
	}
	else if(dir == 3){
		for(int i = c - 1; i >= 1; i --){
			if(board[r][i] != '.'){
				return make_pair(r, i);
			}
		}
	}
	return make_pair(-1,-1);
}

pair<int, int> findAny(int r, int c){
	pair<int, int> ret = make_pair(-1,-1);
	for(int i = 0; i < 4; i ++){
		ret = findNext(r, c, i);
		if(ret.first > 0) return ret;
	}
	return ret;
}
void solve(){
	scanf("%d%d", &R, &C);
	memset(sig, 0, sizeof(sig));
	for(int i = 1; i <= R; i ++){
		scanf("%s", board[i]+1);
	}
	int ans = 0;
	pair<int, int> next;
	bool flag = true;
	for(int i = 1; i <= R; i ++)for(int j = 1; j <= C; j ++){
		if(sig[i][j] || board[i][j] == '.') continue;
		int r = i, c = j;
		while(1){
			sig[r][c] = true;
			if(board[r][c] == '^')next = findNext(r,c, 0);
			else if(board[r][c] == '>') next = findNext(r, c, 1);
			else if(board[r][c] == 'v') next = findNext(r, c, 2);
			else next = findNext(r,c, 3);
			if(next.first < 0){
				next = findAny(r, c);
				ans ++;
			}
			if(next.first < 0){
				flag = false;
				break;
			}
			r = next.first;
			c = next.second;
			if(sig[r][c]) break;
		}
		if(!flag) break;
	}
	if(!flag){
		printf("IMPOSSIBLE\n");
	}
	else printf("%d\n", ans);
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T_case;
	cin>>T_case;
	for(int i_case = 1; i_case <= T_case; i_case ++){
		printf("Case #%d: ", i_case);
		solve();
	}
	return 0;
}