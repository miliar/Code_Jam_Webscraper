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

char CONSTANTS[] = "aeiou" ;

bool isconsonant(char c)
{
	for (int i = 0; i < 5; ++ i)
		if (CONSTANTS[i] == c)
			return false;
	return true;
}

bool solve()
{
	string s;
	int k;
	cin >> s;
	cin >> k;
	int n = sz(s);
	lint ans = 0;
	int cnt = 0;
	int last = -1;
	for (int i = 0;  i < n; ++ i)
	{
		if (isconsonant(s[i]))
			++ cnt;
		else
			cnt = 0;
		if (cnt >= k)
			last = i - k + 1;
		ans += last + 1;
	}
	cout << ans;
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
		cout << endl;
	}

	return 0;
}
