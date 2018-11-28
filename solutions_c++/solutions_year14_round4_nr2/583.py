#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int solve(const vector<int> & v)
{
	int cnt = 0;
	for (int i = 1; i < v.size(); i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (v[j] < v[i])
				cnt++;
		}
	}
	return cnt;
}

void insertAll(vector<int> &v, vector<int>::iterator& begin, vector<int>::iterator& end)
{
	while(begin != end)
	{
		v.push_back(*begin);
		begin++;
	}
}

bool works(const vector<int> & v)
{
	int inversions = 0;
	bool increasing = true;
	for (int i = 1; i < v.size(); i++)
	{
		if (!increasing && v[i] > v[i - 1])
			return false;
		if (increasing && v[i] < v[i - 1])
		{
			increasing = false;
		}
	}
	return true;
}

int bruteForce1(const vector<int> & v)
{
	set<vector<int> > visited;
	visited.insert(v);
	queue<pair<vector<int>, int> > toProcess;
	if (works(v))
		return 0;
	toProcess.push(make_pair(v, 0));

	pair<vector<int>, int> cur;
	while (!toProcess.empty())
	{
		cur = toProcess.front();
		toProcess.pop();

		for (int i = 1; i < cur.first.size(); i++)
		{
			swap(cur.first[i], cur.first[i - 1]);
			if (visited.find(cur.first) == visited.end())
			{
				if (works(cur.first))
					return cur.second + 1;
				visited.insert(cur.first);
				toProcess.push(make_pair(cur.first, cur.second + 1));
			}
			swap(cur.first[i], cur.first[i - 1]);
		}
	}
	return -1;
}
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	/*vector<int> v1;
	v1.push_back(1);
	v1.push_back(2);
	v1.push_back(4);
	v1.push_back(3);
	v1.push_back(1);
	cerr << works(v1) << endl;*/
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n;
		cin >> n;
		vector<int> v(n);
		int maxm = -1;
		int maxidx = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> v[i];
			if (v[i] > maxm)
			{
				maxm = v[i];
				maxidx = i;
			}

		}

		vector<int> input = v;
		//int bruteForce = bruteForce1(v);

		int best = 0;
		for (int i = 0; i < n; i++)
		{
			int minm = 1 << 30;
			int minidx = 0;
			for (int j = 0; j < v.size(); j++)
			{
				if (v[j] < minm)
				{
					minm = v[j];
					minidx = j;
				}
			}
			best += min(minidx, (int)v.size() - minidx - 1);
			v.erase(v.begin() + minidx);

		}
		/*v.erase(v.begin() + maxidx);
		int best = 1 << 30;
		bool decreased = false;
		for (int i = 0; i < n; i++)
		{
			vector<int> first;
			vector<int> second;
			if (i == 0)
			{
				insertAll(second, v.begin(), v.end());
			} else if (i == n - 1)
			{
				insertAll(first, v.begin(), v.end());
			} else
			{
				insertAll(first, v.begin(), v.begin() + i);
				insertAll(second, v.begin() + i, v.end());
			}
			
			reverse(first.begin(), first.end());
			int res = solve(first) + solve(second);
			res += abs(maxidx - i);
			best = min(best, res);
		}*/


		/*if (bruteForce != best)
		{
			cerr << "Result calculated to be: " << best << " when it actually is: " << bruteForce << endl;
			cerr << "For array:";
			for (int i = 0; i < n; i++)
			{
				cerr << " " << input[i];
			}
			cerr << endl;
		}*/
		cout << best << endl;

	}
	return 0;
}
