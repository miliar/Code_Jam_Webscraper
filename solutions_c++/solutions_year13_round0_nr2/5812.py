/*************************************************************************
    > File Name: ..\B\B.cpp
    > Author: hnu0314
    > Mail: hnu0314@126.com 
    > Created Time: 2013/4/13 11:40:22
 ************************************************************************/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>

using namespace std;
typedef long long LL;
const int MAXN = 110; 
const int INF = 110;

int row[MAXN], col[MAXN];
int sz[MAXN];
int q[MAXN][MAXN];

void solve(){
	int n, m;
	scanf("%d%d", &n, &m );
	memset(row, 0, sizeof(row));
	memset(col, 0, sizeof(col));
	memset(sz, 0, sizeof(sz));
	for(int i = 0; i < n; ++i){
		for(int j = 0, a; j < m; ++j){
			
			scanf("%d", &a);
			
			q[a][sz[a]++] = i * m + j;
		}
	}
	
	bool flag(true);
	for(int i = 1; i < MAXN && flag; ++i){
		for(int j = 0; j < sz[i]; ++j){
			int r = q[i][j] / m;
			int c = q[i][j] % m;
			++row[r];
			++col[c];
		}
		for(int j = 0; j < sz[i]; ++j){
			int r = q[i][j] / m;
			int c = q[i][j] % m;
			if(row[r] != m && col[c] != n)  flag = false;
		}
	}
	printf("%s\n", flag ? "YES" : "NO");
}

int main(){
	
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-0.out", "w", stdout);
	int test, cas(1);
	scanf("%d", &test);
	while(test--){
		printf("Case #%d: ",cas++);
		solve();

	}

	return 0;
}
