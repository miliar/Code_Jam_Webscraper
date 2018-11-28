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
	int t;
	int W, R, C;
	int res;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> t;
	Rep(i, 1, t)
	{
		res = 0;
		cin >> R >> C >> W;
		/*for(int j = W - 1; j < C; )
		{
		if(j + W < C)
		{
		res++, j += W;
		}
		else
		{
		if(j < C - 1)
		{
		res += W + 1;
		}
		else
		{
		res += W;
		}

		break;
		}
		}*/
		for(int j = 0; j < R; j++)
		{
			for(int k = W - 1; k < C; k += W)
			{
				if(k + W < C || j < R - 1)
				{
					res++;
				}
				else
				{
					if(k == C - 1)
					{
						res += W;
					}
					else
					{
						res += W + 1;
					}

					break;
				}
			}	
		}

		cout << "Case #" << i <<": " << res <<nl;
	}
	return 0;
}


