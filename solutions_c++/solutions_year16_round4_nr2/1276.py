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
#define N 201
int count (int x){
	int ret = 0;
	while(x){
		x -= x & -x;
		ret++;
	}
	return ret;
}
int n, m, tt;
double p[N];
double f(int x, int y, int k){
	if (y == n && k) return 0;
	if (y == n && !k) return 1;
	if ((1 << y) & x){
		double t1 =  p[y] * f(x, y + 1, k + 1) , t2 = (1 - p[y]) * f(x, y + 1, k - 1);
		//printf("%d %d %d %f %f\n", x, y, k, t1, t2);
		return t1 + t2;
//		return p[y] * f(x, y + 1, k + 1) + (1 - p[y]) * f(x, y + 1, k - 1);
	}
	else return f(x, y + 1, k);
}
int main(){
	int T;
	int k;
	scanf("%d", &T);
	FOE(cc,1,T){
		tt = cc;
		scanf("%d%d", &n, &k);
		double ans = 0;
		FOR(i,0,n) scanf("%lf", &p[i]);
		//FOR(i,0,n) printf("%f\n", p[i]);
		FOR(i,0,1 << n) if (count(i) == k)
		{
		//	printf("%d %d %f\n", i, k, f(i, 0, 0));
			ans = max(ans, f(i, 0, 0));
		}
		printf("Case #%d: %.12f\n", cc, ans);
	}
	return 0;
}

