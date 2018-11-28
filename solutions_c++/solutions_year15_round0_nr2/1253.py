#include <cstdio>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <queue>
#define INF 100000
using namespace std;

int n;
vector<int> a;
map<vector<int>, bool> Map;
int ans = INF;

void dfs(int level, vector<int> v){
	sort(v.begin(), v.end());
	if (Map[v]) return;
	Map[v] = 1;
	if (v[v.size() - 1] <= 3){
		ans = min(ans, level + v[v.size() - 1]);
		return;
	}
	int i = v.size() - 1;
	for (int j = 1; j <= v[i] / 2; j++){
		vector<int> V = v;
		V.pop_back();
		V.push_back(j);
		V.push_back(v[i] - j);
		dfs(level + 1, V);
	}
	for (int i = 0; i < v.size(); i++) v[i]--;
	dfs(level + 1, v);
}

void solve(){
	Map.clear();
	a.clear();
	scanf("%d", &n);
	for (int i = 0; i < n; i++){
		int w;
		scanf("%d", &w);
		a.push_back(w);
	}
	ans = INF;
	dfs(0, a);
	printf("%d\n", ans);
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
