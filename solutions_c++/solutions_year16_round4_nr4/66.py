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

int n, a[33];
char s[33][33];
bool mat[33][33];

bool vis0[33], vis1[33];

bool ok(int d){
	if(d == n) return 1;
	bool hascnd = 0;
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			bool bad = 0;
			if(!vis0[i] && !vis1[j] && mat[i][j]){
				hascnd = 1;
				vis0[i] = vis1[j] = 1;
				if(!ok(d+1)) bad = 1;
				vis0[i] = vis1[j] = 0;
			}
			if(bad) return 0;
		}
	}
	return hascnd;
}

int bktk(int x, int y){
	if(x == n){
		if(ok(0)) return 0;
		return 1e9;
	}
	if(y == n) return bktk(x+1, 0);
	if(s[x][y] == '1'){
		mat[x][y] = 1;
		return bktk(x, y+1);
	}
	else{
		mat[x][y] = 0;
		int ret = bktk(x, y+1);
		mat[x][y] = 1;
		ret = min(ret, bktk(x, y+1) + 1);
		return ret;
	}
}
int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		cin >> n;
		for(int i=0; i<n; i++) cin >> s[i], a[i] = i;
		cout << bktk(0, 0) << endl;
	}
}