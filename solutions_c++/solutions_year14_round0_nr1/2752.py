#include <set>
#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <limits.h>
#include <string.h>
#include <string>
#include <algorithm>
#define MID(x,y) ( ( x + y ) >> 1 )
#define L(x) ( x << 1 )
#define R(x) ( x << 1 | 1 )
#define FOR(i,s,t) for(int i=(s); i<(t); i++)
#define FORD(i,s,t) for(int i=(s-1); i>=t; i--)
#define BUG puts("here!!!")
#define STOP system("pause")
#define file_r(x) freopen(x, "r", stdin)
#define file_w(x) freopen(x, "w", stdout)

using namespace std;

int a[4][4], b[4][4];
int f[100];

void read(int a[][4]) {
	for(int i=0; i<4; i++)
		for(int k=0; k<4; k++)
			cin >> a[i][k];
}

int solve(int r1, int r2) {
	memset(f, 0, sizeof(f));
	for(int i=0; i<4; i++) {
		f[a[r1-1][i]]++;
		f[b[r2-1][i]]++;
	}
	int cnt = 0;
	int v = -1;
	for(int i=0; i<17; i++)
		if( f[i] == 2 ) {
			cnt++;
			v = i;
		}
	if(cnt > 1)
		return 100;
	if(cnt == 0 )
		return 0;
	return v;
}
int main() {
	int ncases;
	int r1, r2;
	
	file_r("in.txt");
	file_w("out.txt");
	cin >> ncases;
	
	int ncase = 1;
	while( ncases-- ) {
		cin >> r1;
		read(a);
		cin >> r2;
		read(b);
		int ans = solve(r1, r2);
		cout << "Case #" << ncase++ << ": ";
		if( ans == 0 )
			cout << "Volunteer cheated!" << endl;
		else if( ans == 100 )
			cout << "Bad magician!" << endl;
		else cout << ans << endl;
	}
	return 0;
}

