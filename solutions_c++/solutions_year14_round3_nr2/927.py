#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<vi> vvi;
typedef set<int> si;
typedef vector<si> vsi;
typedef vector<string> vs;
typedef pair<string, int> psi;
typedef vector<psi> vpsi;

const int inf = 1e9;
const int mod = 1e9 + 7;

void solve()
{
	int n, ans = 0;
	scanf("%d", &n);
	vpsi sets(n);
	for (int i = 0; i < n; ++i)
	{
		cin >> sets[i].first;
		sets[i].second = i;
	}
	sort(sets.begin(), sets.end());
	do
	{
		int uses[100] = {};
		string tmp = "";
		for (int i = 0; i < n; ++i)
			tmp += sets[i].first;
		bool check = true;
		for (int i = 0; i < tmp.size(); ++i)
		{
			int ind = tmp[i] - 'a';
			if (uses[ind])
			{
				if (tmp[i - 1] != tmp[i])
				{
					check = false;
					break;
				}
			}
			uses[ind] = 1;
		}
		ans += check;
	} 
	while (next_permutation(sets.begin(), sets.end()));
	printf("%d\n", ans);
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}