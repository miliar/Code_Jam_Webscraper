#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
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
#define rep(i, x, y) for(int i = x; i < y; i++)
#define Rep(i, x, y) for(int i = x; i <= y; i++)
#define vi vector<int>
#define vvi vector<vector<int> >
#define ll long long
#define all(v) v.begin(),v.end()
#define ii pair<int, int>
#define mem(x, v) memset(x, v, sizeof(x))
#define nl '\n'

int main()
{
	int t;
	double rate, extra, target, cost;
	double timee;
	bool ended;
	freopen("B-large.in", "r", stdin);
	freopen("cookie.txt", "w", stdout);
	cin >> t;
	Rep(i, 1, t)
	{
		cin >> cost >> extra >> target;
		ended = false;
		rate = 2;
		timee = 0;
		while(!ended)
		{
			if(target / rate > cost / rate + target/(rate + extra))
			{
				timee += cost / rate;
				rate += extra;
			}
			else
			{
				timee += target / rate;
				ended = true;
			}
		}
		cout << "Case #" << i << ": ";
		cout << setprecision(7) << fixed << timee << nl;
	}

	return 0;
}

