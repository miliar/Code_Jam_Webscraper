#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#define Rep(i,a) for(int i = 0; i < (a); i++)
#define rep(i,a,b) for(int i = (a); i <= (b); i++)//(a)!
#define dep(i,a,b) for(int i = (a); i >= (b); i--)
#define ab(a) ((a) > 0 ? (a) : -(a))
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back(a)
using namespace std;
typedef long long LL;
typedef unsigned long long uLL;
bool c[1010];
int a[33], p[33], f[33][1010], cnt = 0;

int pw(int a, int b, int c){ int w = 1; for(; b; b >>= 1, a = a * a % c) if (b & 1) w = w * a % c; return w;}

void dfs(int x){
	if (cnt == 500) return;
	if (x > 32){
		rep(i,2,10){
			p[i] = 0;
			rep(j,11,1000) if (c[j]){
				if (f[i][j] == 0) { p[i] = j; break; }
			}
			if (!p[i]) return;
		}
		cnt++;
		rep(i,1,32) printf("%d",a[i]); printf(" ");
		rep(i,2,10) printf("%d ",p[i]);
		printf("\n");
	}else{
		if (x > 1 && x < 32){
			a[x] = 0;
			rep(i,2,10) rep(j,11,1000) if (c[j]) f[i][j] = f[i][j] * i % j;
			dfs(x + 1);
			rep(i,2,10) rep(j,11,1000) if (c[j]) f[i][j] = f[i][j] * pw(i, j - 2, j) % j;
		}

		a[x] = 1;
		rep(i,2,10) rep(j,11,1000) if (c[j]) f[i][j] = (f[i][j] * i + 1) % j;
		dfs(x + 1);
		rep(i,2,10) rep(j,11,1000) if (c[j]) f[i][j] = (f[i][j] - 1) * pw(i, j - 2, j) % j;
	}
}
int main(){
	rep(i,11,1000){
		c[i] = true;
		rep(j,2,i-1) if (i % j == 0) c[i] = false;
	}
	dfs(1);
	return 0;
}