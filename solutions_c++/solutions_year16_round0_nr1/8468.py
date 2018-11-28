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
#define ii pair<long long, long long>
#define mem(x, v) memset(x, v, sizeof(x))
#define nl '\n'
#define MOD 1000000007
#define readFile freopen("input.in", "r", stdin)

set<int>s;

int main()
{
	int t;
	ll n, x, temp;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> t;
	Rep(i, 1, t)
	{
		cin >> n;
		x = n;
		cout << "Case #" << i << ": ";
		if(!n)
			cout << "INSOMNIA" << nl;
		else
		{
			s.clear();
			while(s.size() < 10)
			{
				temp = x;
				while(temp)
				{
					s.insert(temp % 10);
					temp /= 10;
				}
				if(s.size() == 10)
					break;
				x += n;
			}

			cout << x << nl;
		}

	}
	return 0;
}