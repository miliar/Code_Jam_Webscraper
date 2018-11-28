#include <cstdio>
#include <cstring>
#include <iostream>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define MEM(A) memset(A,0,sizeof(A))
using namespace std ;
int n, m, a[100], trie[10][100][200], len[100], ansx, ansy;
char s[10][100];
void dfs(int dep);
int calc();
int main(){
    freopen("D.in", "r", stdin); freopen("D.out","w",stdout);
    int Test ; cin >> Test ;
    fo(_,1,Test) {
        scanf("%d %d", &n, &m);
        fo(j,1,n) scanf("%s", s[j]);
        ansx = -1; dfs(1); printf("Case #%d: %d %d\n", _, ansx, ansy);
	}
}
int calc() {
	int ans = 0; MEM(trie); MEM(len);
	fo(i,1,n){
		int k = a[i], cur = 0;
		if (len[k] == -1) len[k] = 0, ans ++;
		for (int j = 0; j < strlen(s[i]); ++j){
			if (trie[k][cur][s[i][j]] == -1) trie[k][cur][s[i][j]] = ++len[k], ++ans;
			cur = trie[k][cur][s[i][j]];
		}
	}
	return ans;
}
void dfs(int dep){
	if (dep > n){
		int ret = calc();
		if      (ret >  ansx) ansx = ret, ansy = 1;
		else if (ret == ansx) ansy ++ ;
		return;
	}
	fo(i,1,m) a[dep] = i, dfs(dep + 1);
}
