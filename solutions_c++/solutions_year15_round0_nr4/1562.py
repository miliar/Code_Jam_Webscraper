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

int main()
{
//	freopen("input.in","r",stdin);
//	freopen("output.in","w",stdout);
	int t,tc;
	scanf("%d",&t);
	tc = 1;
	while (t --) {
		int x,r,c;
		scanf("%d%d%d",&x,&r,&c);
		if ((r % x == 0 && c >= x - 1) || (c % x == 0 && r >= x - 1)) {
			printf("Case #%d: GABRIEL\n",tc);
		} else {
			printf("Case #%d: RICHARD\n",tc);
		}
		tc += 1;
	}
	return 0;
}
