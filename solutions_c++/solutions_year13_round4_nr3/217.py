#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pb push_back
#define mp make_pair
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
using namespace std;

int n, a[2222], b[2222], h[2222], f[2222], v[2222], g[2222];
bool flag;

void check(){
	for (int i = n; i; i--){
		int now = 1;
		for (int j = i + 1; j <= n; j++)
			if (v[j] < v[i])
				now = max(now, b[j] + 1);
		if (now != b[i]) return;
	}
	for (int i = 1; i <= n; i++)
		printf(" %d", v[i]);
	cout << endl;
	flag = 0;
}

void calc(int dep){
	if (dep == n + 1) 
		check();
	else
		for (int i = max(f[ a[dep] - 1 ], 1); i <= (f[ a[dep] ] == 0 ? n : f[ a[dep] ] - 1) && flag; i++)
			if (!h[i]){
				h[i] = 1;
				v[dep] = i;
				int tmp = f[ a[dep] ];
				if (!f[ a[dep] ])
					f[ a[dep] ] = i;
				else
					f[ a[dep] ] = min(f[ a[dep] ], i);
				calc(dep + 1);
				f[ a[dep] ] = tmp;
				h[i] = 0;
			}
}

void solve(){
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
		scanf("%d", &a[i]);
	for (int j = 1; j <= n; j++)
		scanf("%d", &b[j]);
	flag = 1;
	calc(1);
}

int main(){
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; i++){
		printf("Case #%d:", i);
		solve();
	}
				
	return 0;
}
