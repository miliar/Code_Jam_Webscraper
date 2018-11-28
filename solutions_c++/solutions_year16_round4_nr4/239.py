#include<iostream>
#include<cstdio>
#include<cstring>
#define rep(i, l, r) for(int i = l; i <= r; ++i)
using namespace std;
const int maxn = 10;
int n, last;
bool fail;
bool use[maxn];
bool vis[maxn][maxn], f[maxn][maxn];
bool bit(int state, int x){
	return (state >> x) & 1;
}
void dfs(int x){
	if(x == last) {
		dfs(x + 1);
		return ;
	}
	if(x == n + 1){
		bool ok = 0;
		
		rep(i, 1, n)
			if(f[last][i] && !use[i]) 
				ok = 1;rep(i, 1, n)
		/*	rep(j, 1, n)
				printf("f[%d][%d] = %d\n", i, j, f[i][j]);
		rep(i, 1, n)
			printf("use[%d] = %d\n", i, use[i]);
		printf("last = %d ok = %d\n", last,ok);
		*/if(!ok) fail = 1;
		return ;
	}
	if(fail) return ;
	bool ok = 0;
	rep(i, 1, n)
		if(f[x][i] && !use[i]){
		//	printf(" dfs x = %d i = %d\n", x, i);
			use[i] = 1;
			ok = 1;
			dfs(x  + 1);
			use[i] = 0;
		}
	if(!ok) fail = 1;
}
int main(){
	
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	rep(cas, 1, T){
		cin >> n;
		int ans = n * n;
		static char s[101];
		rep(i, 1, n){
			scanf("%s", s + 1);
			rep(j, 1, n)
				vis[i][j] = s[j] == '1' ? 1 : 0;
		}	
		for(int state = 0; state < (1 << n * n); ++state){
			bool flag = 0;
			int cnt = 0;
			rep(i, 1, n)	
				rep(j, 1, n)
					if(bit(state, (i - 1) * n + j - 1) && !vis[i][j])
						++cnt;
			//printf("state = %d cnt = %d\n", state, cnt);
			if(cnt > ans) continue;
			rep(i, 1, n)
				rep(j, 1, n)
					if(vis[i][j]){
						if(!bit(state, (i - 1) * n + j - 1)){
							flag = 1;
							break;
						}
						else f[i][j] = 1;
					}
					else if(bit(state, (i - 1) * n + j - 1))
						f[i][j] = 1;
					else f[i][j] = 0;
			if(flag) continue;
		//	printf("state = %d cnt = %d\n", state, cnt);
			fail = 0;
			rep(i, 1, n){
				last = i;
				dfs(1);
		//		printf("i = %d fail = %d\n", i, fail);
				if(fail) break;
			}
			if(fail) continue;
		//	printf("state = %d cnt = %d\n", state, cnt);
			if(cnt < ans) ans = cnt;
		}
		printf("Case #%d: %d\n",  cas,ans);
	}
	return 0;
} 
/*
1
2
11
10
*/
