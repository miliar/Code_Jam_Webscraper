#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<bitset>
using namespace std;
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define CLR(a) memset(a, 0, sizeof(a))
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FOE(i,a,b) for (int i=(a);i<=(b);i++)
#define FIT(i,a) for (__typeof__((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define TRA(i,a,b) for (int i = (a); i != -1; i = (b)[i])
#define INF (1 << 30)
#define EPS (1e-9)
#define REP(i,n) FOR(i,0,n)
#define LL long long
int n, m;
int p, r, s;
char a[200];
int win[300][300];
string ans[13][13][13];
int ok(int x){
//	printf("%d %c\n", x, a[x]);
	if (x >= n)
		return 1;
	if (!ok(2 * x) || !ok(2 * x + 1))
		return 0;
	if (a[2 * x] == a[2 * x + 1])
		return 0;
	if (win[a[2 * x]][a[2 * x + 1]])
		a[x] = a[2 * x];
	else
		a[x] = a[2 * x + 1];
	return 1;
}

void prt(){
	a[2 * n] = 0;
//			puts(a + 1);
	ans[p][r][s] = a + n;
//			puts(a + 1);
//	printf("%s\n", ans[p][r][s].c_str());
}


int find(int p, int r, int s){
	if (!p && !r && !s){
		if (ok(1)){
		//	puts(a + 1);
			prt();
			return 1;
		}
		return 0;
	}
	if (p){
		a[m++] = 'P';
		if (find(p - 1, r, s))
			return 1;
		m--;
	}
	if (r){
		a[m++] = 'R';
		if (find(p, r - 1, s))
			return 1;
		m--;
	}
	if (s){
		a[m++] = 'S';
		if (find(p, r, s - 1))
			return 1;
		m--;
	}
	return 0;
}

int main(){
	int T;
	win['P']['R'] = 1;
	win['R']['S'] = 1;
	win['S']['P'] = 1;
	scanf("%d", &T);
	FOR(i,0,13) FOR(j,0,13) FOR(k,0,13) ans[i][j][k] = "";
	FOE(cc,1,T){
		scanf("%d%d%d%d", &n, &r, &p, &s);
		n = 1 << n;
		printf("Case #%d: ", cc);
		m = n;
		if (ans[p][r][s] != ""){
			printf("%s\n", ans[p][r][s].c_str());
		}
		else {
			int tmp = find(p, r, s);
			//printf("ok %d\n", tmp);
			if (!tmp)
				ans[p][r][s] = "IMPOSSIBLE";
			printf("%s\n", ans[p][r][s].c_str());
		}
	}
	return 0;
}

