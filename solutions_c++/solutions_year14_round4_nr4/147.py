#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#define maxn 1010
#define mod 1000000007
using namespace std;


set<string> ss[10];

int best, count1, n, m;
string a[100];
int ch[100];

int check(){
	int result = 0;
	for(int i = 1; i <= n; ++i) ss[i].clear();
	for(int i = 1; i <= m; ++i) 
		for(int j = 1; j <= a[i].size(); ++j) ss[ch[i]].insert(a[i].substr(0, j));
	for(int i = 1; i <= n; ++i) {
		result += ss[i].size();
		if(ss[i].size() > 0) ++result;
	}
	return result;
}

void dfs(int k){
	if(k > m){
		int tmp = check();
		if(tmp > best){
			best = tmp;
			count1 = 1;
		} else if(tmp == best) ++count1;
		return;
	}
	for(int i = 1; i <= n; ++i){
		ch[k] = i;
		dfs(k + 1);
	}
}

void solve(){
	best = -1;
	count1 = 0;
	scanf("%d%d", &m, &n);
	for(int i = 1; i <= m; ++i) cin>>a[i];
	dfs(1);
	printf("%d %d\n", best, count1);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}