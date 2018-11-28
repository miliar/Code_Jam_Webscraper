#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE 
#include <iostream> 
#include <cstdio> 
#include <cstdlib> 
#include <vector> 
#include <sstream> 
#include <string> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <iomanip> 
#include <functional> 
#include <bitset> 
#include <cassert> 
#include <cmath> 
#include <ctime> 
#include <queue> 
#include <list> 
#include <memory.h> 
#include <complex> 
#include <numeric> 
using namespace std; 
#pragma comment(linker, "/STACK:256000000") 
#define mp make_pair 
#define pb push_back 
#define all(C) (C).begin(), (C).end() 
#define sz(C) (int)(C).size() 
#define PRIME 1103 
#define INF ((1ll << 60) - 1) 
#define MOD 1000000007 
#define FAIL ++*(int*)0 
#define EPS 1e-11 
template<class T> T sqr(T a) {return a * a;} 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef pair<int, pii> piii; 
typedef vector<int> vi; 
typedef vector<int64> vi64; 
typedef vector<pii> vpii; 
typedef vector<vector<int> > vvi; 
typedef vector<vvi> vvvi; 
typedef vector<vector<pair<int, int > > > vvpii; 
typedef vector<vector<vector<pair<int, int > > > > vvvpii; 
typedef complex<long double> cd; 
#define TASK "hobbit" 
//---------------------------------------------------------- 

const int MAXN = 10;
int n;
int a[MAXN], b[MAXN];

void read(int a[])
{
	for(int i = 0; i < n; ++i)
	{
		string s;
		cin >> s;
		while(s.length() < 7)
			s += "0";
		a[i] = atoi(s.substr(2).c_str());
	}
}

void print(int a[])
{
	for(int i = 0; i < n; ++i)
		cerr << a[i] << " ";
	cerr << endl;
}

void init()
{
	scanf("%d\n", &n);
	read(a);
	read(b);
}

int dp[1 << MAXN][1 << MAXN];

int rec(int mask1, int mask2)
{
	if(mask1 == (1 << n) - 1)
		return 0;

	if(dp[mask1][mask2] != -1)
		return dp[mask1][mask2];

	int res = 0;
	for(int i = 0; i < n; ++i)
	{
		if(mask1 & (1 << i)) 
			continue;
		for(int j = 0; j < n; ++j)
		{
			if(!(mask2 & (1 << j))) 
				res = max(res, rec(mask1 | (1 << i), mask2 | (1 << j)) + (a[i] > b[j]));
		}
	}
	return dp[mask1][mask2] = res;
}

int solve1()
{
	memset(dp, -1, sizeof dp);
	return rec(0, 0);
}

bool was[MAXN];
int solve2()
{
	int res = 0;
	memset(was, 0, sizeof was);

	sort(a, a + n);
	sort(b, b + n);

	for(int i = 0; i < n; ++i)
	{
		int ind = -1;
		for(int j = 0; j < n; ++j)
		{
			if(!was[j] && b[j] > a[i])
			{
				ind = j;
				break;
			}
		}
		if(ind == -1)
		{
			for(int j = 0; j < n; ++j)
			{
				if(!was[j])
				{
					ind = j;
					break;
				}
			}
		}
		was[ind] = 1;

		res += a[i] > b[ind];
	}
	return res;
}

int main() 
{ 
#ifndef ONLINE_JUDGE 
    freopen ("input.txt", "r", stdin); freopen ("output.txt", "w", stdout); 
#endif 
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; ++i)
    {
    	init();
    	printf("Case #%d: %d %d\n", i + 1, solve1(), solve2());
    }
    return 0; 
}