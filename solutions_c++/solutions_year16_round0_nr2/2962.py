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
string s;

bool op()
{
	int i = 0, n = s.length();
	while (i < n && s[i] == s[0]) i++;
	if (i == n) return 0;
	for (int p = 0; p < i; p++)
   		if (s[p] == '+') s[p] = '-';
   			else s[p] = '+';
	return 1;
}



int main()
{
    freopen(fname"in", "r", stdin);
    freopen(fname"out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> t;
    for (int q = 1; q <= t; q++)
    {
    	int cnt = 0;
    	cin >> s;
    	while (op()) cnt++;
    	if (s[0] == '-') cnt++;
    	out(q, cnt);
    }
}