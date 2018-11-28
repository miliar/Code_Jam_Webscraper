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
		cin >> str;
		string ans;
		ans += str[0];
		for (int i = 1; i < str.length(); i++)
		{
			if (str[i] >= ans[0]) ans = str[i] + ans;
			else ans.push_back(str[i]);
		}
		printf("Case #%d: %s\n", ks++, ans.c_str());
	}

	return 0;
}