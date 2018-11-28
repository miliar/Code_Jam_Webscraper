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

const int INF = 1e9 + 3;
const int N = 20 + 1;
LL str2num(string str)
{
	LL ret = 0;
	for (int i = 0; i < str.length(); i++) ret *= 10, ret += str[i] - '0';
	return ret;
}

bool check(string str)
{
	for (int i = 0; i < str.length(); i++) if (str[i] != '0') return true;
	return false;
}
LL getans(LL n, LL t)
{
	string str;
	LL ret = n-t;
	if (t == 1) ret++;
	while (n)
	{
		str.push_back(n % 10 + '0');
		n /= 10;
	}
	LL flag = 0;
	reverse(str.begin(), str.end());
	for (int i = 0; i <= str.length(); i++)
	{
		
		string s1 = str.substr(0, i);
		string s2 = str.substr(i);
		if (!check(s2)) continue;
		reverse(s1.begin(), s1.end());
		ret = min(ret, str2num(s1) + str2num(s2));
	}
	return ret;
}

LL getresult(LL n)
{
	LL t = 10;
	LL ans = 0;
	while (1)
	{
		if (t > n)
		{
			ans += getans(n, t / 10);
			break;
		}
		ans += getans(t - 1, t / 10) + 1;
		t *= 10;
	}
	return ans;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		LL n;
		cin >> n;
		LL ans = min(getresult(n), getresult(n - 1) + 1);
		printf("Case #%d: %lld\n", ks++, ans);
	}
	return 0;
}