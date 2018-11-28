#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<bitset>
#include<unordered_map>
#include<unordered_set>
using namespace std;
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FOE(i,a,b) for (int i=(a);i<=(b);i++)
#define INF (1 << 30)
#define EPS (1e-9)
#define REP(i,n) FOR(i,0,n)
#define LL long long
#define MOD 1000000007
#define N 200
int n, m;
int a[N][N];
int h[N][N];
int use[N];
int rw[N], cl[N];


vector<vector<int>> v;

int coverrow(int x, int row){
	FOR(i,0,n) if (h[row][i] != -1 && h[row][i] != v[x][i]){
		return 0;
	}
	return 1;
}

int covercol(int x, int col){
	FOR(i,0,n) if (h[i][col] != -1 && h[i][col] != v[x][i]) return 0;
	return 1;
}

int testrow(int x, int row){
	if (!coverrow(x, row)) return 0;
	//FOR(i,0,n) if (h[row][i] != -1 && h[row][i] != v[x][i]) return 0;
	return 1;
	/*
	int ok = 0, cnt = 0;
	FOR(i,row + 1,n){
		FOR(j,x + 1,2 * n - 1){
			if (coverrow(j, i)){
				ok = 1;
				break;
			}
		}
		if (!ok) cnt++;
		if (cnt >= 2) return 0;
	}
	*/
}

int testcol(int x, int col){
	if (!covercol(x, col)) return 0;
	return 1;
	/*
	int ok = 0, cnt = 0;
	FOR(i,col + 1,n){
		FOR(j,x + 1, 2 * n - 1){
			if (covercol(j, i)){
				ok = 1;
				break;
			}
		}
		if (!ok) cnt++;
		if (cnt >= 2) return 0;
	}
	return 1;
	*/
}

int ver(){
	vector<vector<int>> tv;
	tv.resize(2 * n - 1);
	FOR(i,0,n) FOR(j,0,n) tv[i].PB(h[i][j]);
	return 1;

}

void prt();

int dfs(int x){
	if (x >= 2 * n - 1) return 1;
	
	//printf("%d %d %d\n", x, rw[x], cl[x]);
	//printf("v ");
	//for (auto i : v[x]) printf("%d ", i);puts("");
	//prt();
	if (rw[x] != -1){
		if (testrow(x, rw[x])){
			int mk[N];
			FOR(i,0,n) mk[i] = h[rw[x]][i] == -1 ? 1 : 0;
			FOR(i,0,n) if (h[rw[x]][i] == -1) h[rw[x]][i] = v[x][i];
			if (dfs(x + 1)) return 1;
			FOR(i,0,n) if (mk[i]) h[rw[x]][i] = -1;
		}
	}
	if (cl[x] != -1){
		if (testcol(x, cl[x])){
			int mk[N];
			FOR(i,0,n) mk[i] = h[i][cl[x]] == -1 ? 1 : 0;
			FOR(i,0,n) if (mk[i]) h[i][cl[x]] = v[x][i];
			if (dfs(x + 1)) return 1;
			FOR(i,0,n) if (mk[i]) h[i][cl[x]] = -1;
		}
	}
	return 0;
}

//int dfs2(int x, int row, int col, int skip){
//	//printf("%d %d %d %d\n", x, row, col, skip);
//	if (row > n) return 0;
//	if (col > n) return 0;
//	//puts("==============");
//	//prt();
//	//puts("==============");
//	if (x == 2 * n - 1) return 1;
//	if (!testrow(x, row) && !testcol(x, col)){
//		return skip ? 0 : dfs(x + 1, row + 1, col, 1) || dfs(x + 1, row, col + 1, 1);
//	}
//	if (testrow(x, row)){
//		int lo = col, hi;
//		while(h[row][lo] != -1) lo++;
//		for (hi = lo; h[row][hi] == -1; hi++);
//		FOR(i,lo,hi) h[row][i] = v[x][i];
//		if (dfs(x + 1, row + 1, col, skip)) return 1;
//		FOR(i,lo,hi) h[row][i] = -1;
//	}
//	if (testcol(x, col)){
//		int lo = row, hi;
//		while(h[lo][col] != -1) lo++;
//		for (hi = lo; h[hi][col] == -1; hi++);
//		FOR(i,lo,hi) h[i][col] = v[x][i];
//		if (dfs(x + 1, row, col + 1, skip)) return 1;
//		FOR(i,lo,hi) h[i][col] = -1;
//	}
//	return 0;
//}

