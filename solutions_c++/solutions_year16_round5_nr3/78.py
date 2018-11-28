#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <numeric>
#include <deque>
#include <utility>
#include <bitset>
#include <iostream>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;

int n, s;
int x[1005], y[1005], z[1005], vx[1005], vy[1005], vz[1005];

bool vis[1005];

double dist(int a, int b){
	return hypot(hypot(x[b] - x[a], y[b] - y[a]), z[b] - z[a]);
}

bool dfs(int x, double l){
	if(x == 1) return 1;
	if(vis[x]) return 0;
	vis[x] = 1;
	for(int i=0; i<n; i++){
		if(dist(x, i) <= l && dfs(i, l)){
			return 1;
		}
	}
	return 0;
}

bool ok(double x){
	memset(vis, 0, sizeof(vis));
	return dfs(0, x);
}

double solve(){
	cin >> n >> s;
	for(int i=0; i<n; i++){
		cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
	}
	double s = 0, e = 1e4;
	for(int i=0; i<50; i++){
		double m = (s+e)/2;
		if(ok(m)) e = m;
		else s = m;
	}
	return s;
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: %.10f\n",i, solve());
	}
}