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
int a[N];
int main(){
	int T;
	scanf("%d", &T);
	FOE(cc,1,T){
		printf("Case #%d: ", cc);
		scanf("%d", &n);
		FOR(i,0,n) scanf("%d", a + i);
		int ans = N;
		FOE(i,1,1000){
			int tmp = 0;
			FOR(j,0,n){
				int re = max(a[j] - i, 0);
				tmp += re / i + !!(re % i);
			}
			ans = min(ans, i + tmp);
		}
		printf("%d\n", ans);
	}
	return 0;
}

