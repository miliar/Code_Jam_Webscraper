#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <iostream>
#include <cstring>
#include <string>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<vi> vvi;
typedef set<int> si;
typedef vector<si> vsi;

const int inf = 1e9;
const int mod = 1e9 + 7;
const long long P = 31;

void solve(int number)
{
	int a, b, k;
	scanf("%d%d%d", &a, &b, &k);
	int ans = 0;
	for (int i = 0; i < a; ++i)
	{
		for (int j = 0; j < b; ++j)
		{
			if ((i & j) < k)
				ans++;
		}
	}
	printf("Case #%d: %d\n", number, ans);
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
		solve(i + 1);
	return 0;
}