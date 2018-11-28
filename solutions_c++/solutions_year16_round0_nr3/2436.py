//Solution by Zhusupov Nurlan
#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>

using namespace std;

typedef long long LL;
typedef map<string , int> MSI;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define endl '\n'
#define pb(x) push_back(x)
#define sqr(x) ((x) * (x))
#define F first
#define S second
#define SZ(t) ((int) t.size())
#define len(t) ((int) t.length())
#define base LL((1ll << 30) + 1)
#define fname ""
#define sz 1000 * 1000
#define EPS (1e-8)
#define INF ((int)1e9 + 9)
#define mp make_pair

void out(int i, LL x)
{
	cout << "Case #" << i << ": " << x << "\n";
}
void out(int i, string x)
{
	cout << "Case #" << i << ": " << x << "\n";
}

LL n, t;
map <LL, LL> was;
LL ans[1000];

LL gen(LL n)
{
	LL x = 1;
	for (int i = 2; i < n; i++)
	{
		x = x * 10 + rand() % 2;
	}
	return x * 10 + 1;
}

LL f(LL r, LL x)
{
	LL res = 0, p = 1;
	for (int i = 1; i <= n; i++)
	{
		res = res + p * (x % 10);
		x /= 10;
		p *= r;
	}
	return res;
}

LL divisor(LL x)
{
	for (LL p = 2; p * p <= x; p++)
	{
		if (x % p == 0)
			return p;
	}	
	return 0;
}

int main()
{
    freopen(fname"in", "r", stdin);
    freopen(fname"out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> t;
    srand(322 + 228 + 1337);

    int j;
    for (int q = 1; q <= t; q++)
    {
    	cin >> n >> j;
    	LL x, p = 0;
		while (p < j)
		{
			while (was[x = gen(n)]);
			was[x] = 1;

			LL X = x, r = 0;
			int pr = 0;
			for (int j = 2; j <= 10; j++)
			{
				x = f(j, X);
				if (!divisor(x))
					pr = 1;
		  	}

		  	//cerr << X << " " << pr << endl;
		  	if (!pr)
		  		ans[p++] = X;
		}

		out(1, "");
		for (int i = 0; i < p; i++)
		{
			LL X = ans[i], r = 0;
			cout << X << " ";
			for (int j = 2; j <= 10; j++)
			{
				x = f(j, X);
				cout << divisor(x) << " ";
		  	}
			cout << "\n";
		}
    }
}