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
#include <functional>
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
const double Pi = acos(-1.0);

typedef long long Int;
typedef unsigned long long UINT;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 1000000000;

int n,m;

struct Rect
{
	int x1,x2,y1,y2;
	Rect(int X1, int X2 , int Y1 , int Y2) : x1(X1) , y1(Y1), x2(X2) , y2(Y2) {}
	int DLeft()
	{
		return y1;
	}
	int DRight()
	{
		return m - 1 - y2;
	}
	int Dist(Rect a)
	{
		if (max(x1,a.x1) <= min(x2,a.x2))
		{
			return min( abs(y1 - a.y2) - 1 , abs(y2 - a.y1) - 1);
		}
		if (max(y1,a.y1) <= min(y2,a.y2))
		{
			return min( abs(x1 - a.x2) - 1 , abs(x2 - a.x1) - 1);
		}

		return max( min( abs(y1 - a.y2) - 1 , abs(y2 - a.y1) - 1) , min( abs(x1 - a.x2) - 1 , abs(x2 - a.x1) - 1) );

	}
};

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	int t;
	cin >> t;   
	FOR(tt,0,t)
	{
		printf("Case #%d: " , tt + 1);
		int k;
		cin >> m >> n >> k;
		vector<Rect> a;
		FOR(i,0,k)
		{
			int X1;
			int Y1;
			int X2;
			int Y2;
			cin >> Y1 >> X1 >> Y2 >> X2;

			a.push_back(Rect(X1, X2, Y1 , Y2));
		}
		vector<int> d(k);
		vector<bool> used(k,0);
		FOR(i,0,d.size())
		{
			d[i] = a[i].DLeft();
		}

		FOR(i,0,k)
		{
			int mx = INF;
			int id;
			FOR(j,0,k)
			{
				if (!used[j] && d[j] < mx)
				{
					mx = d[j];
					id = j;
				}
			}

			used[id] = 1;
			FOR(j,0,k)
			{
				if (j != id)
				{
					int c = a[id].Dist(a[j]);
					d[j] = min(d[j] , d[id] + c);
				}
			}

		}

		int res = m;
		FOR(i,0,k)
		{
			res = min(res , d[i] + a[i].DRight());
		}

		cout << res << endl;
	}

    return 0;
}