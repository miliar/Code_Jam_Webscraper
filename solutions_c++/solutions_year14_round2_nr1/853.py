#pragma comment(linker, "/STACK:167177216")

#include <stdio.h>
#include <stack>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <time.h>
#include <cassert>
//#include <unordered_map>

using namespace std;

#define mp make_pair
#define pb push_back
#define pii pair<int, int>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define x first
#define y second

typedef long long li;
typedef long double ld;
typedef unsigned long long uli;

const int INF = 1e9;
const ld eps = 1e-8;
const li mod = INF + 7;
const li INF64 = (li)(INF) * (li)(INF);

const int ddx[] = {-1, 1, 1, -1};
const int ddy[] = {1, 1, -1, -1};
const int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int dx4[] = {-1, 0, 1, 0};
const int dy4[] = {0, 1, 0, -1};
const int dxh[] = {-1, -1, -1, 1, 1, 1, 1, -1};
const int dyh[] = {1, -1, -1, -1, -1, 1, 1, 1};
const string dirs[] = {"RIGHT", "UP", "LEFT", "DOWN"};

string s[111];
vector<char> c[111];
vector<int> cnt[111];

void solve()
{
	int n;
	cin >> n;
	string enter;
	getline(cin, enter);
	for(int i = 1; i <= n; i++)
		getline(cin, s[i]), c[i].clear(), cnt[i].clear();

	//vector<char> c[3];
	for(int i = 1; i <= n; i++)
	{
		int cur = 1;
		c[i].pb(s[i][0]);
		for(int j = 1; j < s[i].length(); j++)
			if(s[i][j] != s[i][j - 1])
			{
				cnt[i].pb(cur);
				c[i].pb(s[i][j]);
				cur = 1;
			}
			else
			{
				cur++;
			}
		cnt[i].pb(cur);
	}

	/*cout << "cerr symbols " << endl;
	for(int i = 1; i <= n; i++)
	{
		forn(j, c[i].size())
			cout << c[i][j];
		cout << endl;
	}

	cout << "cerr cnts " << endl;
	for(int i = 1; i <= n; i++)
	{
		forn(j, cnt[i].size())
			cout << cnt[i][j] << ' ';
		cout << endl;
	}

	cout << "end cerr" << endl;*/

	bool ok = true;
	for(int i = 1; i <= n; i++)
		for(int j = i + 1; j <= n; j++)
		{
			if(c[i].size() != c[j].size())
			{
				cout << "Fegla Won" << endl;
				return;
			}

			for(int k = 0; k < c[i].size(); k++)
				if(c[i][k] != c[j][k])
				{
					cout << "Fegla Won" << endl;
					return;
				}
		}

	if(!ok)
	{
		cout << "Fegla Won" << endl;
		return;
	}

	int ans = 0;
	for(int k = 0; k < cnt[1].size(); k++)
	{
		int best = 1, mn = INF;
		for(int i = 1; i <= 100; i++)
		{
			int sum = 0;
			for(int j = 1; j <= n; j++)
				sum += abs(cnt[j][k] - i);
			if(sum < mn)
			{
				mn = sum;
				best = i;
			}
		}

		ans += mn;
	}

	cout << ans << endl;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //ios_base::sync_with_stdio(false);
	int tests;
	cin >> tests;
	forn(test, tests)
	{
		cout << "Case #" << test + 1 << ": ";
		solve();
	}
    return 0;
}