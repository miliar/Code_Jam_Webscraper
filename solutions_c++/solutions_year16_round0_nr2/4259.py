#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <climits>
#include <cfloat>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stdexcept>

using namespace std;

#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ULL unsigned long long
#define LL long long
#define REP(i,n) for(int i=0;i<(n);i++)
#define set_bit(x, i) (x) |= (1 << (i))
#define clr_bit(x, i) (x) & ~(1 << (i))
#define tog_bit(x, i) (x) ^= (1 << (i))
#define chk_bit(x, i) (((x) >> (i)) & 1)
#define feq(x,y) (fabs(x-y) <= DBL_EPSILON)


#define MOD 1000000007

typedef pair<int,int> ii;
#define mp make_pair


#define sq(x) ((x)*(x))


int solve(string s) {
	int ans = 0;
	int n = s.size();
	int i = 0;
	if(s[0] == '-') 
		ans += 1;
	while(s[i] == '-' && i < n)
		i++;
	for(;i<n;i++) {
		if(s[i] == '-')
			ans += 2;
		while(s[i] == '-')
			i++;
	}
	return ans;
}

//#define ONLINE_JUDGE
int main() {

#ifndef ONLINE_JUDGE
	//freopen("test", "r", stdin);
	freopen("large-in", "r", stdin);
	freopen("large-out", "w+", stdout);
#endif

	int testcases = 0;
	scanf("%d", &testcases);
	for(int k=1;k<=testcases;k++) {

		string s;
		cin >> s;

		int ans = solve(s);
		printf("Case #%d: %d\n", k, ans);
	}

	return 0;
} 


