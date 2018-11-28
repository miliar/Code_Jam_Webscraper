#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <vector>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

typedef long long LL;

int INT(){int x;scanf("%d",&x);return x;}

#define CLR(A,X) memset((A),(X),sizeof((A))
#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)


int N, R, P, S;

char ans[3][1<<13];

void gen(int k, char winner, char* res) {
	if (k == 0) {
		res[0] = winner;
		return;
	}
	char W, L;
	if (winner == 'R') {
		W = 'R';
		L = 'S';
	} else if (winner == 'P') {
		W = 'P';
		L = 'R';
	} else {
		W = 'S';
		L = 'P';
	}
	gen(k-1, W, res);
	gen(k-1, L, res + (1<<(k-1)));
}

bool isOk(char* res) {
	int r=0,p=0,s=0;
	FOR(i,(R+P+S)) {
		if(res[i]=='R')++r;
		else if(res[i]=='P')++p;
		else ++s;
	}
	return R==r && P==p && S==s;
}

void minimize(char *res, int k) {
	if (k==0) return;
	minimize(res, k-1);
	minimize(res+(1<<(k-1)), k-1);
	
	int cmp_ = 0;
	for (int i = 0, j = (1<<(k-1)); i < (1<<(k-1)); ++i, ++j) {
		if (res[i] != res[j]) {
			cmp_ = (int)res[i] - (int)res[j];
			break;
		}
	}
	if (cmp_ > 0) {
		for (int i = 0, j = (1<<(k-1)); i < (1<<(k-1)); ++i, ++j) {
			std::swap(res[i], res[j]);
		}
	}
}

int main() {
	int T=INT();
	REP(t,1,T) {
		N=INT();R=INT();P=INT();S=INT();
		memset(ans,0,sizeof(ans));
		gen(N, 'R', ans[0]); minimize(ans[0], N);
		gen(N, 'P', ans[1]); minimize(ans[1], N);
		gen(N, 'S', ans[2]); minimize(ans[2], N);
		int k = -1;	
		for (int i=0;i<3;++i) {
			if (k==-1) {
				if (isOk(ans[i])) k=i;
			} else if (isOk(ans[i]) && strcmp(ans[i],ans[k])<0) {
				k=i;
			}
		}

		printf("Case #%d: ", t);
		if (k==-1) puts("IMPOSSIBLE");
		else puts(ans[k]);
	}
	return 0;
}
