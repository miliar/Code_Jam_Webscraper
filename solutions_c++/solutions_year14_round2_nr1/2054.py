#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<math.h>
using namespace std;

int match(string src, string dst)
{
	
	int result = -1; 
	vector<pair<char, int>> s;
	vector<pair<char, int>> d;
	
	while (1)
	{
		if (src.size() == 1)
		{
			s.push_back(make_pair(src[0], 1));
			break;
		}
		int count = 1;
		char cur, nxt;
		for (int i = 0; i < src.size(); i++)
		{		
			cur = src[i];
			if (i + 1 == src.size())
			{
				s.push_back(make_pair(cur, count));
				break;
			}
			nxt = src[i + 1];
			if (cur == nxt)
				count++;
			else
			{
				s.push_back(make_pair(cur, count));
				count = 1;
			}
		}
		break;
	}

	while (1)
	{
		if (dst.size() == 1)
		{
			d.push_back(make_pair(dst[0], 1));
			break;
		}
		int count = 1;
		char cur, nxt;
		for (int i = 0; i < dst.size(); i++)
		{
			cur = dst[i];
			if (i + 1 == dst.size())
			{
				d.push_back(make_pair(cur, count));
				break;
			}
			nxt = dst[i + 1];
			if (cur == nxt)
				count++;
			else
			{
				d.push_back(make_pair(cur, count));
				count = 1;
			}
		}
		break;
	}

	if (s.size() != d.size())
		return -1;
	else
	{
		result = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i].first == d[i].first)
			{
				result += abs(s[i].second - d[i].second);
			}
			else
			{
				result = -1;
				break;
			}
		}
		return result;
	}

	
}

string prune(string src)
{
	vector<pair<char, int>> s;
	vector<pair<char, int>> d;

	while (1)
	{
		if (src.size() == 1)
		{
			s.push_back(make_pair(src[0], 1));
			break;
		}
		int count = 1;
		char cur, nxt;
		for (int i = 0; i < src.size(); i++)
		{
			cur = src[i];
			if (i + 1 == src.size())
			{
				s.push_back(make_pair(cur, count));
				break;
			}
			nxt = src[i + 1];
			if (cur == nxt)
				count++;
			else
			{
				s.push_back(make_pair(cur, count));
				count = 1;
			}
		}
		break;
	}


	string result = "";
	for (int i = 0; i < s.size(); i++)
		result += s[i].first;
	return result;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	int count = 0;
	while (T--)
	{
		if (count != 0)
			cout << endl;		
		count++;
		cout << "Case #" << count << ": ";
		
		int N;
		cin >> N;
		vector<string> strs(N);
		for (int i = 0; i < N; i++)
			cin >> strs[i];
		int min = 100000000;
		for (int i = 0; i < N; i++)
		{
			int result = 0;
			for (int j = 0; j < N; j++)
			{
				if (j == i) continue;
				int r = match(strs[i], strs[j]);
				if (r == -1)
				{
					result = 100000000;
					break;
				}
				else
					 result +=r;
			}
			if (min > result)
				min = result;
		}
	
		int result = 0;
		string x = prune(strs[0]);
		for (int j = 0; j < N; j++)
		{
			
			int r = match(x, strs[j]);
			if (r == -1)
			{
				result = 100000000;
				break;
			}
			else
				result += r;
		}
		if (min > result)
			min = result;

		if (min == 100000000)
			cout << "Fegla Won";
		else
		cout << min;
		
		

	}
	return 0;
}