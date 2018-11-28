#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int case1(vector<int>& v)
{
	int total = 0;
	for(int k = 0; k < v.size() -1; k++)
	{
		int diff = v[k] - v[k+1];
		if(diff > 0) total += diff;
	}
	return total;
}

int case2(vector<int>& v)
{
	int maxdiff = 0;
	for(int k = 0; k < v.size() - 1; k++)
	{
		int diff = v[k] - v[k+1];
		if(diff > maxdiff) maxdiff = diff;
	}
	int total = 0;
	for(int k = 0; k < v.size() - 1; k++)
	{
		//int diff = v[k] - v[k+1];
		//total += diff < maxdiff ? maxdiff : diff;
		total += v[k] < maxdiff ? v[k] : maxdiff;
	}
	return total;
}

int main()
{
	int t, n;
	cin >> t;
	for(int k = 1; k <= t; k++)
	{
		cin >> n;
		vector<int> v;
		while(n--)
		{
			int y; cin >> y; v.push_back(y);
		}
		printf("Case #%d: %d %d\n", k, case1(v), case2(v));
	}
}