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

vector<vector<int> > b;

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	
	FOR(i1,2,6)
		FOR(i2,i1,i1 + 1)
			FOR(i3,0,i2 + 1)
				FOR(i4,0,i3 + 1)
					FOR(i5,0,i4 + 1)
						if (i3 != 1 && i4 != 1 && i5 != 1)
						{
							vector<int> c;
							c.push_back(i1);
							c.push_back(i2);
							c.push_back(i3);
							c.push_back(i4);
							c.push_back(i5);
							b.push_back(c);
						}

	int t;
	cin >> t;
	FOR(ttt,0,t)
	{
		printf("Case #%d:\n" , ttt + 1);
		
		int r,c,m;
		cin >> r >> c >> m;

		if (r == 1)
		{
			cout << 'c';
			FOR(i,0,r * c - m - 1)
				cout << '.';
			FOR(i,0,m)
				cout << '*';
			cout << endl;
			continue;
		}
		if (c == 1)
		{
			cout << 'c' << endl;
			FOR(i,0,r * c - m - 1)
				cout << '.' << endl;
			FOR(i,0,m)
				cout << '*' << endl;
			continue;
		}

		if (r * c - m == 1)
		{
			char A[6][6];
			FOR(i,0,r)
				FOR(j,0,c)
					A[i][j] = '*';
			A[0][0] = 'c';
			FOR(i,0,r)
			{
				FOR(j,0,c)
					cout << A[i][j];
				cout << endl;
			}
			continue;
		}

		bool found = false;

		FOR(I,0,b.size())
		{
			bool ok = true;
			int t = 0;
			FOR(j,0,r)
				if (b[I][j] > c)
					ok = false;
				else t += b[I][j];
			if (t == r * c - m && ok)
			{
				found = true;
				char A[6][6];
				FOR(i,0,r)
					FOR(j,0,c)
						A[i][j] = '*';
				
				FOR(i,0,r)
					FOR(j,0,b[I][i])
						A[i][j] = '.';
				A[0][0] = 'c';

				FOR(i,0,r)
				{
					FOR(j,0,c)
						cout << A[i][j];
					cout << endl;
				}
				break;
			}
		}
		if (!found)
		{
			cout << "Impossible\n";
		}

	}

	return 0;
}