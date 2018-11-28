#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <ctime>
#include <sstream>
#include <vector>
#include <string.h>
using namespace std;
#define NN 100000
#define ll long long
#define pii pair<int,int>

struct str
{
	int x, y, k;
	str(int _x = 0, int _y = 0, int _k = 0)
	{
		x = _x;
		y = _y;
		k = _k;
	}
	bool operator<(const str &two)const
	{
		if(x != two.x)
			return x < two.x;
		if(y != two.y)
			return y < two.y;
		return k < two.k;
	}
	bool operator==(const str &two)const
	{
		if(x == two.x && y == two.y && k == two.k)
			return true;
		return false;
	}
};

int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
			//   N	     E	     S	      W
string mehdi = "NESW";

map <str, pii> dp;
str q[1000000];
str par[1000000];
pii res[1024];

int main()
{
	int t;
	int XX, YY;
	int L, R;
	string s;
	str e;
	
	cin >> t;
	for(int cas = 1; cas <= t; cas ++)
	{
		cin >> XX >> YY;
		
		dp.clear();
		L = R = 0;
		q[R ++] = str(0, 0, 1);
		int r, c;
		int n = 0;
		while(L < R)
		{
			e = q[L ++];
			if(e.x == XX && e.y == YY)
			{
				// cout << "HELLO " << e.k << endl;
				while( e.k != 1 )
				{
					// cout << e.x << " " << e.y << endl;
					res[n ++] = pii(e.x, e.y);
					r = dp[e].first;
					c = dp[e].second;
					e.x = r;
					e.y = c;
					e.k --;
				}
				res[n ++] = pii(0, 0);
				// cout << "HERE " << n << endl;
				// cout << e.x << " " << e.y << endl;
				break;
			}
			if(e.k > 500)
				continue;
				
			for(int h = 0; h < 4; h ++)
			{
				int x = dir[h][0] * e.k + e.x;
				int y = dir[h][1] * e.k + e.y;
				
				if( !dp.count( str(x, y, e.k+1) ) )
				{
					// dp.insert( str(x, y, e.k+1) );
					dp[ str(x, y, e.k+1) ] = pii(e.x, e.y);
					q[R ++] = str(x, y, e.k+1);
				}
			}
		}
		
		s = "";
		reverse(res, res+n);
		// cout << "HERE " << n << endl;
		for(int i = 1; i < n; i ++)
		{
			// cout << res[i].first << " " << res[i].second << endl;
			if(res[i].first == res[i-1].first)	// x sabet moonde
			{
				if(res[i].second > res[i-1].second)	// y ezafe shode
					s += 'N';
				else
					s += 'S';
			}
			else		// res[i].second == res[i-1].second		// y sabet moonde
			{
				if(res[i].first > res[i-1].first)
					s += 'E';
				else
					s += 'W';
			}
		}
		cout << "Case #" << cas << ": " << s << endl;
	}
	
	return 0;
}