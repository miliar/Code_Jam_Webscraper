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
#include <time.h>
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

const int MAX = 7000000;
const Int BASE = 1000000007;

const int MOD = 1000000009;


int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	
	int t;
	cin >> t;
	FOR(ttt,0,t)
	{
		printf("Case #%d: " , ttt + 1);
		
		double c,f,x;
		cin >> c >> f >> x;
		double time = 0.0;
		double res = x / 2;
		double persec = 2;
		int steps = 0;
		while (1)
		{
			time += c / persec;
			persec += f;
			if (time + x / persec > res)
				break;
			else
				res = time + x / persec;
			++steps;
		}

		printf("%.8f\n" , res);
		cerr << steps << endl;

	}

	return 0;
}