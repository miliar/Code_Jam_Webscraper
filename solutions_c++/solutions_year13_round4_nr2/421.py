#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pb push_back
#define mp make_pair
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
using namespace std;

bool c1(LL x, int n, LL p){
	LL pos = 0;
	for (int i = 0; i < n; i++){
		LL t = (1ll << i) | pos;
		pos = (pos << 1) + (t <= x);
	}
	return pos < p;
}

bool c2(LL x, int n, LL p){
	LL pos = 0;
	for (int i = 0; i < n; i++){
		LL t = (1ll << i) | (((1ll << i) - 1) ^ pos);
		pos = (pos << 1) + ((1ll << n) - t <= x);
	}
	return pos < p;
}

void solve(){
	LL n, p;
	cin >> n >> p;
	LL l = 0, r = (1ll << n) - 1, ans = 0;
	while (l <= r){
		LL m = (l + r) / 2;
		if (c1(m, n, p)){
			ans = m;
			l = m + 1;
		}
		else
			r = m - 1;
	}
	cout << ans << " ";
	l = 0, r = (1ll << n) - 1, ans = 0;
	while (l <= r){
		LL m = (l + r) / 2;
		if (c2(m, n, p)){
			ans = m;
			l = m + 1;
		}
		else
			r = m - 1;
	}
	cout << ans << endl;
}

int main(){
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; i++){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
