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
int T;
int a[20], b[20], r;
int main(){
	scanf("%d", &T);
	FOE(cc,1,T){
		printf("Case #%d: ", cc);
		scanf("%d", &r);
		r--;
		FOR(i,0,4) FOR(j,0,4)
			if (i == r) scanf("%d", a + j);
			else scanf("%d", &n);
		scanf("%d", &r);
		r--;
		FOR(i,0,4) FOR(j,0,4){
			scanf("%d", &n);
			b[n] = i;
		}
		m = 0;
		FOR(i,0,4) if (b[a[i]] == r) { m++; n = a[i]; }
		if (!m) puts("Volunteer cheated!");
		else if (m == 1) printf("%d\n", n);
		else puts("Bad magician!");
	}
	return 0;
}

