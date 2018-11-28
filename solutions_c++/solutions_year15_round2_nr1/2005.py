#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <tuple>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int n;
int dp[1000002];

int rev(int x){
	int ret = 0;
	while (x){
		ret = ret * 10 + x % 10;
		x /= 10;
	}
	return ret;
}

int f1(int x){
	int tmp = rev(x), ans = 1e9;

	if (x == 0) return 0;

	if (dp[x] != -1) return dp[x];

	if (x % 10 != 0 && tmp < x){
		ans = min(ans, f1(x - 1) + 1);
		ans = min(ans, f1(tmp) + 1);
	}
	else ans = min(ans, f1(x - 1) + 1);

	return dp[x] = ans;
}

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	memset(dp, -1, sizeof dp);
	f1(3600);
	for (int i = 4000; i <= 1000000; i += 3000) f1(i);
	for (int tc = 1; tc <= t; tc++){
		cin >> n;
		cout << "Case #" << tc << ": " << dp[n] << endl;
	}
}