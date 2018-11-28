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

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define RFOR(i,b,a) for(int i=(b)-1;i>=(a);--i)
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

string F[13][3];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt" , "w", stdout);

	F[0][0] = "R";
	F[0][1] = "P";
	F[0][2] = "S";
	FOR(i,1,12)
	{
		FOR(j,0,3)
		{
			string s1 = F[i - 1][j];
			string s2 = F[i - 1][(j + 2) % 3];
			if (s1 > s2) swap(s1 , s2);
			F[i][j] = s1 + s2;
		}
	}

	int t;
	cin >> t;
	FOR(tt,0,t)
	{
		printf("Case #%d: " , tt + 1);
		int n, r , p , s;
		cin >> n >> r >> p >> s;
		string res = "Z";
		FOR(j,0,3)
		{
			int cr = 0;
			int cp = 0;
			int cs = 0;
			FOR(k,0,SZ(F[n][j]))
			{
				if (F[n][j][k] == 'R') ++cr;
				if (F[n][j][k] == 'P') ++cp;
				if (F[n][j][k] == 'S') ++cs;
			}
			if (cr == r && cp == p && cs == s)
			{
				res = min(res , F[n][j]);
			}
		}
		if (res == "Z")
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << res << endl;
		}
	}

	//cout << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	return 0;
}
