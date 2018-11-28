#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MEM(a,b) memset((a),(b),sizeof(a))
const LL INF = 1e9 + 7;
const int N = 1e6 + 10;
bool match(int x, string str)
{
	int l = str.length();
	while (--l >= 0)
	{
		if (!isdigit(str[l]))
		{
			x /= 10;
			continue;
		}
		if (str[l] != x % 10 + '0') return false;
		x /= 10;
	}
	return true;
}

void output(int x, int len)
{
	string str;
	while (len--) str.push_back(x % 10 + '0'), x /= 10;
	reverse(str.begin(), str.end());
	printf(" %s", str.c_str());
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	string str;
	int ks = 1;
	while (ncase--)
	{
		string str1, str2;
		cin >> str1 >> str2;
		int ans = 1000;
		int k1 = 0, k2 = 0;
		int n = str1.length();
		int t = 1;
		while (n--) t *= 10;
		for (int i = 0; i < t; i++)
		{
			if (!match(i, str1)) continue;
			for (int j = 0; j < t; j++)
			{
				if (!match(j, str2)) continue;
				if (ans > abs(i - j))
				{
					ans = abs(i - j);
					k1 = i;
					k2 = j;
				}
			}
		}
		printf("Case #%d:", ks++);
		output(k1, str1.length());
		output(k2, str2.length());
		puts("");
	}

	return 0;
}