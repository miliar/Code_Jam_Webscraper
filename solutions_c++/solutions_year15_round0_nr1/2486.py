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

char s[1005];

int main()
{
//	freopen("input.in","r",stdin);
//	freopen("output.in","w",stdout);
	int t,tc;
	scanf("%d",&t);
	tc = 1;
	while (t --) {
		int n,i,cur,ans;
		scanf("%d",&n);
		scanf("%s",s);
		ans = 0;
		cur = 0;
		for (i = 0; i <= n; i++) {
			if (s[i] == '0') continue;
			if (cur >= i) {
				cur = cur + s[i] - '0';
			} else {
				ans = ans + (i - cur);
				cur = cur + (i - cur);
				cur = cur + s[i] - '0';
			}
		}
		printf("Case #%d: %d\n",tc,ans);
		tc += 1;
	}
	return 0;
}
