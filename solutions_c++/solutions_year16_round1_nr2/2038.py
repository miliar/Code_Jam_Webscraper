/*
* @problem: Rank and File
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
#define bitcnt(x) __builtin_popcount(x)
#define MS0(x) memset(x, 0, sizeof(x))
#define MS1(x) memset(x, -1, sizeof(x))
#define ll long long int
#define mp(x, y) make_pair(x, y)
#define pii pair<int, int>
#define pll pair<ll, ll>
#define in(x) scanf("%lld", &x)
#define ind(x) scanf("%d", &x)
#define ins(x) scanf("%s", x)
#define pi acos(-1.0)

using namespace std;
int x, ans[55], idx[105], sidx[105];
vector<int> s[105];
bool vis[105];

int main()
{
	// #ifndef ONLINE_JUDGE
	// 	freopen("../input.txt", "r", stdin);
	// #endif
	ios_base::sync_with_stdio(0);
    cin.tie(0);
	int t, n, m, pos, pos1;
	cin >> t;
	for(int a = 1; a <= t; a++)
	{
		cin >> n;
		m = 2 * n - 1;
		for(int i = 0; i < m; i++)
		{
			s[i].clear();
			for(int j = 0; j < n; j++)
			{
				cin >> x;
				s[i].push_back(x);
			}
		}
		//sort(s, s + m);
		int m1, m2, p1, p2, tmp = 0;
		MS0(vis);
		for(int i = 0; i < n; i++)
		{
			m1 = MAX;
			m2 = MAX;
			for(int j = 0; j < m; j++)
			{
				if(vis[j])
					continue;
				if(s[j][i] < m1)
				{
					m2 = m1;
					p2 = p1;
					m1 = s[j][i];
					p1 = j;
				}
				else if(s[j][i] < m2)
				{
					m2 = s[j][i];
					p2 = j;
				}
			}
			// cout << m1 << " " << m2 << endl;
			if(m1 == m2)
			{
				vis[p1] = vis[p2] = 1;
				idx[p1] = tmp++;
				idx[p2] = tmp++;
			}
			else
			{
				pos = p1;
				pos1 = i;
				vis[p1] = 1;
				idx[p1] = tmp++;
			}
			// cout << p1 << " " << p2 << endl;
		}

		for(int i = 0; i < m; i++)
		{
			for(int j = 0; j < m; j++)
			{
				if(idx[j] == i)
				{
					sidx[i] = j;
					break;
				}
			}
		}
		//cout << pos << " " << pos1 << endl;
		// for(int i = 0; i < m; i++)
		// {
		// 	for(int j = 0; j < s[idx[i]].size(); j++)
		// 		cout << s[sidx[i]][j] << " ";
		// 	cout << endl;
		// }
		// bool flag = 0;
		// for(int i = 0, j = 0; i < n, j < m - 1; i++, j += 2)
		// {
		// 	if(s[idx[j]][i] != s[idx[j + 1]][i])
		// 	{
		// 		pos = j;
		// 		pos1 = i;
		// 		flag = 1;
		// 		break; 
		// 	}
		// }
		// if(!flag)
		// {
		// 	pos = m - 1;
		// 	pos1 = n - 1;
		// }

		ans[pos1] = s[pos][pos1];
		int i = idx[pos] - 1, j = pos1 - 1;
		while(i > 0)
		{
			if(s[sidx[i]][pos1] != s[pos][j])
				ans[j] = s[sidx[i]][pos1];
			else
				ans[j] = s[sidx[i - 1]][pos1];
			i -= 2;
			j--;
		}
		i = idx[pos] + 1;
		j = pos1 + 1;
		while(i < m)
		{
			if(s[sidx[i]][pos1] != s[pos][j])
				ans[j] = s[sidx[i]][pos1];
			else
				ans[j] = s[sidx[i + 1]][pos1];
			i += 2;
			j++;
		}
		cout << "Case #" << a << ": ";
		for(i = 0; i < n; i++)
		{
			cout << ans[i] << " ";
		}
		cout << endl;
	}
	return 0;
}