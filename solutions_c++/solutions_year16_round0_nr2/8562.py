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



int main()
{
	
	int t;
	string s;
	ll flips;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> t;
	Rep(i, 1, t)
	{
		cin >> s;
		cout << "Case #" << i << ": ";
		flips = 0;
		if(s == string(s.size(), '+'))
		{
			flips = 0;
		}
		else if(s == string(s.size(), '-'))
		{
			flips = 1;
		}
		else
		{
			while(s != string(s.size(), '+'))
			{
				int i = 0;
				if(s[0] == '-')
				{
					flips++;
					while(i < s.size() && s[i] == '-')
						s[i] = '+', i++;
				}
				else
				{
					flips += 2;
					string reversed;
					while(i < s.size() && s[i] == '+')
						s[i] = '-', i++;
					for(int j = s.size() - 1; j >= 0; j--)
					{
						if(s[j] == '-')
						{
							reversed = s.substr(0, j + 1);
							break;
						}
					}

					reverse(all(reversed));
					rep(x, 0, reversed.size())
					{
						if(reversed[x] == '+')
							reversed[x] = '-';
						else
							reversed[x] = '+';
					}
					rep(x, 0, reversed.size())
						s[x] = reversed[x];
				}

			}


		}
		cout << flips << nl;




	}
	return 0;
}