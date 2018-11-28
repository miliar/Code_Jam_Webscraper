#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int t;
int grid[100][100], maxr[100], maxc[100];

main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    scanf("%d", &t);
    for(int test=1; test<=t; test++) {
	int r, c;
	scanf("%d %d", &r, &c);
	for(int i=0;i<r;i++) for(int j=0;j<c;j++) scanf("%d", &grid[i][j]);
	for(int i=0;i<r;i++) {
	    maxr[i]=0;
	    for(int j=0;j<c;j++) maxr[i] = max(maxr[i], grid[i][j]);
	    }
	for(int j=0;j<c;j++) {
	    maxc[j]=0;
	    for(int i=0;i<r;i++) maxc[j] = max(maxc[j], grid[i][j]);
	    }
	bool ok=true;
	for(int i=0;i<r;i++) for(int j=0;j<c;j++) 
	    ok &= grid[i][j]==maxr[i] || grid[i][j]==maxc[j];
	printf("Case #%d: %s\n", test, ok ? "YES" : "NO");
	}
    }










