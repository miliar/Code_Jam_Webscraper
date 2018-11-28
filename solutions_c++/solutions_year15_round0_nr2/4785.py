#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

map<vector<int>, int> mp;

int go(vector<int> v)
{
	if(v.empty())
		return 0;
	map<vector<int>, int>::iterator it = mp.find(v);
	if(it != mp.end())
	{
		return it->second;
	}

	int res = 1000000000;

	int n = v.size();
	for(int i=0;i<n;i++)
	{
		for(int cut = 1; cut < v[i]; cut++)
		{
			vector<int> v2 = v;
			v2[i] -= cut;
			v2.push_back(cut);
			sort(v2.begin(), v2.end());
			int curr = go(v2) + 1;
			if (curr < res)
				res = curr;
		}
	}

	vector<int> v3;
	for(int i=0;i<n;i++)
	{
		if (v[i] != 1)
		{
			v3.push_back(v[i]-1);
		}
	}
	int cand = go(v3)+1;
	if(cand < res)
		res = cand;
	
	mp[v] = res;
	return res;
}

void solve()
{
	mp.clear();
	vector<int> v;
	int d;
	scanf("%d", &d);
	for(int i=0; i<d; i++)
	{
		int x;
		scanf("%d", &x);
		v.push_back(x);
	}
	sort(v.begin(), v.end());
	printf("%d\n", go(v));
}

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tst=0;tst<t;tst++)
	{
		printf("Case #%d: ", tst+1);
		solve();
	}
	return 0;
}