#include <iostream>
#include<stdio.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <stack>
#include <list>
#include <set>
#include <functional>
using namespace std;
const int inf = 98765432;
#define max(a,b) (a>b ? a:b)
#define min(a,b) (a<b ? a:b)

int d_x[4] = { 0, 0, 1, -1 };
int d_y[4] = { 1, -1, 0, 0 };
//struct Edge{
//	int W;
//	int x;
//	int y;
//	Edge(int W, int x, int y) :W(W), x(x), y(y){}
//};
//bool comp(Edge a ,Edge b){
//	return a.W < b.W;
//}
//vector<Edge> vt;
//bool in_range(int pre_index, int cur_index){
//	int cur_x = vt[cur_index].x;
//	int cur_y = vt[cur_index].y;
//	int pre_x = vt[pre_index].x;
//	int pre_y = vt[pre_index].y;
//	for (int i = 0; i < 4; i++){
//		int range_x = cur_x + d_x[i];
//		int range_y = cur_y + d_y[i];
//		if (pre_x == range_x && pre_y == range_y){
//			return true;
//		}
//
//	}
//	return false;
//}
//void dfs(int x, int y){
//	for (int i = 0; i < 4; i++){
//		int next_x = x + d_x[i];
//		int next_y = y + d_y[i];
//		if (A[next_x][next_y] > A[x][y] && D[next_x][next_y] < D[x][y] + 1){
//			D[next_x][next_y] = D[x][y] + 1;
//			dfs(next_x, next_y);
//		}
//	}
//}


//long long DP(long long L, long long R){
//	if (D[L][R]){
//		return D[L][R];
//	}
//	if (L >= R){
//		return 1;
//	}
//	D[L][R] = DP(L + 1, R);
//	if (S[L] == '('){
//		for (int i = L + 1; i <= R; i++){
//			if (S[i] == ')'){
//				D[L][R] += DP(L + 1, i - 1)*DP(i + 1, R);
//			}
//		}
//	}
//	else if (S[L] == '['){
//		for (int i = L + 1; i <= R; i++){
//			if (S[i] == ']'){
//				D[L][R] += DP(L + 1, i - 1)*DP(i + 1, R);
//			}
//		}
//	}
//	//printf("D[%d][%d] = %d\n", L, R, D[L][R]);
//
//	return D[L][R];
//}
bool C[101];
bool Check(int size){
	for (int i = 0; i < size; i++){
		if (C[i] == false){
			return false;
		}
	}
	return true;
}
int main(void) {
	int T;
	string s;
	cin >> T;
	for(int i=1;i<=T;i++){
		cin >> s;
		int size = s.size();
		for (int i = 0; i < size; i++){
			if (s[i] == '+'){
				C[i] = true;
			}
		}
		long long ans = 0;
		while (!Check(size)){
			int count = 0;
			bool init = C[count];
			while (init == C[count]){ // 다를떄까지
				C[count] = !C[count];
				count++;
			}
			ans++;
		}
		printf("Case #%d: %lld\n",i, ans);
		memset(C, 0, sizeof(C));
	}
}