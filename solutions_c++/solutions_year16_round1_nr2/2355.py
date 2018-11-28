#include <bits/stdc++.h>
using namespace std;

const int MAXN = 55;

int N,solution[MAXN];
vector<vector<int>> soldados,grid;
bool solved,chosen[2*MAXN];

bool is_valid(int sr,int n) {
	if (n == 0) return true;
	for (int i=0; i<N; i++) {
		if (soldados[sr][i] <= grid[n-1][i])
			return false;
	}
	return true;
}

bool matchX(int r,int sr) {
	for (int i=0; i<N; i++) {
		if (grid[i][r] != soldados[sr][i])
			return false;
	}
	return true;
}

pair<int,int> get_miss() {
	int misses = 0, col = -1;
	bool ccol[2*MAXN];
	fill(ccol,ccol+2*MAXN,false);
	for (int j=0; j<N; j++) {
		bool hasMatch = false;
		for (int i=0; i<2*N-1; i++) {
			if (chosen[i]) continue;
			if (ccol[i]) continue;
			if (matchX(j,i)) {
				hasMatch = true;
				ccol[i] = true;
				break;
			}
		}
		if (!hasMatch) {
			misses++; col = j;
		}
	}
	return make_pair(misses,col);
}

void solve(int curRow) {
	if (curRow == N) {
		pair<int,int> missing = get_miss();
		if (missing.first == 1) {
			for (int i=0; i<N; i++)
				solution[i] = grid[i][missing.second];
		}
		return;
	}
	for (int i=0; i<2*N-1; i++) {
		if (chosen[i]) continue;
		if (is_valid(i,curRow)) {
			grid.push_back(soldados[i]);
			chosen[i] = true;

			solve(curRow+1);
			grid.pop_back();
			chosen[i] = false;
		}
	}
}

int main() {
	int T; scanf("%d",&T);
	for (int tt=1; tt<=T; tt++) {
		scanf("%d",&N);
		soldados.clear();
		solved = false;
		for (int i=0; i<2*N-1; i++) {
			soldados.push_back(vector<int>());
			for (int j=0; j<N; j++) {
				int S; scanf("%d",&S);
				soldados[i].push_back(S);
			}
		}
		fill(chosen,chosen+2*N,false);
		solve(0);
		printf("Case #%d: ",tt);
		for (int i=0; i<N; i++)
			printf("%d ",solution[i]);
		printf("\n");
	}
	return 0;
}