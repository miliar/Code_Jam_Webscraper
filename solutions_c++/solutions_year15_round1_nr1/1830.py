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
const int maximum_string_length = (int)1e4 + 5;
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
template <typename T>
int signum(T val) {
	return (T(0) < val) - (val < T(0));

}
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
#pragma endregion

const int maxn = 1005;

int main()
{
	int t, n, cas = 1,ans1,ans2,min_diff;
	array<int, maxn> arr;
	array<int, maxn> diff;
	in(t);
	while (t--)
	{
		in(n);
		for (size_t i = 0; i < n; i++)
		{
			in(arr[i]);
		}
		for (size_t i = 1; i < n; i++)
		{
			diff[i-1] = arr[i] - arr[i - 1];
		}
		min_diff = INT_MAX;
		ans1 = ans2 = 0;
		for (size_t i = 0; i < n-1; i++)
		{
			min_diff = min(diff[i], min_diff);
			if (diff[i]<0)
			{
				
				ans1 -= diff[i];
			}
		}
		min_diff = -min_diff;
		for (size_t i = 0; i < n-1; i++)
		{
			ans2 += min(arr[i], min_diff);
		}
		printf("Case #%d: %d %d\n", cas, ans1, ans2);
		cas++;
	}

	return 0;
}