void prt(){
	FOR(i,0,n){
		FOR(j,0,n) printf("%d ", h[i][j]);
		puts("");
	}
}

int main(){
	int T;
	scanf("%d", &T);
	FOE(cc,1,T){
		scanf("%d", &n);
		FOR(i,0,2 * n - 1) FOR(j,0,n) scanf("%d", &a[i][j]);
		FOR(i,0,v.size()) v.clear();
		v.resize(2 * n - 1);
		FOR(i,0,2 * n - 1) FOR(j,0,n) v[i].PB(a[i][j]);
		sort(v.begin(), v.end());
		int lo = 2500, hi = 1;
		FOR(i,0,n) FOR(j,0,n) h[i][j] = -1;
		FOR(i,0,2 * n - 1) lo = min(lo, a[i][0]);
		FOR(i,0,2 * n - 1) hi = max(hi, a[i][n - 1]);
		int cnt = 0;
		memset(use, 0, sizeof(use)); 
		memset(rw, -1, sizeof(rw)); 
		memset(cl, -1, sizeof(cl)); 
		FOR(i,0,2 * n - 1) if (a[i][0] == lo) cnt++;
		if (cnt == 2){
			FOR(i,0,2 * n - 1) if (a[i][0] == lo){
				use[i] = 1;
				if (h[0][0] == -1) FOR(j,0,n) h[0][j] = a[i][j];
				else FOR(j,0,n) h[j][0] = a[i][j];
			}
			FOR(i,0,2 * n - 1) FOR(j,0,n) if (v[i][0] == h[j][0]) rw[i] = j;
			FOR(i,0,2 * n - 1) FOR(j,0,n) if (v[i][0] == h[0][j]) cl[i] = j;
			//prt();
			dfs(2);
		}
		else{
			FOR(i,0,2 * n - 1) if (a[i][n - 1] == hi){
				use[i] = 1;
				if (h[n - 1][n - 1] == -1) FOR(j,0,n) h[n - 1][j] = a[i][j];
				else FOR(j,0,n) h[j][n - 1] = a[i][j];
			}
			FOR(i,0,2 * n - 1) FOR(j,0,n) if (v[i][n - 1] == h[j][n - 1]) rw[i] = j;
			FOR(i,0,2 * n - 1) FOR(j,0,n) if (v[i][n - 1] == h[n - 1][j]) cl[i] = j;
			//prt();
			int ok = dfs(0 );
		}
			//prt();
		memset(use, 0, sizeof(use));
		vector<int> ans;
		ans.clear();
		FOR(i,0,n){
			vector<int> tv;
			FOR(j,0,n) tv.PB(h[i][j]);
			int ok = 0;
			FOR(j,0,2 * n - 1) if (tv == v[j] && !use[j]){
				use[j] = 1;
				ok = 1;
				break;
			}
			if (!ok){ ans = tv; break; }
		}
		if (ans.size() <= 0){
			FOR(i,0,n){
				vector<int> tv;
				FOR(j,0,n) tv.PB(h[j][i]);
				int ok = 0;
				FOR(j,0,2 * n - 1) if (tv == v[j] && !use[j]){
					use[j] = 1;
					ok = 1;
					break;
				}
				if (!ok){ ans = tv; break; }
			}
		}

		printf("Case #%d: ", cc);
		FOR(i,0,n) printf("%d ", ans[i]); puts("");
	}
	return 0;
}

