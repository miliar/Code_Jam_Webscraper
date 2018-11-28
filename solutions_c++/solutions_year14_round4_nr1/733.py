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
using namespace std;
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FOE(i,a,b) for (int i=(a);i<=(b);i++)
#define INF (1 << 30)
#define EPS (1e-9)
#define REP(i,n) FOR(i,0,n)
#define LL long long
#define N 100100
int n, m;
int T;
int a[N], b[N];
int main(){
	scanf("%d", &T);
	FOE(cc,1,T){
		scanf("%d%d", &n, &m);
		int ans = n;
		FOR(i,0,n) scanf("%d", a + i);
		sort(a, a + n);
		int tmp = n - 1;
		FOR(i,0,n){
			while(tmp > i && a[i] + a[tmp] > m) tmp--;
			if (tmp > i) { ans--; tmp--; }
			else break;
		}
		printf("Case #%d: ", cc);
		printf("%d\n", ans);
	}
	return 0;
}

