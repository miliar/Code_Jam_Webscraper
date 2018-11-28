#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

#define MAX_N 100000

int tests, r1, r2;
int cards1[4][4], cards2[4][4];
int seen[17];

int main() {
	scanf("%d",&tests);
	for (int test = 1; test <= tests; test++) {
		scanf("%d",&r1); r1--;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) scanf("%d",&cards1[i][j]);		
		scanf("%d",&r2); r2--;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) scanf("%d",&cards2[i][j]);
		for (int i = 0; i <= 16; i++) seen[i] = 0;
		
		for (int i = 0; i < 4; i++) seen[cards1[r1][i]]++;
		for (int i = 0; i < 4; i++) seen[cards2[r2][i]]++;
				
		int res = 0, val;
		for (int i = 0; i <= 16; i++) if (seen[i] == 2) { res++; val = i;}
		
		if (res == 0) printf("Case #%d: Volunteer cheated!\n", test);
		if (res == 1) printf("Case #%d: %d\n",test,val);
		if (res > 1) printf("Case #%d: Bad magician!\n", test);		
	}
	return 0;
}