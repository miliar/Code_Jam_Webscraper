#include <cstdio>
#include <string>
#include <set>

using namespace std;

const int MAXM = 10;

int ans, cnt, cases;
int N, M;
char ch;
string S[MAXM];
int mark[MAXM];
char buf[50];

int dfs(int v){
	if(v >= M){
		set<string> gg[4];
		for(int i = 0; i < M; ++i){
			string tmp = "";
			for(int j = 0; j < S[i].length(); ++j){
				tmp += S[i][j];
				gg[mark[i]].insert(tmp);
			}
		}
		int tot = 0;
		for(int i = 0; i < N; ++i){
			if(gg[i].size() == 0) return 0;
			tot += (gg[i].size() + 1);
		}
		if(tot > ans){
			ans = tot;
			cnt = 1;
		} else if(tot == ans){
			cnt++;
			cnt = cnt % 1000000007;
		}
		return 0;
	}
	for(int i = 0; i < N; ++i){
		mark[v] = i;
		dfs(v + 1);
	}
}

int main(){
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx){
		scanf("%d%d", &M, &N);
		ans = 0, cnt = 1;
		scanf("%c", &ch);
		for(int i = 0; i < M; ++i){
			scanf("%s", buf);
			string tmp(buf);
			S[i] = tmp;
		}
		dfs(0);
		printf("Case #%d: %d %d\n", xx, ans, cnt);
	}
}
