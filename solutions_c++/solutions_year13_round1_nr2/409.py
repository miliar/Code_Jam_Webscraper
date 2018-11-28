#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cassert>
#include <ctime>

#define Fr(a,b,c) for(int a = b; a < c; ++a)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define oo 0x3F3F3F3F

#define dbg if(0)

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long rash;

#define MAXN 20

int e, r, n;
int inp[MAXN];
int pd[MAXN][MAXN];

int rec(int lvl, int energy) {
	energy = min(e, energy + r);
	if(pd[lvl][energy] != -1) return pd[lvl][energy];
	if(lvl == n) return pd[lvl][energy] = 0;
	
	pd[lvl][energy] = 0;
	Fr(i,0,energy+1) pd[lvl][energy] = max(pd[lvl][energy], i * inp[lvl] + rec(lvl + 1, energy - i));
//	printf("pd[%d][%d] %d\n", lvl, energy, pd[lvl][energy]);
	return pd[lvl][energy];
}

int main() {
	int t, caso = 0; scanf("%d", &t);
	while(t--) {
		scanf("%d%d%d", &e, &r, &n);
		Fr(i,0,n) scanf("%d", &inp[i]);
		
		memset(pd, -1, sizeof(pd));
		printf("Case #%d: %d\n", ++caso, rec(0, e));
	}
	
	return 0;
}


