#pragma warning(disable: 4996)
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>
#include <exception>
#include <functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define fori(i,n) for (int i = 0; i < (n); ++ i)
#define forv(i,v) for (int i = 0; i < (sz(v)); ++ i)
typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	if (s == "input_txt")
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	else if (sz(s) != 0)
	{
		freopen((s + ".in").c_str(),"r",stdin);
		freopen((s + ".out").c_str(),"w",stdout);
	}
#endif
}
	

void read(vector< string > &a)
{
	string s;
	cin >> s;
	cin >> s;
	while (s != "}")
	{
		a.push_back(s.substr(1, sz(s) - 2));
		cin >> s;
	}
}
void read(string &s)
{
	cin >> s;
	s = s.substr(1, sz(s) - 2);
}

void read(vector< int > &a)
{
	string s;
	cin >> s;
	cin >> s;
	while (s != "}")
	{
		a.push_back(atoi(s.c_str()));
		cin >> s;
	}
}

const int MAXN = 104;
const int MAXV = 1000 * 1000 + 41;
int dp[MAXN][MAXV];
int was[MAXN][MAXV];
int T = 12;
int M = 1000 * 1000 + 2;
bool Upd(int i, int j, int val)
{
	if (dp[i][j] > val)
	{
		dp[i][j] = val;
		return true;
	}
	return false;
}


int newj(int j)
{
	if (j > M)
		j = M;
	return j;
}
bool solve()
{
	int start = 0;
	int n;
	cin >> start >> n;
	vector<int> a(n);
	for (int i = 0; i < n; ++ i)
		cin >> a[i];
	sort(all(a));
	_(dp, 60);

	Upd(0, start, 0);
	
	for (int i = 0; i < n; ++ i)
	{
		for (int j = 0; j < M; ++ j)
		{
			Upd(i, newj(j * 2 - 1), dp[i][j] + 1);
			if (j > a[i])
				Upd(i + 1, newj(j + a[i]), dp[i][j] + 0);
			Upd(i + 1, j, dp[i][j] + 1);
		}
	}

	cout << *min_element(dp[n], dp[n] + MAXV);

	return false;
}

int main()
{
	prepare("input_txt");

	int T;
cin >> T;
for (int i = 0; i < T; ++ i)
{
	cout << "Case #" << i + 1 << ": ";
	cerr << "Case #" << i + 1 << ": " << clock() << endl;
	while (solve())
	{
	
	}
	cout << endl;
}
	return 0;
}
