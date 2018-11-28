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


void solve()
{
	int a, b, k;
	cin >> a >> b >> k;
	int ans = 0;
	for(int i = 0; i < a; i++)
		for(int j = 0; j < b; j++)
		{
			int c = i & j;
			//cout << i << ' ' << j << ' ' << c << endl;
			if(c < k)
				ans++;
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