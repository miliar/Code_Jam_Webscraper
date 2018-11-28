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
int T, x, y, p, a1, a2;
double a[10101], b[10101];
int main(){
	scanf("%d", &T);
	FOE(cc,1,T){
		printf("Case #%d: ", cc);
		scanf("%d", &n);
		FOR(i,0,n) scanf("%lf", a + i);
		FOR(i,0,n) scanf("%lf", b + i);
		sort(a, a + n);
		sort(b, b + n);
		x = 0;
		y = n - 1;
		a1 = a2 = 0;
		FOR(i,0,n){
			if (a[i] > b[x]) { x++; a1++; }
			else y--;
		}
		x = 0;
		FOR(i,0,n){
			while(x < n && a[i] > b[x]) x++;
			if (x == n) a2++;
			else x++;
		}
		printf("%d %d\n", a1, a2);
	}
	return 0;
}

