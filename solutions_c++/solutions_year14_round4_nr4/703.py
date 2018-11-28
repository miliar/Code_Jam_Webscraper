#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <memory.h> 
#include <math.h> 
#include <assert.h> 
#include <stack> 
#include <queue> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <string> 
#include <functional> 
#include <vector> 
#include <deque> 
#include <utility> 
#include <bitset> 
#include <limits.h>  

using namespace std; 
typedef long long ll; 
typedef unsigned long long llu; 
typedef double lf;
typedef unsigned int uint;
typedef long double llf;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
#define memset0(x) memset(x, 0, sizeof (x));

int TC, TCC;

int N, M;
string S[100];
vector<string> T[100];
char tmp[100];

int res_node, res_cnt;

void init () {
	for(int i = 0; i < N; i++) T[i].clear();
	res_node = res_cnt = -123;
}
	
void solve (int w) {
	if(w == M) {
		int val = 0;
		for(int i = 0; i < N; i++) {
			if(T[i].empty()) return;
			for(int j = 0; j < T[i].size(); j++) {
				int s = 0;
				while(j > 0 && s < T[i][j].size() && s < T[i][j-1].size() && T[i][j-1][s] == T[i][j][s]) ++s;
				val += T[i][j].size() - s;
			}
		}
		if(val > res_node) res_node = val, res_cnt = 1;
		else if(val == res_node) ++res_cnt;
		return;
	}

	for(int i = 0; i < N; i++) {
		T[i].push_back(S[w]);
		solve(w+1);
		T[i].pop_back();
	}
}

void solve () {
	scanf("%d%d", &M, &N);
	for(int i = 0; i < M; i++) scanf("%s", tmp), S[i] = tmp;
	sort(S, S+M);

	solve(0);

	printf("Case #%d: %d %d\n", TCC, res_node + N, res_cnt);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &TC);
	while(++TCC <= TC) {
		init();
		solve();
	}
	return 0;
}