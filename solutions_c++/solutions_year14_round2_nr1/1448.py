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
	vector<vector<ll> > c;
	string distinct;
	vector<string>words;
	int n;
	ll res = 0;
	ll temp;
	freopen("A-large (1).in", "r", stdin);
	//freopen("A-small-attempt2.in", "r", stdin);
	freopen("repOutLarge.txt", "w", stdout);
	cin >> t;
	Rep(i, 1, t)
	{
		cin >> n;
		words.resize(n);
		res = 0;
		/*c1.resize(n);
		c2.resize(n);*/
		rep(j, 0, n)
		{
			cin >> words[j];
		}

		distinct.clear();
		rep(j, 0, words[0].size())
		{
			if(distinct.empty() || distinct[distinct.size() - 1] != words[0][j])
				distinct += words[0][j];
		}
		c.clear();
		c.resize(n);
		rep(j, 0, n)
			c[j].resize(distinct.size(), 0);
		bool valid = true;
		rep(j, 0, n)
		{
			int index = 0;
			rep(k, 0, distinct.size())
			{
				while(index < words[j].size() && words[j][index] == distinct[k])
					c[j][k]++, index++;
			}
			if(index < words[j].size())
				valid = false;
			if(!valid)
				break;
		}

		
		ll mini = INT_MAX, maxi = INT_MIN;
		if(valid)
		rep(q, 0, distinct.size())
		{
			mini = INT_MAX, maxi = INT_MIN;
			rep(j, 0, n)
			{
				if(!c[j][q])
				{
					valid = false;
					break;
				}
				else
					mini = min(mini, c[j][q]), maxi = max(maxi, c[j][q]);
			}
			
			if(!valid)
				break;
			ll tempx = INT_MAX;
			rep(j, 0, n)
			{
				temp = 0;
				rep(k, 0, n)
				{
					temp += labs(c[k][q] - c[j][q]);
				}
				tempx = min(tempx, temp);
			}
			
			res += tempx;
		}
		
		cout << "Case #" << i << ": ";
		if(valid)
			cout << res << nl;
		else
			cout << "Fegla Won" << nl;
	}

	return 0;
}