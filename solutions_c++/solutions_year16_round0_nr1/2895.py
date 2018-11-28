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


LL t, n;
int was[100], cnt;

void mark(LL x)
{
	while (x)
	{
		if (!was[x % 10]) was[x % 10] = 1, cnt++;
		x /= 10;
	}
}


int main()
{
    freopen(fname"in", "r", stdin);
    freopen(fname"out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> t;
    for (int i = 1; i <= t; i++)
    {
    	cin >> n;
    	cnt = 0;
    	for (int x = 0; x < 10; x++)
    		was[x] = 0;
    	for (int x = 1; x <= 1000000; x++)
    	{
    		mark(x * n);
    		if (cnt == 10)
    		{
    			out(i, x * n);
    			break;
    		}
    	}
    	if (cnt != 10)
    		out(i, "INSOMNIA");
    }
}