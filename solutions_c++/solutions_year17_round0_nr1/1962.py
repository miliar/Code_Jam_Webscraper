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
#include <cassert>
#include <iterator>
#include <complex>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MEM(x, y) memset((x),(y),sizeof(x))
const LL INF = 1e9 + 7;
const int N = 2e5 + 1;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		string str;
		cin >> str;
		int k;
		cin >> k;
		int n = str.length();
		int ans = 0;
		for (int i = 0; i + k <= str.length(); i++)
		{
			if (str[i] == '+') continue;
			ans++;
			for (int j = 0; j < k; j++)
			{
				if (str[i + j] == '+') str[i + j] = '-';
				else str[i + j] = '+';
			}
		}
		int flag = 0;
		for (auto &c : str)
		{
			if (c == '-') flag = 1;
		}
		if (flag) printf("Case #%d: IMPOSSIBLE\n", ks++);
		else printf("Case #%d: %d\n", ks++, ans);
	}
	return 0;
}

