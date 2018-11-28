#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <iostream>

#define ln printf("\n")
typedef long long ll;

#define fr(a,b,c) for(int a = b; a < c; a++)
#define rep(a,b) fr(a,0,b)

#define dbg(x) cerr << #x << " = " << x << endl
#define db dbg
#define _  << " , " <<

using namespace std;

const double eps = 1e-8;
int n, m;

int cn = 1;

int r[111][111];

bool read(){
	scanf("%d%d", &n, &m);
	
	rep(i,n) rep(j,m) scanf("%d", &r[i][j]);
	
	return true;
}

int bigl[111];
int bigc[111];

int r2[111][111];

void process(){
	printf("Case #%d: ", cn++);
	
	memset(bigl, -1, sizeof bigl);
	memset(bigc, -1, sizeof bigc);
	
	rep(i,n){
		rep(j,m) bigl[i] = max(bigl[i], r[i][j]);
	}
	
	rep(j,m){
		rep(i,n) bigc[j] = max(bigc[j], r[i][j]);
	}
	
	rep(i,n) rep(j,m) r2[i][j] = 100;
	
	for(int i = 100; i >= 0; i--){
		rep(j,n){
			if(bigl[j] == i){
				rep(k,m) r2[j][k] = i;
			}
		}
		rep(j,m){
			if(bigc[j] == i){
				rep(k,n) r2[k][j] = i;
			}
		}
	}
	
	rep(i,n) rep(j,m) if(r[i][j] != r2[i][j]){
		printf("NO\n");
		return;
	}
	
	printf("YES\n");
	
}

int main(){	
	int t = -1;
	scanf("%d", &t);
	
	while(t-- && read()){		
		process();
	}	
	
	return 0;
}
