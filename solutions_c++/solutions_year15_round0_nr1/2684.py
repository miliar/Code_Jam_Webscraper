#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <list>

using namespace std;

#define pb push_back
#define fs first
#define sc second
#define sz(a) (int)a.size()
#define szs(s) (int)s.length() 
#define elif else if
#define mp make_pair

typedef long long ll;
typedef long double ld;

const int INF = 1000000009;
const ll INFL = 1759849216489136867ll;
const double eps = 1e-9;

#define NAME ""

void solve();

int main()
{
	clock_t t_start, t_end;
	
	#ifdef _GEANY
	assert(freopen("input.txt", "r", stdin));
	t_start = clock();
	#endif
	
	int t(0);
	cin >> t;
	
	for (int i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	
	#ifdef _GEANY
	t_end = clock();
	cerr.precision(3);
	cerr << fixed << (double)(t_end - t_start) / CLOCKS_PER_SEC << '\n';
	#endif
	
	return 0;
}

void solve()
{
	int n(0);
	
	cin >> n;
	
	getc(stdin);
	
	int sum(0), need(0);
	
	for (int i = 0; i <= n; ++i)
	{
		char c(0);
		c = getc(stdin);
		
		if (i > sum && c != 0)
		{
			need += i - sum;
			sum += i - sum;
		}
		sum += (c - '0');
	}
	
	cout << need << '\n';
}
