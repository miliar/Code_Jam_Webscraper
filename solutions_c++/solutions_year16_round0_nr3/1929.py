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
#define N 100005

/***************************************************************/

bool isp[N+5];
int prime[1000005], pcnt;
void make_prime() {
	MSET(isp, true);
	pcnt = 2;
	prime[0] = 2, prime[1] = 3;
	for(int i=5, j=2; i<=N; i+=j, j^=6) {
		if( isp[i] ) {
			prime[pcnt++] = i;
			if( 1ll*i*i<=N )
				for(int k=i*i; k<=N; k+=i)
					isp[k] = false;
		}
	}
}

struct Item {
	unsigned num;
	int fac[11];
};

vector<Item> ans[33];

int check(unsigned num_rev, int base, unsigned num) {
	unsigned num_rev2, rem;
	int modd;
	for(int i=0; i<pcnt; ++i) {
		num_rev2 = num_rev;
		rem = 0;
		modd = 0;
		while( num_rev2 ) {
			rem = rem*base+(num_rev2&1);
			if( rem>=prime[i] )
				rem %= prime[i], modd++;
			num_rev2>>=1;
		}
		if( rem==0 && modd>1 ) return prime[i];
	}
	//printf("cant check %u under base %d\n", num, base);
	return 0;
}

void solve(int n, int j) {
	unsigned num = 1u<<(n-1) | 1, num2, num_rev;
	bool valid;
	Item tmp;
	for(; j; num+=2) {
		valid = true;
		num2 = num, num_rev = 0;
		while( num2 ) {
			num_rev = (num_rev<<1) | (num2&1);
			num2 >>= 1;
		}
		for(int i=2; i<=10; i++)
			if( !(tmp.fac[i] = check(num_rev, i, num)) ) {
				valid = false;
				break;
			}
		if( valid ) {
			tmp.num = num;
			--j;
			ans[n].PB(tmp);
			/*while( num_rev ) {
				printf("%d", num_rev&1);
				num_rev>>=1;
			}
			puts("~");*/
		}
	}
}

int main() {
#ifdef KEVINPTT
	//freopen("a.in", "r", stdin);
	//freopen("a.ans", "w", stdout);
#endif
	make_prime();
	for(int i=2; i<=32; i++) {
		int j = min(500, 1<<(i-2));
		solve(i, j);
	}
	DRI(t);
	REP1(casen, t) {
		DRII(n, m);
		printf("Case #%d:\n", casen);
		//solve(n, m);
		//puts("OK");
		for(int i=0; i<m; ++i) {
			for(int j=n-1; j>=0; --j)
				printf("%d", (ans[n][i].num>>j)&1);
			for(int j=2; j<=10; ++j)
				printf(" %d", ans[n][i].fac[j]);
			puts("");
		}
	}
	
	return 0;
}

