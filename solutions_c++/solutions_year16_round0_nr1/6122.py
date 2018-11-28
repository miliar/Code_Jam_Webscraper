#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <cassert>
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
#include <time.h>
#include <complex>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define RFOR(i,b,a) for(int i=(b)-1;i>=(a);--i)
#define FILL(A,val) memset(A,val,sizeof(A))

#define ALL(V) V.begin(),V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair

typedef long long Int;
typedef unsigned long long UInt;
typedef vector<int> VI;
typedef pair<int,int> PII;

const double Pi = acos(-1.0);
const int INF = 1000000000;
const int MAX = 1000007;
const int MAX2 = 2000000;
const int BASE = 10;
const int ST = 1000000007;
const int CNT = 100;

const int MOD = 1000000007;

bool A[10];

void Apply(Int x)
{
	while (x)
	{
		A[x % 10] = 1;
		x /= 10;
	}
}

int main()
{
	freopen("out.txt" , "w" , stdout);
	freopen("in.txt", "r", stdin);
	//freopen("puzzle.in", "r", stdin);
	//freopen("puzzle.out", "w", stdout);


	int t;
	cin >> t;
	FOR(tt,0,t)
	{
		printf("Case #%d: ", tt + 1);
		FILL(A, 0);
		int n;
		cin >> n;
		if (n == 0)
		{
			cout << "INSOMNIA" << endl;
		}
		else
		{
			FOR(i,1,100000000)
			{
				Apply(1LL * n * i);
				bool ok = 1;
				FOR(j,0,10)
					ok &= A[j];
				if (ok)
				{
					cout << 1LL * i * n << endl;
					break;
				}
			}
		}
	}

	return 0;
}

