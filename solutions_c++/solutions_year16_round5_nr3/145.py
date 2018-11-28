#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

double a[2000][7], d[2000][2000];

double sqr(double x){
	return x * x;
}

int view[2000];

int n;
double s;
double now;
void dfs(int x){
	view[x] = 1;
	for(int i = 0; i < n; i++){
		if(d[i][x] < now && !view[i]){
			dfs(i);
		}
	}
}

int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; cc++){
		scanf("%d%lf", &n, &s);
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < 6; ++j){
				scanf("%lf", a[i] + j);
			}
		}
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < n; ++j){
				d[i][j] = sqrt(sqr(a[i][0] - a[j][0]) + sqr(a[i][1] - a[j][1]) + sqr(a[i][2] - a[j][2]));
			}
		}
		double l = 0, h = d[0][1];
		while(h - l > 1e-5){
			double mid = (l + h) / 2;
			now = mid;
			memset(view, 0, sizeof(view));
			dfs(0);
			if(view[1]){
				h = mid;
			} else l = mid;
		}
		printf("Case #%d: %.10f\n", cc, l);
	}
	return 0;
}

