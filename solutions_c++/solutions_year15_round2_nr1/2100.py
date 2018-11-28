#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

int T;
ll N;

ll getrev(ll num)
{
	ll ret = 0;
	while (num > 0)
	{
		ret = 10*ret + num % 10;
		num /= 10;
	}
	return ret;
}

//ll get9(ll num)
//{
//	ll temp = 1;
//	while (10*temp <= num)
//		temp *= 10;
//	return temp - 1;
//}
//
//ll go1(ll num)
//{
//	ll ret = 0;
//
//	if (num % 10 == 0)
//	{
//		ret += 9;
//		num -= 9;
//	}
//	else
//	{
//		ret += (num % 10) - 1;
//		num = num - (num % 10) + 1;
//	}
//
//	if (getrev(num) != num)
//	{
//		ret++;
//		num = getrev(num);
//	}
//
//	ret += num - get9(num);
//
//	return ret;
//}
//
//ll go2(ll num)
//{
//	ll ret = 0;
//	
//	if (getrev(num) != num)
//	{
//		ret++;
//		num = getrev(num);
//	}
//
//	if (num % 10 == 0)
//	{
//		ret += 9;
//		num -= 9;
//	}
//	else
//	{
//		ret += (num % 10) - 1;
//		num = num - (num % 10) + 1;
//	}
//
//	if (getrev(num) != num)
//	{
//		ret++;
//		num = getrev(num);
//	}
//
//	ret += num - get9(num);
//
//	return ret;
//}
//
//ll cnt()
//{
//	ll ans = 0;
//	while (N > 0)
//	{
//		ll a = getrev(N) % 10, b = N % 10, c = get9(N);
//		if (a == 1)
//			ans += N - c;
//		else
//		{
//			if (b == 0)
//				ans += go1(N);
//			else
//				ans += min(go1(N), go2(N));
//		}
//		N = c;
//	}
//
//	return ans;
//}

const int MAXN = 1000005;
int dp[MAXN];

int getdp(int num)
{
	if (dp[num] != -1)
		return dp[num];

	dp[num] = getdp(num - 1) + 1;
	if (num % 10 != 0 && getrev(num) < num)
		dp[num] = min(dp[num], getdp(getrev(num)) + 1);
	return dp[num];
}

int main()
{
	ifstream in ("input.txt");
	ofstream out ("output.txt");

	memset(dp, -1, sizeof(dp));
	dp[0] = 0;

	for (int i = 1; i < MAXN; i++)
		dp[i] = getdp(i);

	in >> T;
	for (int t = 1; t <= T; t++)
	{
		in >> N;
		out << "Case #" << t << ": " << dp[N] << "\n";
	}

	in.close();
	out.close();
	return 0;
}