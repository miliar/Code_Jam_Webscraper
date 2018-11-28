#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <functional>
#include <numeric>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <set>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;

int a[105], r, c;
bool ok[105][105], ans[105][105], fnd;
int dx[4] = {1, 0, -1, 0}, dy[4] = {0, -1, 0, 1};

pi simulate(pi x){
	int dir = 0;
	if(x.first <= 0){
		x.first++;
		dir = 0;
	}
	if(x.first > r){
		x.first--;
		dir = 2;
	}
	if(x.second <= 0){
		x.second++;
		dir = 3;
	}
	if(x.second > c){
		x.second--;
		dir = 1;
	}
	while(x.first <= r && x.first >= 1 && x.second <= c && x.second >= 1){
		if(!ok[x.first-1][x.second-1]) dir = 3 - dir;
		else dir = (dir ^ 1);
		x.first += dx[dir];
		x.second += dy[dir];
	}
	return pi(x.first, x.second);
}

pi get(int x){
	if(x <= c) return pi(0, x);
	if(x <= r + c) return pi(x-c, c+1);
	if(x <= r + c + c) return pi(r+1, r+c+c+1-x);
	return pi(2*r+2*c-x+1, 0);
}

void bktk(int x, int y){
	if(x == r){
		bool ok = 1;
		for(int i=0; i<2*r+2*c; i+=2){
			if(simulate(get(a[i])) != get(a[i+1])){
				ok = 0;
				break;
			}
		}
		if(ok){
			for(int i=0; i<r; i++){
				for(int j=0; j<c; j++){
					ans[i][j] = ::ok[i][j];
				}
			}
			fnd = 1;
		}
		return;
	}
	if(y == c){
		bktk(x+1, 0);
		return;
	}
	if(fnd) return;
	ok[x][y] = 0;
	bktk(x, y+1);
	ok[x][y] = 1;
	bktk(x, y+1);
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d:\n", i);
		cin >> r >> c;
		for(int j=0; j<2*r+2*c; j++){
			cin >> a[j];
		}
		fnd = 0;
		bktk(0, 0);
		if(!fnd) puts("IMPOSSIBLE");
		else{
			for(int j=0; j<r; j++){
				for(int k=0; k<c; k++){
					if(ans[j][k]) putchar('/');
					else printf("\\");
				}
				puts("");
			}
		}
	}
}