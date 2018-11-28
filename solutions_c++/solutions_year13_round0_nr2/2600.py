#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
using namespace std; 

#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define forit(it,S) for(__typeof(S.begin()) it = S.begin(); it != S.end(); ++it)
#ifdef WIN32
	#define I64d "%I64d"
#else
	#define I64d "%lld"
#endif

typedef pair <int, int> pi;
int a[111][111], rm[111], cm[111], n, m;

int main() {
	int tests;
	scanf("%d", &tests);	
	for (int casenum = 1; casenum <= tests; ++casenum) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf("%d", &a[i][j]);
		for (int i = 0; i < n; ++i) {
			rm[i] = a[i][0];
			for (int j = 1; j < m; ++j)
				rm[i] >?= a[i][j];
		}			
		for (int j = 0; j < m; ++j) {
			cm[j] = a[0][j];
			for (int i = 1; i < n; ++i)
				cm[j] >?= a[i][j];
		}
		bool ok = true;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (a[i][j] < rm[i] && a[i][j] < cm[j])
					ok = false;
		printf("Case #%d: %s\n", casenum, ok ? "YES": "NO");
	}
	return 0;		
}
