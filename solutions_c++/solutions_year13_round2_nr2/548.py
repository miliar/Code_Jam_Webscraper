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
int T=12;
const int XXX = 10001;
int a[20 * 1000 + 41][10 * 1000 + 41];
bool solve()
{
	int n;
	int X,Y;
	cin >> n >> X >> Y;
	int m = (1 << n);
	int cnt1 = 0;
	int cnt2 = 0;
	X += XXX;
	for (int msk = 0; msk < m; ++ msk)
	{
		++ T;
		for (int i = 0; i < n; ++ i)
		{
			int x = XXX, y = 2 * i;
			while (y > 0 && a[x][y - 2] != T)
			{
				y -= 2;
			}

			while (y > 0)
			{
				int pos = 0;
				if (a[x - 1][y - 1] != T)
					pos |= 1;
				if (a[x + 1][y - 1] != T)
					pos |= 2;
				if (pos == 0)
					break;
				if (pos == 3)
					pos &= ((msk >> i) & 1);
				if (pos & 1)
					x --;
				else
					x ++;
				y --;
			}
			a[x][y] = T;
		}
		cnt2 ++;
		if (a[X][Y] == T)
			cnt1++;
	}

	printf("%.10lf", (double)cnt1 / (double)cnt2);

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
	while (solve())
	{
	
	}
	cerr << "Case #" << i + 1 << ": " << clock() << endl;
	cout << endl;
}
	return 0;
}
