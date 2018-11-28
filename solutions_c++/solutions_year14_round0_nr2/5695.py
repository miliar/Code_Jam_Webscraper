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
int n, m, p;
int T;
double C, F, X;
int main(){
	scanf("%d", &T);
	FOE(cc,1,T){
		printf("Case #%d: ", cc);
		scanf("%lf%lf%lf", &C, &F, &X);
		double tmp = 0, rate = 2, ans = 101011010;
		FOE(i,0,100000){
			ans = min(ans, tmp + X / rate);
			tmp += C / rate;
			rate += F;
		}
		printf("%.12f\n", ans);
	}
	return 0;
}

