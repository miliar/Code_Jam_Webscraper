//#define Testing

#define FileIO

#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <time.h>
#include <bitset>
#include <functional>

using namespace std;

#define ABS(a) ((a<0)?-(a):a)
#define MIN(a, b) ((a<b)?a:b)
#define MAX(a, b) ((a>b)?a:b)
#define FOR(i,a,n) for ( int i = (a); i < (n); ++i)
#define FORI(s, n) for(LL i=s; i<n; i++)
#define mp(a, b) make_pair(a, b)
typedef long long LL;

double eps = 0.00000001;
const LL INF = 1000000009;
const LL MAXNUM = 1024;
const LL MOD = 1000000007;

LL poww(LL v, LL p)
{
	if (p == 0) return 1;

	if (p & 1)
	{
		return (poww(v, p - 1) * v) % MOD;
	}
	else
	{
		LL t = poww(v, p / 2);
		return (t * t) % MOD;
	}
}

LL t, res;
int l = 0;
string S;

int main()
{

#ifdef FileIO
	freopen("COME_HERE.txt", "r", stdin);
	freopen("GO_AWAY.txt", "w", stdout);
#endif // FileIO
#ifdef Testing
	clock_t Start = clock();
#endif // Testing
	//----------------------------------------	

	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> S;
		l = S.size();
		res = 1;
		for (int k = 1; k < l; k++)
		{
			if (S[k] != S[k - 1])
				res++;
		}
		if (S[l - 1] == '+')
			res--;

		cout << "Case #" << i << ": " << res << endl;
	}

	//----------------------------------------
#ifdef Testing
	cout << "\nTime: " << clock() - Start << endl;
#endif // Testing

	return 0;
}