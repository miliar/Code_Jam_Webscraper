#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <list>

// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
#define INF                         (int)1e9
#define EPS                         1e-9

#define bitcount                    __builtin_popcount
#define gcd                         __gcd

#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define mp							make_pair
#define DEBUG

using namespace std;

int g[101][101];

int T, m, n;

bool check(int i, int j) {
	bool valid = true;
	for (int k = 0; k < n; k++)
		if (g[k][j] > g[i][j])
			valid = false;
	if (!valid) {


		valid = true;
		for (int k = 0; k < m; k++)
			if (g[i][k] > g[i][j])
				valid = false;
	}
	return valid;
}
void solve(int t) {
	forall(i, 0, n)
		forall(j, 0, m)
			if (!check(i, j)) {
				//printf("a7a (%d, %d)\n", i, j);
				printf("Case #%d: NO\n", t);
				return;
			}
	printf("Case #%d: YES\n", t);
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &T);

	forall(t, 1, T+1) {
		scanf("%d %d", &n, &m);
		forall(i, 0, n)
			forall(j, 0, m)
				scanf("%d", g[i] + j);

		solve(t);

	}

	return 0;
}
