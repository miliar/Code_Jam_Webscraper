#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <time.h>
using namespace std;
#pragma comment(linker, "/STACK:200000000")

#define mp make_pair
#define pb push_back 
#define ll long long
#define sz(x) (int)(x).size()

string matrix[111];

int minrow[111], maxrow[111];
int mincol[111], maxcol[111];

int main()
{
	freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    //freopen("a.in","rt",stdin);
    //freopen("a.out","wt",stdout);
	
	int T;
	scanf("%d", &T);

	for(int test = 1; test <= T; test++) {
		int R, C;
		scanf("%d %d", &R, &C);
		for(int i = 0; i < R; i++) cin >> matrix[i];
		for(int i = 0; i < R; i++) minrow[i] = 1e9, maxrow[i] = -1e9;
		for(int i = 0; i < C; i++) mincol[i] = 1e9, maxcol[i] = -1e9;
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				if(matrix[i][j] != '.') minrow[i] = min(minrow[i], j);
				if(matrix[i][j] != '.') mincol[j] = min(mincol[j], i);
				if(matrix[i][j] != '.') maxrow[i] = max(maxrow[i], j);
				if(matrix[i][j] != '.') maxcol[j] = max(maxcol[j], i);
			}
		}
		int cnt = 0;
		bool bad = false;
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				if(matrix[i][j] == '^' && mincol[j] == i || matrix[i][j] == 'v' && maxcol[j] == i || matrix[i][j] == '<' && minrow[i] == j || matrix[i][j] == '>' && maxrow[i] == j) { // надо повернуть
					if(mincol[j] < i || maxcol[j] > i || minrow[i] < j || maxrow[i] > j) {
						cnt++;
					}
					else bad = true;
				}
			}
		}
		if(bad) printf("Case #%d: IMPOSSIBLE\n", test);
		else printf("Case #%d: %d\n", test, cnt);
	}

    return 0;
}