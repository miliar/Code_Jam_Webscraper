#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm> 
#include <iostream> 
#include <string.h> 
#include <stdlib.h> 
#include <sstream> 
#include <fstream>
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
#define Int long long 
#define INF 0x3F3F3F3F 
#define eps 1e-9
using namespace std;

bool isValid(vector<int> a)
{
	int i, j;
	for (i = 0; i < a.size(); i++)
	{
		bool ok = true;
		for (j = 1; j <= i; j++) {
			if (a[j] < a[j - 1]) {
				ok = false;
				break;
			}
		}
		for (j = i + 1; j < a.size(); j++) {
			if (a[j] > a[j - 1]) {
				ok = false;
				break;
			}
		}
		if (ok)
			return true;
	}
	return false;
}

int brute(vector<int> a)
{
	int n = a.size(), i, j;
	map<vector<int>, int> d;
	d[a] = 0;
	queue<vector<int> > q;
	q.push(a);
	while (q.size())
	{
		auto t = q.front();
		q.pop();
		if (isValid(t))
			return d[t];
		for (i = 1; i < n; i++)
		{
			auto s = t;
			swap(s[i], s[i - 1]);
			if (!d.count(s))
			{
				q.push(s);
				d[s] = d[t] + 1;
			}
		}
	}
	return 0;
}

int inc(vector<int> a)
{
	int res = 0;
	for (int i = 0; i < a.size(); i++)
	{
		auto pos = min_element(a.begin() + i, a.end()) - a.begin();
		int val = a[pos];
		res += pos - i;
		a.erase(a.begin() + pos);
		a.insert(a.begin() + i, val);
	}
	return res;
}

int solve(vector<int> A)
{
	int n = A.size(), i, j;
	int res = 0;
	for (int k = 0; k < n; k++)
	{
		int mn = min_element(A.begin(), A.end()) - A.begin();
		res += min(mn, (int)A.size() - mn - 1);
		A.erase(A.begin() + mn);
	}
	//int mx = max_element(A.begin(), A.end()) - A.begin();
	//for (int pos = 0; pos < n; pos++)
	//{
	//	auto a = A;
	//	int tmp = a[mx];
	//	if (mx > pos)
	//	{
	//		for (i = mx; i > pos; i--)
	//			a[i] = a[i - 1];
	//	}
	//	else if (mx < pos)
	//	{
	//		for (i = mx; i < pos; i++)
	//			a[i] = a[i + 1];
	//	}
	//	a[pos] = tmp;
	//	int cur = abs(pos - mx);
	//	cur += inc(vector<int>(a.begin(), a.begin() + pos));
	//	reverse(a.begin() + pos, a.end());
	//	cur += inc(vector<int>(a.begin() + pos, a.end()));
	//	res = min(res, cur);
	//}
	return res;
}

int main()
{
	int tests, i, n;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		scanf("%d", &n);
		vector<int> a(n);
		for (i = 0; i < n; i++)
			scanf("%d", &a[i]);
		printf("Case #%d: %d\n", test, solve(a));
	}
}