#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility> 
using namespace std;
 
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))
 
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define Pi 3.14159265358979

typedef long long Int;
typedef unsigned long long UINT;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 1000000000;
const int MAX = 20000;
const int MAX2 = 7000;
const int BASE = 1000000000;

int T, n, s;
int A[MAX];
multiset <int> S;

void Init()
{
	S.clear();
}

void SolveTest(int test)
{
	scanf("%d %d", &n, &s);
	FOR (i,0,n)
	{
		scanf("%d", &A[i]);
		S.insert(A[i]);
	}
	int res = 0;
	while (!S.empty())
	{
		++ res;
		int a = *S.rbegin();
		S.erase(S.find(a));
		if (!S.empty())
		{
			multiset<int>::iterator it = S.upper_bound(s-a);
			if (it != S.begin())
			{
				-- it;
				S.erase(it);
			}
		}
	}
	printf("Case #%d: %d\n", test+1, res);
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("A-large (1).in", "r", stdin);
		//freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif

	scanf("%d", &T);
	FOR (test,0,T)
	{
		Init();
		SolveTest(test);
	}

	return 0;
}