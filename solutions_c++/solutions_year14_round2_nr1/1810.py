#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <memory.h>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;

vector<string> original;
vector<string> compressed;
vector<vector<int> > comp_int;

int check(int x, int p)
{
	int sum = 0;
	for (int i = 0; i < compressed.size(); i++)
	{
		sum += abs(comp_int[i][p] - x);
	}
	return sum;
}

int main(void)
{
	freopen("input.txt","r", stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int q = 1; q <= t; q++)
	{
		int n;
		scanf("%d", &n);
		comp_int.clear();
		compressed.clear();
		original.clear();
		comp_int.resize(n);

		for (int i = 0; i < n; i++)
		{
			char s[105];
			scanf("%s", &s);
			string a = (string) s;
			string b = "";
			char prev = 0;
			int cnt = 0;
			for (int j = 0; j < a.length(); j++)
			{
				if (a[j] != prev)
				{
					if (cnt != 0)
						comp_int[i].push_back(cnt);
					b += a[j];
					cnt = 1;
				}
				else
					cnt++;
				prev = a[j];
			}
			if (cnt != 0)
				comp_int[i].push_back(cnt);
			original.push_back(a);
			compressed.push_back(b);
		}
		bool ok = 1;
		for (int i = 1; i < n; i++)
			if (compressed[i] != compressed[i-1])
			{
				ok = 0;
				break;
			}
		if (!ok)
		{
			printf("Case #%d: Fegla Won\n", q);
		}
		else
		{
			int res = 0;
			for (int i = 0; i < comp_int[0].size(); i++)
			{
				int sum = 0;
				for (int j = 0; j < n; j++)
					sum += comp_int[j][i];
				sum /= n;
				int tmp = check(sum, i);
				tmp = min(tmp, check(sum+1, i));
				res += tmp;
			}
			printf("Case #%d: %d\n", q, res);
		}
	}
	return 0;
}