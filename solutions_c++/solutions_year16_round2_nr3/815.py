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
		int n;
		vector<string> vs1, vs2;
		map<string, int> ms1, ms2;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			string s1, s2;
			cin >> s1 >> s2;
			vs1.push_back(s1);
			vs2.push_back(s2);
		}
		int ans = 0;
		for (int i = 0; i < (1 << n); i++)
		{
			
			int sum = 0;
			ms1.clear();
			ms2.clear();
			for (int j = 0; j < n; j++)
			{
				if (i&(1 << j)) sum++;
				else ms1[vs1[j]] = 1, ms2[vs2[j]] = 1;
			}
			int flag = 1;
			for (int j = 0; j < n; j++)
			{
				if (i&(1 << j))
				{
					if (ms1.count(vs1[j]) && ms2.count(vs2[j])) continue;
					flag = 0;
					break;
				}
			}
			if (flag) ans = max(ans, sum);
		}
		printf("Case #%d: %d\n", ks++, ans);
	}

	return 0;
}