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

#define MAXN 120

int n, m;
int inp[MAXN][MAXN];
int line[MAXN], colu[MAXN];

int main() {
	int t, caso = 0; scanf("%d", &t);
	while(t--) {
		scanf("%d%d", &n, &m);
		Fr(i,0,n) Fr(j,0,m) scanf("%d", &inp[i][j]);
		
		Fr(i,0,n) line[i] = 0;
		Fr(i,0,m) colu[i] = 0;
		Fr(i,0,n) Fr(j,0,m) {
			line[i] = max(line[i], inp[i][j]);
			colu[j] = max(colu[j], inp[i][j]);
		}
		
		/*
		Fr(i,0,n) Fr(j,0,m) {
			printf(" inp[%d][%d] %d, line %d, colu %d\n", i, j, inp[i][j], line[i], colu[j]);
		} puts("");
		//*/
		
		bool ok = true;
		Fr(i,0,n) Fr(j,0,m) ok &= min(line[i], colu[j]) == inp[i][j];
		
		if(ok) printf("Case #%d: YES\n", ++caso);
		else printf("Case #%d: NO\n", ++caso);
	}
	
	return 0;
}


