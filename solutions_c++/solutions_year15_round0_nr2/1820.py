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
#include <cmath> 
#include <cstring> 
#include <queue>
using namespace std; 
#pragma comment(linker, "/STACK:256000000") 
#define mp make_pair 
#define pb push_back 
#define all(C) (C).begin(), (C).end() 
#define sz(C) (int)(C).size() 
#define PRIME 1103 
#define PRIME1 31415 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef vector<int> vi; 
typedef vector<vector<int> > vvi; 
//------------------------------------------------------------ 
const int N = 317;
int mas[1000];

int solve()
{
	int d;
	scanf("%d", &d);
	for(int i = 0; i < d; ++i)
		scanf("%d", &mas[i]);
	int bans = 1000;
	for(int i = 1; i <= 1000; ++i)
	{
		int tans = 0;
		for(int j = 0; j < d; ++j)
		{
			tans += mas[j] / i - 1;
			if (mas[j] % i)
				tans++;
		}
		bans = min(tans + i, bans);
	}
	return bans;
}

int main() 
{
#ifdef WIN32
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		printf("Case #%d: %d\n", i + 1, solve());
	}
}