#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<climits>
#include<algorithm>
#include<map>
using namespace std;

#define N 210
int a[N][N];
int row[N], col[N];
int n, m;

int getmax(int x, int y) { return x>y?x:y; }

void conduct() {
	int i, j;
	scanf("%d%d", &n, &m);
	for (i=0; i<n; ++i) for (j=0; j<m; ++j) scanf("%d", &a[i][j]);
	for (i=0; i<n; ++i) for (row[i]=j=0; j<m; ++j) row[i]=getmax(row[i], a[i][j]);
	for (j=0; j<m; ++j) for (col[j]=i=0; i<n; ++i) col[j]=getmax(col[j], a[i][j]);
	for (i=0; i<n; ++i) for (j=0; j<m; ++j) if (a[i][j]<row[i] && a[i][j]<col[j]) {
		printf("NO\n"); return;
	}
	printf("YES\n");
}

int main() {
	int time; scanf("%d", &time);
	for (int i=1; i<=time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	} return 0;
}
