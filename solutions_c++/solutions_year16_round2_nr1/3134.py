/*
* @problem: Getting the Digits
*/

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <bitset>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define MAX 100100
#define mod 1000000007LL
#define bitcnt(x) __builtin_popcountll(x)
#define MS0(x) memset(x, 0, sizeof(x))
#define MS1(x) memset(x, -1, sizeof(x))
#define ll long long int
#define mp(x, y) make_pair(x, y)
#define pii pair<int, int>
#define pll pair<ll, ll>
#define in(x) scanf("%lld", &x)
#define ind(x) scanf("%d", &x)
#define ins(x) scanf("%s", x)
#define pr(x) printf("%lld\n", x)
#define prd(x) printf("%d\n", x)
#define prs(x) printf("%s\n", x)
#define pi acos(-1.0)
#define ff first
#define ss second

using namespace std;

int main()
{
	// ios_base::sync_with_stdio(0);
	// cin.tie(0);
	int t, l, cnt[27], c, p[30];
	char s[2005], no[10][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	bool vis[2005];
	vector<int> v;
	ind(t);
	for (int k = 1; k <= t; k++)
	{
		ins(s);
		l = strlen(s);
		v.clear();
		MS0(cnt);
		c = l;
		for (int i = 0; i < l; i++)
		{
			cnt[s[i] - 'A']++;
		}
		printf("Case #%d: ", k);
		bool ans = 1;
		while (c > 0 && ans)
		{
			bool flag;
			ans = 0;
			int tmp[] = {0, 2, 4, 6, 8};
			for (int a = 0; a < 5; a++)
			{
				int i = tmp[a];
				flag = 0;
				MS0(p);
				for (int j = 0; no[i][j] != '\0'; j++)
				{
					if (cnt[no[i][j] - 'A'] <= p[no[i][j] - 'A'])
					{
						flag = 1;
						break;
					}
					p[no[i][j] - 'A']++;
				}
				if (!flag)
				{
					for (int j = 0; no[i][j] != '\0'; j++)
					{
						cnt[no[i][j] - 'A']--;
						c--;
					}
					v.push_back(i);
					ans = 1;
				}
			}
		}
		ans = 1;
		while (c > 0 && ans)
		{
			bool flag;
			ans = 0;
			int tmp[] = {1, 3, 5};
			for (int a = 0; a < 3; a++)
			{
				int i = tmp[a];
				flag = 0;
				MS0(p);
				for (int j = 0; no[i][j] != '\0'; j++)
				{
					if (cnt[no[i][j] - 'A'] <= p[no[i][j] - 'A'])
					{
						flag = 1;
						break;
					}
					p[no[i][j] - 'A']++;
				}
				if (!flag)
				{
					for (int j = 0; no[i][j] != '\0'; j++)
					{
						cnt[no[i][j] - 'A']--;
						c--;
					}
					v.push_back(i);
					ans = 1;
				}
			}
		}
		while (c > 0)
		{
			bool flag;
			ans = 0;
			int tmp[] = {7, 9};
			for (int a = 0; a < 2; a++)
			{
				int i = tmp[a];
				flag = 0;
				MS0(p);
				for (int j = 0; no[i][j] != '\0'; j++)
				{
					if (cnt[no[i][j] - 'A'] <= p[no[i][j] - 'A'])
					{
						flag = 1;
						break;
					}
					p[no[i][j] - 'A']++;
				}
				if (!flag)
				{
					for (int j = 0; no[i][j] != '\0'; j++)
					{
						cnt[no[i][j] - 'A']--;
						c--;
					}
					v.push_back(i);
					//ans = 1;
				}
			}
		}
		sort(v.begin(), v.end());
		for(int i = 0; i < v.size(); i++)
			printf("%d", v[i]);
		printf("\n");
	}
	return 0;
}