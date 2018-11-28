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

LL n, m, k;
LL d[size], ans[size];
LL tmp;

bool ispal(LL n)
{
	if (n % 10 == 0)
		return 0;
	LL a1,a2 = 0;
	LL i=0;
	a1 = n;
	while(n)
	{
		tmp = n % 10;
		if (i)
			a2 *= 10;
		a2 += tmp;
		n /= 10;
		++i;
	}
	if (a2 == a1)
		return 1;
	return 0;
}
int main()
{
	#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//	double start = clock();
	#endif
	//REP(i,size-1)
	for(LL i = 1; i < size; i++)
	{
		if (ispal(i))
			if  (ispal(i*i))
				d[i] = 1;
	}
	REP(i,size-1)
		if(i)
			ans[i] = ans[i-1]+d[i];
	cin >> n;
	LL l, r;
	LL res = 0;
	REP(k,n)
	{
		scanf("%I64d %I64d", &l, &r);
		LL x = sqrt((double)l);
		LL y = sqrt((double)r);
		if (x*x < l)
			x++;
		res = ans[y] - ans[x-1];
		printf("Case #%d: %I64d\n", k+1, res);
	}
	/*
	#ifdef _DEBUG
	printf("%.4lf\n", (clock() - start)/ CLOCKS_PER_SEC);
	#endif*/
	return 0;
}