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


int product[4][4] = { { 1, 2, 3, 4 }, { 2, -1, 4, -3 }, { 3, -4, -1, 2 }, { 4, 3, -2, -1 } };

unordered_map<int, int> mapping = { { 1, 1 }, { 'i', 2 }, { 'j', 3 }, { 'k', 4 } };

int multiply(int x, int y)
{
	return product[abs(x) - 1][abs(y) - 1] * signum(x)*signum(y);
}

int main()
{
	string basic, main;
	vector<int> arr;
	int  t, l, x,ptr,cas=1,pr;
	in(t);
	bool milna = false;
	while (t--)
	{
		in(l);
		in(x);
		arr.clear();
		main.clear();
		//x = min(24, x);
		in(basic);
		main.reserve(basic.size()*x);
		arr.reserve(basic.size()*x);
		while (x--)
		{
			main += basic;
		}
		for (char c : main)
		{
			arr.push_back(mapping[c]);
		}
		int s = arr.size();
		if (s<3)
		{
			printf("Case #%d: NO\n",cas);
			cas++;
			continue;
		}
		ptr = 0;
		pr = 1;
		milna = false;
		pr = 1;
		for (size_t i = ptr; i <s-2 ; i++)
		{
			pr = multiply(pr, arr[i]);
			if (pr==2)
			{
				milna = true;
				ptr = i + 1;
				break;
			}
		}
		if (milna==false)
		{
			printf("Case #%d: NO\n", cas);
			cas++;
			continue;
		}
		milna = false;
		pr = 1;
		for (size_t i = ptr; i <s - 1; i++)
		{
			pr = multiply(pr, arr[i]);
			if (pr == 3)
			{
				milna = true;
				ptr = i + 1;
				break;
			}
		}
		if (milna == false)
		{
			printf("Case #%d: NO\n", cas);
			cas++;
			continue;
		}
		milna = false;
		pr = 1;
		for (size_t i = ptr; i <s; i++)
		{
			pr = multiply(pr, arr[i]);
			if ((pr == 4) && (i==s-1))
			{
				milna = true;
				break;
			}
		}
		if (milna == false)
		{
			printf("Case #%d: NO\n", cas);
			cas++;
			continue;
		}
		printf("Case #%d: YES\n", cas);
		cas++;
	}

	return 0;
}
