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

bool check(vector<pair<int,int>> &vp)
{
	int sum = 0;
	int maxv = 0;
	for (int i = 0; i < vp.size(); i++)
	{
		sum += vp[i].first;
		maxv = max(maxv, vp[i].first);
	}
	return maxv * 2 <= sum;
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
		int n;
		cin >> n;
		vector<pair<int, int>> vp;
		vector<string> vs;
		for (int i = 0; i < n; i++)
		{
			int x;
			cin >> x;
			vp.push_back({ x,i });
		}
		sort(vp.begin(), vp.end());
		while (vp.back().first != 0)
		{
			string str = "";
			vp[n - 1].first--;
			str.push_back(vp[n - 1].second + 'A');
			if (check(vp))
			{
				
				vs.push_back(str);
				sort(vp.begin(), vp.end());
				continue;
			}
			vp[n - 2].first--;
			str.push_back(vp[n - 2].second + 'A');
			if (check(vp))
			{
				vs.push_back(str);
				sort(vp.begin(), vp.end());
				continue;
			}

		}
		printf("Case #%d:", ks++);
		for (auto str : vs) printf(" %s", str.c_str());
		puts("");
	}

	return 0;
}