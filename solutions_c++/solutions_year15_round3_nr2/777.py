#include <iostream>
#include <thread>
#include <Windows.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <iomanip> 

using namespace std;

int nums[26];

void dfs(string &keys, int cur, int s, string str, set<string> &candidates)
{
	if (cur >= s)
	{
		candidates.insert(str);
		return;
	}
	for (int i = 0; i < keys.size(); ++i)
	{
		str.push_back(keys[i]);
		dfs(keys, cur + 1, s, str, candidates);
		str.pop_back();
	}
}

int solve(string s, string t)
{
	int res = 0;
	for (int i = 0; i < s.size(); ++i)
	{
		if (i + t.size()>s.size())break;
		int j = 0;
		for (; j < t.size(); ++j)
		{
			if (s[i + j] != t[j])break;
		}
		if (j == t.size())res++;
	}
	return res;
}

double solve2(string s, int k)
{
	double res = 1.0;
	for (int i = 0; i < s.size(); ++i)
	{
		res = res*((nums[s[i] - 'A'] * 1.0) / (k*1.0));
	}
	return res;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int k, l, s, index = 1;
	int T;
	cin >> T;
	
	while (T--)
	{
		
		//cout << "Case #" << index++ << ": ";
		cin >> k >> l >> s;
		memset(nums, 0, sizeof(nums));
		string keys, target;
		cin >> keys >> target;
		for (int i = 0; i < keys.size(); ++i)nums[keys[i] - 'A']++;
		set<string> candidates;
		string str = "";
		dfs(keys, 0, s, str, candidates);
		int _max = 0;
		double sum = 0;
		for (set<string>::iterator it = candidates.begin(); it != candidates.end(); ++it)
		{
			int num = solve(*it, target);
			sum += (solve2(*it, k)*num*1.0);
			//sum += num;
			if (_max < num)
			{
				_max = num;
			}
		}
		//cout << setprecision(8)<< _max - sum << endl;
		printf("Case #%d: %.8lf\n", index++, (_max*1.0) - sum);
	}
	return 0;
}