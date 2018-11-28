#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <functional>
#include <algorithm>
#include <bitset>
#include <set>
#include <stack>
#include <limits>
#include <sstream>
#include <ctime> 
#define endl '\n'
#pragma warning (disable : 4996)

using namespace std;

#define lli long long int
#define ull unsigned long long int
#define MP make_pair

const int N = (int)(2e7 + 20);
const int L = 20;
const lli M = 1000000007;
const double E = 1e-7;

int dp[N];

int reverse(int n) {
	int res = 0;
	while (n) {
		res = res * 10 + (n % 10);
		n /= 10;
	}
	return res;
}

int main()
{
	ios_base::sync_with_stdio(0);
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif      
	int T;
	cin >> T;

	dp[1] = 1;
	for (int i = 1; i < 1010000; ++i) {
		if (!dp[i + 1]) dp[i + 1] = dp[i] + 1;
	}
	for (int i = 1; i < 1010000; ++i) {
		dp[i + 1] = min(dp[i] + 1, dp[i+1]);
		int rev = reverse(i);
		dp[rev] = min(dp[rev], dp[i] + 1);
	}

	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		int n;
		cin >> n;
		cout << dp[n];

		cout << endl;
	}
}