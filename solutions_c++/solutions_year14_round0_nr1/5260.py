#pragma comment(linker, "/STACK:167177216")

#include <stdio.h>
#include <stack>
#include <deque>
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
#include <bitset>
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
const ld eps = 1e-12;
const li mod = INF + 7;
const li INF64 = (li)(INF) * (li)(INF);

const int ddx[] = {-1, 1, 1, -1};
const int ddy[] = {1, 1, -1, -1};
const int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int dx4[] = {-1, 0, 1, 0};
const int dy4[] = {0, 1, 0, -1};
const int dxh[] = {-2, -2, -1, 1, 2, 2, 1, -1};
const int dyh[] = {1, -1, -2, -2, -1, 1, 2, 2};
const string dirs[] = {"RIGHT", "UP", "LEFT", "DOWN"};

set<int> s1, s2, s;
int n = 4;
int a[5][5], b[5][5];
int i1, i2;

void solve()
{
	s.clear();
	s1.clear();
	s2.clear();
	cin >> i1;
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= n; j++)
			cin >> a[i][j];
	cin >> i2;
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= n; j++)
			cin >> b[i][j];

	for(int j = 1; j <= n; j++)
		s1.insert(a[i1][j]);
	for(int j = 1; j <= n; j++)
		s2.insert(b[i2][j]);
	for(set<int>::iterator it = s1.begin(); it != s1.end(); it++)
	{
		int val = *it;
		if(s2.find(val) != s2.end())
			s.insert(val);
	}

	if(s.size() == 1)
	{
		cout << *s.begin() << endl;
		return;
	}

	if(s.empty())
	{
		cout << "Volunteer cheated!" << endl;
		return;
	}

	cout << "Bad magician!" << endl;
	return;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
	int tests;
	cin >> tests;
	forn(test, tests)
	{
		cout << "Case #" << test + 1 << ": ";
		solve();
	}
	return 0;
}
