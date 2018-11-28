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
int n, m;

char s[200];
int a[200];
int main(){
	int T;
	scanf("%d", &T);
	FOE(cc,1,T){
		int ans = 0;
		scanf("%s", s);
		n = strlen(s);
		reverse(s, s + n);
		FOR(i,0,n) s[i] = s[i] == '+';
		m = 1;
		a[0] = s[0];
		FOR(i,0,n) if (s[i] != a[m - 1]) a[m++] = s[i];
		n = m;
		FOR(i,0,n){
			if (a[i]) continue;
			if (a[n - 1]){
				ans += 1;
				a[n - 1] = 0;
			}
			ans += 1;
			reverse(a + i, a + n);
			FOR(j,i,n) a[j] = 1 - a[j];
		}
		printf("Case #%d: %d\n", cc, ans);
	}
	return 0;
}

