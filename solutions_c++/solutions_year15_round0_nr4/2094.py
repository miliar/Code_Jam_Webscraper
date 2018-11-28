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
#include <climits>
#include <cstring>

using namespace std;

#define mp make_pair
#define pp push_back
#define Sort(x) sort(x.begin(), x.end())
#define rep(i, x, y) for(int i = x; i < y; ++i)
#define Rep(i, x, y) for(int i = x; i <= y; ++i)
#define dRep(i, x, y) for(int i = x;i >= y; --i)
#define vi vector<int>
#define vvi vector<vector<int> >
#define ll long long
#define all(v) v.begin(),v.end()
#define ii pair<int, int>
#define mem(x, v) memset(x, v, sizeof(x))
#define nl '\n'
#define MOD 1000000007

int main()
{
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("D-small-attempt2.out", "w", stdout);
	int t;
	int x, r, c;
	string winner;
	cin >> t;
	
	Rep(i, 1, t)
	{
		cin >> x >> r >> c;
		if(x == 1)
		{
			winner = "GABRIEL";
		}
		else if(x == 2)
		{
			if((r * c) % 2 == 0)
			{
				winner = "GABRIEL";
			}
			else
				winner = "RICHARD";
		}
		else if(x == 3)
		{
			if((r * c) % 3 == 0 && r >= 2 && c >= 2)
			{
				winner = "GABRIEL";
			}
			else
			{
				winner = "RICHARD";
			}
		}
		else
		{
			if((r * c) % 4 == 0 && r >= 3 && c >= 3)
				winner = "GABRIEL";
			else
				winner = "RICHARD";
		}	

		cout << "Case #" << i << ": " << winner << nl;
	}
	return 0;
}