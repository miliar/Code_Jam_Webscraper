// Template.cpp by kevinptt 20150108
#include <bits/stdc++.h>
/*
#include <cstdio>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <map>
#include <set>

#include <iostream>
// */
using namespace std;

#define REP(I, N) for(int I=0; I<(N); ++I)
#define REP1(I, N) for(int I=1; I<=(N); ++I)
#define REPP(I, A, B) for(int I=(A); I<(B); ++I)
#define REPR(I, N) for(int I=N-1; I>=0; --I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int X; scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define MP make_pair
#define PB push_back
#define MSET(x, y) memset(x, y, sizeof(x))
#define F first
#define S second
typedef long long ll;
typedef pair<int,int> pii;

/***************************************************************/

bool check[10];
int solve(int n0) {
	int n2, n = n0, cnt;
	MSET(check, false);
	while(1) {
		n2 = n;
		while( n2 ) {
			check[n2%10] = true;
			n2/=10;
		}
		cnt = 0;
		REP(i, 10)
			cnt += check[i];
		if( cnt==10 )
			return n;
		else
			n += n0;
	}
}

int main() {
#ifdef KEVINPTT
	//freopen("a.in", "r", stdin);
	//freopen("a.ans", "w", stdout);
#endif
	DRI(t);
	REP1(casen, t) {
		DRI(n);
		if( n==0 )
			printf("Case #%d: INSOMNIA\n", casen);
		else
			printf("Case #%d: %d\n", casen, solve(n));
	}
	
	return 0;
}

