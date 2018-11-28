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

#define FOR(i,a,b) for(int (i)=(a);i<(b);++i)
#define RFOR(i,b,a) for(int (i)=(b)-1;i>=(a);--i)
#define FILL(A,val) memset(A,val,sizeof(A))

#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define MP make_pair
#define PB push_back

typedef long long Int;
typedef unsigned long long UInt;
typedef vector<int> VI;
typedef pair<int, int> PII;

const double Pi = acos(-1.0);
const int INF = 1000000000;
const int MAX = 1000007;
const int BASE = 1000000000;
const int ST = 1000000007;

string s[27];

int R[27];
int C[27];

int popcnt[1 << 25];
bool d[1 << 25];

int F(vector<vector<int> > A)
{
	int n = SZ(A);
	if (n == 0) return 0;
	FOR(i,0,n)
		R[i] = C[i] = 0;

	FOR(i,0,1 << n)
		d[i] = 0;

	FOR(i,0,n)
	{
		FOR(j,0,n)
		{
			if (A[i][j])
			{
				R[i] |= (1 << j);
				C[j] |= (1 << i);
			}
		}
	}

	VI empty;
	FOR(j,0,n)
	{
		if (C[j] == 0)
		{
			empty.push_back(j);
		}
	}

	int MR = -1;
	int MC = -1;
	int mn = -1;

	FOR(maskR, 1 , 1 << n)
	{
		int maskC = 0;
		FOR(i,0,n)
		{
			if (maskR & (1 << i))
			{
				maskC |= R[i];
				d[maskR] |= d[maskR ^ (1 << i)];
			}
		}
		if (popcnt[maskC] > popcnt[maskR]) continue;
		int mmR = 0;
		FOR(j,0,n)
		{
			if (maskC & (1 << j))
			{
				mmR |= C[j];
			}
		}
		if ((maskR & mmR) != mmR) continue;

		int add = popcnt[maskR] - popcnt[maskC];
		if (add > SZ(empty)) continue;
		FOR(i,0,add)
		{
			maskC |= (1 << empty[i]);
		}

		if (popcnt[maskR] > mn && d[maskR] == 0)
		{
			mn = popcnt[maskR];
			MR = maskR;
			MC = maskC;
		}
		d[maskR] = 1;
	}

	vector<VI> AA;
	FOR(i,0,n)
	{
		if (MR & (1 << i)) continue;
		VI B;
		FOR(j,0,n)
		{
			if(MC & (1 << j)) continue;
			B.push_back(A[i][j]);
		}
		AA.push_back(B);
	}



	return mn * mn + F(AA);
}



int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt" , "w", stdout);

	FOR(i,1 , 1 << 25)
	{
		popcnt[i] = popcnt[i / 2] + i % 2;
	}

	int t;
	cin >> t;
	FOR(tt,0,t)
	{
		printf("Case #%d: " , tt + 1);

		int n;
		cin >> n;
		FOR(i,0,n)
		{
			cin >> s[i];
		}

		int res = 0;

		vector<VI> A(n , VI(n , 0));

		FOR(i,0,n)
		{
			FOR(j,0,n)
			{
				A[i][j] = s[i][j] - '0';
				res -= A[i][j];
			}
		}

		res += F(A);


		cerr << tt << ' ' << res << endl;
		printf("%d\n" , res);

	}

	//cout << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	return 0;
}
