#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define rep(i,s,t) for(int i=int(s); i<int(t); i++)
#define mst(A,k) memset(A,k,sizeof(A))

int n;
int R, S, P;
int order[15];

int solve(int l, int r, int *a) {
	if(l == r) return a[l];
	int mid = l + r >> 1;
	int x = solve(l, mid, a);
	int y = solve(mid + 1, r, a);
	if(x == -1 || y == -1 || x == y) return -1;
	if((x + 1) % 3 == y) return x;
	else return y;
}
bool dfs(int k, int r, int s, int p) {
	if(!r && !s && !p) {
		return solve(0, k - 1, order) != -1;
	}
	if(p) {
		order[k] = 2;
		if(dfs(k + 1, r, s, p - 1)) return true;
	}
	if(r) {
		order[k] = 0;
		if(dfs(k + 1, r - 1, s, p)) return true;
	}
	if(s) {
		order[k] = 1;
		if(dfs(k + 1, r, s - 1, p)) return true;
	}
	return false;
}
int main() {
	freopen("A-small-attempt1.in","r",stdin); 
	freopen("ans.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++) {
		scanf("%d%d%d%d", &n, &R, &P, &S);
		bool flag = dfs(0, R, S, P);
		printf("Case #%d: ", cas);
		if(!flag) printf("IMPOSSIBLE\n");
		else {
			for(int i = 0; i < (1 << n); i++) {
				if(order[i] == 0) printf("R");
				else if(order[i] == 1) printf("S");
				else printf("P");
			}
			printf("\n");
		}
	}
	return 0;
}

