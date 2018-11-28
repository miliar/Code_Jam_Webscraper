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
		
		int a[16];
		FILL(a,0);

		int r;
		cin >> r;
		--r;
		FOR(i,0,4)
			FOR(j,0,4)
			{
				int x;
				cin >> x;
				if (i == r)
				{
					a[x - 1]++;
				}
			}
		cin >> r;
		--r;
		FOR(i,0,4)
			FOR(j,0,4)
			{
				int x;
				cin >> x;
				if (i == r)
				{
					a[x - 1]++;
				}
			}
		vector<int> b;
		FOR(i,0,16)
			if (a[i] == 2)
				b.push_back(i + 1);
		if (b.size() == 0)
		{
			cout << "Volunteer cheated!\n";
		}
		if (b.size() == 1)
		{
			cout << b[0] << endl;
		}
		if (b.size() > 1)
		{
			cout << "Bad magician!\n";
		}
	}

	return 0;
}