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
#define N 2000
int n, m;
char s[N];
int main(){
	int T;
	scanf("%d", &T);
	FOE(cc,1,T){
		printf("Case #%d: ", cc);
		scanf("%d%s", &n, s);
		int tmp = 0, ans = 0;
		FOE(i,0,n){
			if (tmp < i) ans += i - tmp;
			tmp = max(tmp, i);
			tmp += s[i] - '0';
		}
		printf("%d\n", ans);
	}
	return 0;
}

