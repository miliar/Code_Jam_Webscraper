#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <sstream>
#include <utility>
#include <numeric>
#include <functional>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define F(i,a) FOR(i,0,a)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define X first
#define Y second
#define S size()
#define MS(a, v) memset(a, v, sizeof a)
#define NL printf("\n")
#define SP system("pause")
#define INF 1e9
#define PI acos(-1)
#define EPS 1e-9
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main()
{
	// ios_base::sync_with_stdio(0);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t, r1, r2, m[16][16], aux, ans;
	bool check[20];
	scanf("%d", &t);
	F(tc, t) {
		printf("Case #%d: ", tc + 1);
		MS(check, false);
		scanf("%d", &r1); r1--;
		F(i, 4) F(j, 4) { scanf("%d", &m[i][j]); if(i == r1) check[m[i][j]] = true; }
		int c = 0;
		scanf("%d", &r2); r2--;
		F(i, 4) F(j, 4) { scanf("%d", &aux); if(i == r2 && check[aux]) ans = aux, c++; }
		if(!c) printf("Volunteer cheated!\n");
		else if(c == 1)	printf("%d\n", ans);
		else printf("Bad magician!\n"); 
	}
	return 0;
}