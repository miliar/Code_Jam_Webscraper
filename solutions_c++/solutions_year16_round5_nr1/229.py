#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<numeric>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<set>
#include<map>
#include<unordered_map>
#include<unordered_set>
#include<list>
#include<cmath>
#include<bitset>
#include<cassert>
#include<queue>
#include<stack>
#include<deque>
#include<cassert>
using namespace std;
typedef long long ll;
typedef long double ld;
const int MAXN = 20 * 1000 + 7;
char a[MAXN];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%s", a);
		vector<char>st;
		int n = strlen(a);
		int res = 0;
		for (int i = 0; i < n; i++)
		{
			if (!st.empty() && st.back() == a[i])
			{
				res += 10;
				st.pop_back();
			}
			else
			{
				st.push_back(a[i]);
			}
		}
		while ((int)st.size() >= 2)
		{
			res += 5;
			st.pop_back();
			st.pop_back();
		}
		printf("Case #%d: %d\n", tt, res);
	}
}