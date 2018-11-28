#pragma comment(linker, "/STACK:1000000000")
#define _CRT_SECURE_NO_WARNINGS
#include "iostream"
#include <cstdio>
#include "vector"
#include "cmath"
#include "algorithm"
#include "string"
#include "cstring"
#include "cstdlib"
#include "fstream"
#include "stack"
#include "bitset"
#include "queue"
#include "map"
#include "set"
#include <ctime>

using namespace std;
#define REP(i,b) for(int i=0; i<b;i++)
#define FOR(i,a,b) for(int i=a; i<=b;i++)
#define mp make_pair
#define pb push_back
#define X  first
#define Y  second
#define eps 0.000000001
typedef long long LL;
typedef unsigned long long ULL;
const int size = 10000010;
const LL alphabet = 130;
const LL INF =  1000000000;
const double pi = 4 * atan(1.0);
const LL MOD = 1000000007;

LL n, m, k, t, p, q;

int lawn[105][105];

bool check (int a, int b, int val)
{
	int ans = 2;
	FOR(i,1,n)
		if (lawn[i][b] > val)
		{
			--ans;
			break;
		}
	FOR(i,1,m)
		if (lawn[a][i] > val)
		{
			--ans;
			break;
		}
	if (!ans)
		return 0;
	return 1;
}

int main()
{
	#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//	double start = clock();
	#endif
	cin >> t;
	int a;
	REP(k,t)
	{
		memset(lawn,0,sizeof(lawn));
		cin >> n >> m;
		int mix = 0;
		REP(i,n)
			REP(j,m)
		{
			scanf("%d", &a);
			if (a > mix)
				mix = a;
			lawn[i+1][j+1] = a;
		}
		if(n == 1 || m == 1)
		{
			printf("Case #%d: YES\n", k+1);
			continue;
		}
		bool lol = 1;
		FOR(i,1,n)
			if (lol)
			FOR(j,1,m)
			{
				int val = lawn[i][j];
				if (!check(i,j,val))
				{
					printf("Case #%d: NO\n", k+1);
					lol = 0;
					break;
				}
			}
			else break;
		if (lol)
			printf("Case #%d: YES\n", k+1);
	}


	return 0;
}