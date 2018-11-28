//------------------------------------------------------------------------------
//  Problem : 
//  User    : 
//  Date    : 
//------------------------------------------------------------------------------


#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

char s[11111];
int mtx[10][10];
string p[] = {"1", "i", "j", "k", "-1", "-i", "-j", "-k"};

bool check(int now, int X) {
	switch(now) {
		// 1
		case 0: {
			return false;
		}
		// -1
		case 4: {
			return X&1;
		}
		// i, j, k, -i, -j, -k
		default: {
			return (X&3) == 2;
		}
	}
}

void solu(int x) {
	printf("Case #%d: YES\n", x);
}

void nosl(int x) {
	printf("Case #%d: NO\n", x);
}

int change(char x) {
	switch(x) {
		case 'i': {
			return 1;
		}
		case 'j': {
			return 2;
		}
		case 'k': {
			return 3;
		}
	}
}
			

void work(int testcase) {
	int N, X;
	cin >> N >> X;
	scanf("%s", s);
	int now = 0;
	for(int i = 0; i < N; ++i) {
		int x = change(s[i]);
		now = mtx[now][x];
	}
	if(!check(now, X)) {
		nosl(testcase);
		return;
	}
	now = 0;
	int ri, pi;
	ri = pi = -1;
	for(int i = 0; i < 4; ++i) {
		for(int j = 0; j < N; ++j) {
			int x = change(s[j]);
			now = mtx[now][x];
			if(now == 1) {
				pi = j;
				ri = i;
				break;
			}
		}
		if(ri != -1) {
			break;
		}
	}
	if(ri == -1) {
		nosl(testcase);
		return;
	}
	now = 0;
	for(int i = pi+1; i < N; ++i) {
		now = mtx[now][change(s[i])];
		if(now == 2) {
			solu(testcase);
			return;
		}
	}
	int rj, pj;
	rj = pj = -1;
	for(int i = 0; i < 4; ++i) {
		for(int j = 0; j < N; ++j) {
			now = mtx[now][change(s[j])];
			if(now == 2) {
				pj = j, rj = i;
				break;
			}
		}
		if(rj != -1) {
			break;
		}
	}
	if(rj == -1 || ri+rj+2 > X) {
		nosl(testcase);
		return;
	}
	solu(testcase);
}

int mns(int x) {
	return x<4? x+4: x-4;
}
	
void make_matrix() {
	for(int i = 0; i < 4; i++) {
		mtx[0][i] = mtx[i][0] = i;
		if(i > 0) {
			mtx[i][i] = 4;
		}
	}
	mtx[1][2] = 3, mtx[1][3] = 6, mtx[2][1] = 7, mtx[2][3] = 1, mtx[3][1] = 2, mtx[3][2] = 5;
	for(int i = 0; i < 4; ++i)
	for(int j = 4; j < 8; ++j) {
		mtx[i][j] = mns(mtx[i][j-4]);
		mtx[j][i] = mns(mtx[j-4][i]);
		mtx[i+4][j] = mtx[i][j-4];
	}
}
	
	
	
		

int main( int argc , char *argv[] )
{
	freopen("C1.in", "r", stdin);
	freopen("C1.out", "w", stdout);
	make_matrix();
	int T;
	scanf("%d", &T);
	for(int testcase = 1; testcase <= T; ++testcase) {
		work(testcase);
	}
		
	return 0;
}
