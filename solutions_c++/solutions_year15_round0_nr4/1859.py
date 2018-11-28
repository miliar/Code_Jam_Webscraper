#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<LD> VLD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000001;
const LD EPS = 10e-9;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define abs(a) ((a)<0 ? -(a) : (a))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

int t;
int x, r, c;

int main()
{
	cin >> t;
	for(int _t = 1; _t <= t; _t++)
	{
		cin >> x >> r >> c;
		
		if(r > c)
		{
			swap(r, c);
		}
		
		string result;
		if(x == 4)
		{
			if((r == 3 && c == 4) || (r == 4 && c == 4))
			{
				result = "GABRIEL";
			}
			else
			{
				result = "RICHARD";
			}
		}
		else if(x == 3)
		{
			if((r == 2 && c == 3) || (r == 3 && c == 3) || (r == 3 && c == 4))
			{
				result = "GABRIEL";
			}
			else
			{
				result = "RICHARD";
			}
		}
		else if(x == 2)
		{
			if((r == 1 && c == 2) || (r == 1 && c == 4) || (r == 2 && c == 2) || (r == 2 && c == 3) || (r == 2 && c == 4) ||
			   (r == 3 && c == 4) || (r == 4 && c == 4) )
			{
				result = "GABRIEL";
			}
			else
			{
				result = "RICHARD";
			}
		}
		else if(x == 1)
		{
			result = "GABRIEL";
		}

		//cout << x << ' ' << r << ' ' << c << endl;
		cout << "Case #" << _t << ": " << result << endl;
	}
	return 0;
}


