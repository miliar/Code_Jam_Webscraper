#if 1
#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <list>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;

const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;

#define mp make_pair
#define pb push_back
#define X first
#define Y second

#define dbg(x) { cerr << #x << " = " << x << endl; }

// extended template
#pragma comment(linker, "/STACK:36777216")
typedef vector<int> vi;
typedef vector<vi> vvi;


#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;

#define NAME "problem"


int solve(vector <vector <int> > &a)
{
	int n = a.size();
	int m = a[0].size();
	vector <vector <int> > b(n, vector <int> (m, 100));
	for (int i = 0; i < n; i++)
	{
		int ma = *max_element(a[i].begin(), a[i].end());
		for (int k = 0; k < m; k++)
			b[i][k] = min(b[i][k], ma);
	}

	for (int k = 0; k < m; k++)
	{
		int mi = inf;
		for (int i = 0; i < n; i++)
		{
			if (a[i][k] != b[i][k])
				mi = min(mi, a[i][k]);
		}
		for (int i = 0; i < n; i++)
			b[i][k]	= min(b[i][k], mi);
	}
	return (b == a);
}

int main()
{
	START
	freopen("B-large.in","r",stdin);freopen("output2.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int test = 1; test <= t; test++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		vector <vector <int> > a(n, vector <int> (m));
		for (int i = 0; i < n; i++)
			for (int k = 0; k < m; k++)
				scanf("%d", &a[i][k]);
		int ans = solve(a);
		printf("Case #%d: ", test);
		if (ans)
			printf("YES\n");
		else
			printf("NO\n");
	}
	END
    return 0;
}
/*******************************************
*******************************************/
#endif