#include "iostream"
#include "cstring"
#include "cstdio"
#include "string"
using namespace std;
int sz[10];
int trie[10][1000][26];
void insert(int id, string s)
{
	int len = s.size();
	int r = 0;
	for(int i = 0; i < len; ++ i){
		int idx = s[i] - 'A';
		if(trie[id][r][idx]){
			r = trie[id][r][idx];
		}else{
			trie[id][r][idx] = ++sz[id];
			r = trie[id][r][idx];
		}
	}
}
string a[10];
int T, n, m;
int val[10], sum[10];
int ans, num;
void dfs(int now){
	if(now == n){
		memset(sum, 0, sizeof(sum));
		for(int i = 0; i < n; ++ i){
			sum[val[i]] ++;
		}
		for(int i = 0; i < m; ++ i){
			if(sum[i] == 0) return ;
		}
		memset(trie, 0, sizeof(trie));
		memset(sz, 0, sizeof(sz));
		for(int i = 0; i < n; ++ i){
			insert(val[i], a[i]);
		}
		int tans = 0;
		for(int  i = 0; i < m; ++ i){
			tans += sz[i];
		}
		if(tans == ans){
			num ++;
		}else if(tans > ans){
			ans = tans;
			num = 1;
		}
		return ;
	}else{
		for(int i = 0; i < m; ++ i){
			val[now] = i;
			dfs(now + 1);
		}
	}
}
int main(void)
{
	scanf("%d", &T);
	int g = 0;
	while(T --){
		scanf("%d %d", &n, &m);		
		for(int i = 0; i < n; ++ i){
			cin >> a[i];
		}
		ans = 0, num = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", ++ g, ans + m, num);
	}
	return 0;
}