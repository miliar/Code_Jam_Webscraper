#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 20000;

int n;
int id[N];
int ans;
vector<string> v[N];
vector<int> p[N];
vector<string> all;

char ch;
bool a[N], b[N];

int calc(){
	for(int i = 0; i < all.size(); i++) a[i] = b[i] = 0;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < p[i].size(); j++){
			if (id[i] == 0) a[p[i][j]] = true;
			else b[p[i][j]] = true;
		}
	}
	int ret = 0;
	for(int i = 0; i < all.size(); i++) if (a[i] && b[i]) ret++;
	return ret;
}

void dfs(int lev){
	if (lev == n){
		ans = min(ans, calc());
		return;
	}
	id[lev] = 0;
	dfs(lev + 1);
	id[lev] = 1;
	dfs(lev + 1);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++){
		all.clear();
		printf("Case #%d: ", cas);
		scanf("%d", &n);
		while((ch == getchar()) && ch != '\n');
		for(int i = 0; i < n; i++){
			v[i].clear();
			string s = "";
			while(true){
				s = "";
				while((ch = getchar()) && ch != '\n' && ch != ' ') s = s + ch;
				v[i].push_back(s);
				all.push_back(s);
				if (ch == '\n') break;
			}
		}
		sort(all.begin(), all.end());
		all.erase(unique(all.begin(), all.end()), all.end());
		for(int i = 0; i < n; i++){
			p[i].clear();
			for(int j = 0; j < v[i].size(); j++){
				p[i].push_back(lower_bound(all.begin(), all.end(), v[i][j]) - all.begin());
			}
		}
		ans = 0x3f3f3f3f;
		id[0] = 0;
		id[1] = 1;
		dfs(2);
		printf("%d\n", ans);
	}
}
