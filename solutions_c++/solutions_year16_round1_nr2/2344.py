#ifndef _HEAD_H_
#define _HEAD_H_
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>

#define rep(i, n) for (int i=0; i<(n); ++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define repd(i, a, b) for (int i=(a); i>=(b); --i)
#define sz(a) ((int)(a).size())
#define SQR(x) ((x)*(x))

using namespace std;

template <class T> void checkmin(T &a, T b){ if (b<a) a=b; }
#endif
#define N 50

int row;
vector<vector<int> > a;
int n;
int mat[N+10][N+10];
bool type[N*2+10];

int debug(){
	for (int i=0; i<n; ++i){
		for (int j=0; j<n; ++j){
			cout<<mat[i][j]<<' ';
		}
		cout<<endl;
	}
	cout<<endl;
}

bool dfs(int x){
	if (row==n){
		row = 0;
		for (int i=0; i<2*n-1; ++i) if (type[i]==1){

			for (int j=0; j<n; ++j)
				mat[row][j] = a[i][j];
			++row;
		}

		//debug();

		int col = 0;
		int error = 0;
		int errorCol = 0;
		
		for (int i=0; i<2*n-1; ++i) if (type[i]==0){

			bool flag = true;;
			for (int j=0; j<n; ++j)
				if (mat[j][col] != a[i][j]){
					flag =false;
					break;
				}

			if (!flag){
				errorCol = col;
				if (++error>1) break;
				--i;
			}
			++col;
		}


		if (error <= 1){
			if (error == 0)
				errorCol = col;

			for (int j=0; j<n; ++j){
				if (j) putchar(' ');
				printf("%d", mat[j][errorCol]);
			}
			puts("");
			return true;
		}
		return false;

	}


	if (x >= 2*n-1) return false;

	++row;
	type[x] = 1;
	if (dfs(x+1)) 
		return true;
	type[x] = 0;
	--row;

	if (dfs(x+1)) 
		return true;

	return false;
}

void solve(){
	row = 0;
	memset(mat, 0, sizeof(mat));
	memset(type, 0, sizeof(type));
	dfs(0);
}


int main(){
	int ts;
	scanf("%d", &ts);

	for (int te=1; te<=ts; ++te){
		scanf("%d", &n);

		a.clear();
		for (int i=0; i<2*n-1; ++i){
			vector<int> row;
			for (int j=0; j<n; ++j){
				int k;
				scanf("%d", &k);
				row.push_back(k);
			}
			a.push_back(row);
		}
		sort(a.begin(), a.end());

		printf("Case #%d: ", te);
		solve();
	}
	return 0;
}
