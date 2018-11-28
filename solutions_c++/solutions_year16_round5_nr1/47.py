#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <iterator>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define add(x,y) ((ll)(x)+(y))%mod
#define F(i,n) for(int i = 0; i < n; i++)
#define FF(i,n) for(int i = 1; i <= n; i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const double pi = 3.1415926535897932384626433832795;
//----------------------------------------------------------------------------//

char buf[20001];

int main() {
#ifndef __GNUG__
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	FF(tt, T) {
		printf("Case #%d: ", tt);
		//-----------------------Your code goes here------------------------//
		vector<int> stk;
		scanf("%s", buf);
		int ans = 0;
		int n = strlen(buf);
		F(i, n) {
			int cur = (buf[i] == 'C');
			stk.push_back(cur);
			int sz = stk.size();
			if (sz >= 2 && stk[sz-1] == stk[sz-2]) {
				stk.resize(sz - 2);
				ans += 2;
			}
		}
		ans += stk.size() / 2;
		printf("%d\n", ans * 5);
		//------------------------------------------------------------------//
		fprintf(stderr, "Case %d complete\n", tt);
	}
	return 0;
}
