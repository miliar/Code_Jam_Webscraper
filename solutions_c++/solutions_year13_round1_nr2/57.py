#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#define INF 1000000000
#define INFll 1000000000000000000ll
#define LD long double
#define LL long long
#define Vi vector<int>
#define VI Vi::iterator
#define Si set<int>
#define SI Si::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Li list<int>
#define LI Li::iterator
#define pb push_back
#define mp make_pair
using namespace std;

int tst, E, R, n, a[11111], Q[11111][2], l, r;
LL ans;

LL solve(){
	scanf("%d%d%d", &E, &R, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	if (R > E) R = E;
	l = r = 0;
	ans = 0;
	Q[0][0] = a[0];
	Q[0][1] = E;
	for (int i = 1; i < n; i++){
		int ss = 0;
		while (l <= r && ss + Q[l][1] <= R){
			ans += (LL)Q[l][0] * (LL)Q[l][1];
			ss += Q[l++][1];
		}
		ans += (LL)Q[l][0] * (LL)(R - ss);
		Q[l][1] -= (R - ss);
		ss = 0;
		while (l <= r && Q[r][0] < a[i])
			ss += Q[r--][1];
		Q[++r][0] = a[i];
		Q[r][1] = ss + R;
	}
	for (int i = l; i <= r; i++)
		ans += (LL)Q[i][0] * (LL)Q[i][1];
	return ans;
}

int main(){
	cin >> tst;
	for (int i = 1; i <= tst; i++)
		printf("Case #%d: %lld\n", i, solve());
	return 0;
}






