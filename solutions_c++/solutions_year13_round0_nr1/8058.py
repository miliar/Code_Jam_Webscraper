#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))


void proc()
{
    int i, j, x, o , t, e, isFound;
	string restr;
	char r[5][5];
	
	x = o = t = e = isFound = 0;
	FOR(i,0,3)
	{
		x = t = o = 0;
		scanf("%s", r[i]);
		FOR(j,0,3)
		{
			if (r[i][j] == 'X')
				x++;
			if (r[i][j] == 'O')
				o++;
			if (r[i][j] == 'T')
				t++;
			if (r[i][j] == '.')
				e++;
			if ((x > 0) && (o > 0))
				break;
		}
		if ((x == 4) || ((x == 3)&&(t == 1)))
		{
			isFound = 1;
			restr = "X won";
		}
		if ((o == 4) || ((o == 3)&&(t == 1)))
		{
			isFound = 1;
			restr = "O won";
		}
	}

	if (isFound == 0)
	{
		x = t = o = 0;
		FOR(i,0,3)
		{
			x = t = o = 0;
			FOR(j,0,3)
			{
				if (r[j][i] == 'X')
					x++;
				if (r[j][i] == 'O')
					o++;
				if (r[j][i] == 'T')
					t++;
				if ((x > 0) && (o > 0))
					break;
			}
			if ((x == 4) || ((x == 3)&&(t == 1)))
			{
				isFound = 1;
				restr = "X won";
			}
			if ((o == 4) || ((o == 3)&&(t == 1)))
			{
				isFound = 1;
				restr = "O won";
			}
		}
	}
	
	if (isFound == 0)
	{
		x = t = o = 0;
		FOR(j,0,3)
		{
			if (r[j][j] == 'X')
				x++;
			if (r[j][j] == 'O')
				o++;
			if (r[j][j] == 'T')
				t++;
			if ((x > 0) && (o > 0))
				break;
		}
		if ((x == 4) || ((x == 3)&&(t == 1)))
		{
			isFound = 1;
			restr = "X won";
		}
		if ((o == 4) || ((o == 3)&&(t == 1)))
		{
			isFound = 1;
			restr = "O won";
		}
	}
	
	if (isFound == 0)
	{
		x = t = o = 0;
		FOR(j,0,3)
		{
			if (r[j][3 - j] == 'X')
				x++;
			if (r[j][3 - j] == 'O')
				o++;
			if (r[j][3 - j] == 'T')
				t++;
			if ((x > 0) && (o > 0))
				break;
		}
		if ((x == 4) || ((x == 3)&&(t == 1)))
		{
			isFound = 1;
			restr = "X won";
		}
		if ((o == 4) || ((o == 3)&&(t == 1)))
		{
			isFound = 1;
			restr = "O won";
		}
	}
	if (isFound == 0)
	{
		if (e > 0)
		{
			restr = "Game has not completed";
		}
		else
		{
			restr = "Draw";
		}
	}
	static int caseNo = 0;
    cout << "Case #" << ++caseNo << ": " << restr << endl;
}

int main() {
    int nCases;
    cin >> nCases;

    for (int i = 0; i < nCases; ++i) {
        proc();
    }
}
