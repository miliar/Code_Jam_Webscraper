#pragma region Saaman


/*

This code is exclusive property of Anant Simran Singh.
Any use without his consent will result in copyright violation.

*/

#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS 
#define getchar_unlocked() getchar()
#endif 
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstdlib>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<string>
#include<climits>
#include<bitset>
#include<cfloat>
#include<sstream>
#include<iomanip>
#include<array>
#include<unordered_set>
#include<unordered_map>
#include<limits>
using namespace std;
const int maximum_string_length = (int)1e3 + 5;
inline void in(char &d)
{
	d = getchar_unlocked();
	while ((d<33) || (d>126))
	{
		d = getchar_unlocked();
	}
}
inline void in(string &str)
{
	str.clear();
	str.reserve(maximum_string_length);
	char c = getchar_unlocked();
	while ((c<33) || (c>126))
	{
		c = getchar_unlocked();
	}
	while ((c >= 33) && (c <= 126))
	{
		str.push_back(c);
		c = getchar_unlocked();
	}
	return;
}
template<typename T>
inline void in(T & t){
	char c, m = 0;
	t = 0;
	c = getchar_unlocked();
	while ((c<'0' || c>'9') && c != '-')
		c = getchar_unlocked();
	if (c == '-')
		m = 1,
		c = getchar_unlocked();

	while (c >= '0' && c <= '9'){
		t = (t << 3) + (t << 1) + c - '0';
		c = getchar_unlocked();
	}
	if (m)
		t = 0 - t;


}
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
#pragma endregion

const int maxb = 1005;
const int maxn = 1005;

int base[maxb][maxb];

void initialise_base()
{
	for (size_t i = 2; i < maxb; i++)
	{
		for (size_t j = 1; j < i; j++)
		{
			base[i][j] = 1 + base[i - j][j];
		}
	}
}



int main()
{
	initialise_base();
	int t, n,cas=1;
	ull ans;
	array<int, maxn> arr;
	int dp[maxn][maxb];
	in(t);
	while (t--)
	{
		in(n);
		for (size_t i = 0; i < n; i++)
		{
			in(arr[i]);
		}
		for (size_t i = 0; i < n; i++)
		{
			for (size_t j = 0; j < maxb; j++)
			{
				dp[i][j] = 0;
			}
		}
		for (size_t j = 1; j <= arr[0]; j++)
		{
			dp[0][j] = base[arr[0]][j];
		}
		for (size_t i = 1; i < n; i++)
		{
			for (size_t j = 1; j <maxb; j++)
			{
				dp[i][j] = base[arr[i]][j] + dp[i - 1][j];
			}
		}
		ans = LONG_MAX;
		for (size_t j = 1; j < maxb; j++)
		{
			ans = min(ans, (ull)dp[n - 1][j] + j);
		}
		printf("Case #%d: %d\n", cas, ans);
		cas++;
	}

	return 0;
}
