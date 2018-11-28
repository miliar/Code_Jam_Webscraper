// Lupus Nocawy 2016
// Code Jam 2016
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/6254486/dashboard
// Problem D. Fractiles

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,b) for(int i=(a), _b=(b); i<=_b; ++i)
typedef unsigned long long int llu;

void solve(void){
	int k,c,s;
	scanf("%d %d %d ", &k, &c, &s);
	FOR(i,1,k)
		printf("%d ", i);
	printf("\n");
	return;
}

int main(void){
	int t;
	scanf("%d ", &t);
	for(int c=1; c<=t; ++c){
		printf("Case #%d: ", c);
		solve();
	}
	return 0;
}
