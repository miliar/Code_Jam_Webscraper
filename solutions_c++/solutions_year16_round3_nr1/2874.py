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
#include <unordered_map>
#include <Windows.h>

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

vector<pair<int, char> >v;

bool isValid(vector<pair<int, char> >vec, ll sum)
{
	rep(i, 0, vec.size())
	{
		if(vec[i].first * 2 > sum)
			return 0;
	}
	return 1;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t, parties, x;
	ll sum;
	vector<string>res;
	cin >> t;
	Rep(i, 1, t)
	{
		cin >> parties;
		sum = 0;
		res.clear();
		rep(j, 0, parties)
		{
			cin >> x;
			v.pp(mp(x, 'A' + j));
			sum += x;
		}

		cout << "Case #" << i <<":";
		while(sum)
		{
			Sort(v);
			while(!v[0].first)
				v.erase(v.begin());
			
			v[v.size() - 1].first -= 2;			
			if(!isValid(v, sum - 2))
			{
				v[v.size() - 1].first += 2;			
			}
			else
			{
				sum -= 2;
				cout << " " <<  v[v.size()-1].second << v[v.size()-1].second;
				continue;
			}

			v[v.size() - 2].first -= 2;			
			if(!isValid(v, sum - 2))
			{
				v[v.size() - 2].first += 2;			
			}
			else
			{
				sum -= 2;
				cout << " " <<  v[v.size()-2].second << v[v.size()-2].second;
				continue;
			}

			v[v.size() - 1].first--;			
			v[v.size() - 2].first--;
			if(!isValid(v, sum - 2))
			{
				v[v.size() - 1].first++;			
				v[v.size() - 2].first++;
			}
			else
			{
				sum -= 2;
				cout << " " <<  v[v.size()-1].second << v[v.size()-2].second;
				continue;
			}

			v[v.size() - 1].first -= 1;			
			if(!isValid(v, sum - 1))
			{
				v[v.size() - 1].first ++;			
			}
			else
			{
				sum --;
				cout << " " <<  v[v.size()-1].second;
				continue;
			}

			v[v.size() - 2].first --;			
			if(!isValid(v, sum - 1))
			{
				v[v.size() - 2].first ++;			
			}
			else
			{
				sum --;
				cout << " " <<  v[v.size()-2].second;
				continue;
			}
		}

		cout << nl;
	}
	return 0;
}