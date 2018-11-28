#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>
#include <fstream>
#include <iomanip>

using namespace std;

const int N = 100000;

int T, p = 1;
double C, F, X;
double dp[N];

int main()
{
	cin >> T;
	while(T--)
	{
		cin >> C >> F >> X;
		dp[0] = 0.0;
		for(int i = 1; i < N; i++)
			dp[i] = C / (2.0 + F * (i - 1)) + dp[i - 1];
		for(int i = 0; i < N; i++)
			dp[i] += X / (2.0 + F * i);
		double ans = dp[0];
		for(int i = 1; i < N; i++)
			ans = min(ans, dp[i]);
		printf("Case #%d: %.7f\n", p++, ans);
	}
	return 0;
}