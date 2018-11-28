#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <ctype.h>
#include <complex>
#include <cassert>
#include <ctime>
using namespace std;
#define fill(x,v) memset(x,v,sizeof x)
#define MP make_pair
#define x first
#define y second
#define sz(s) int((s).size())
#define pb push_back
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef long long ll;
typedef unsigned long long ull;
template<class T> T sqr(T x) {return x * x;}
template<class T> T abs(T x) {return (x < 0) ? -x : x;}
const double EPS = 1e-18;
const int INF = 1010*1000*1000;

const int nmax = 39;

const int saf[nmax] =
{
	1,
	4,
	9,
	121,
	484,
	10201,
	12321,
	14641,
	40804,
	44944,
	1002001,
	1234321,
	4008004,
	100020001,
	102030201,
	104060401,
	121242121,
	123454321,
	125686521,
	400080004,
	404090404,
	10000200001,
	10221412201,
	12102420121,
	12345654321,
	40000800004,
	1000002000001,
	1002003002001,
	1004006004001,
	1020304030201,
	1022325232201,
	1024348434201,
	1210024200121,
	1212225222121,
	1214428244121,
	1232346432321,
	1234567654321,
	4000008000004,
	4004009004004
};

int main () {
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int testCount;
	ll a, b;
	cin >> testCount;
	for (int t = 0; t < testCount; t++)
	{
		cin >> a >> b;
		int ans = 0;
		for (int i = 0; i < nmax; i++)
		{
			if (saf[i] >= a && saf[i] <= b)
			{
				ans++;
			}
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
	
	
	return 0;
}

