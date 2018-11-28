/* Man Mohan Mishra aka m17
   IIIT - Allahabad */
#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <iterator>

#define MOD 1000000007
#define INF 1000000000000000000
#define PI acos(-1)

using namespace std;

long long GCD (long long a,long long b) {
	if (b == 0) return a;
	return(a % b == 0 ? b : GCD(b,a % b));
}

long long POW (long long base,long long exp) {
	long long val;
	val = 1;
	while (exp > 0) {
		if (exp % 2 == 1) {
			val = (val * base) % MOD;
		}
		base = (base * base) % MOD;
		exp = exp / 2;
	}
	return val;
}

int a[1005];

int main()
{
//	freopen("input.in","r",stdin);
//	freopen("output.in","w",stdout);
	int t,tc;
	scanf("%d",&t);
	tc = 1;
	while (t --) {
		int n,m,i,j,moves,ans;
		scanf("%d",&n);
		m = -1;
		for (i = 0; i < n; i++) {
			scanf("%d",&a[i]);
			m = max(m,a[i]);
		}
		ans = m;
		for (i = 1; i < m; i++) {
			moves = 0;
			for (j = 0; j < n; j++) {
				moves = moves + a[j] / i + 1 * (a[j] % i != 0) - 1;
			}
			ans = min(ans,moves + i);
		}
		printf("Case #%d: %d\n",tc,ans);
		tc += 1;
	}
	return 0;
}
