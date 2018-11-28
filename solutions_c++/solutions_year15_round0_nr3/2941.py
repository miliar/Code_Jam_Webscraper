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
	map<pair<char, char>, string>m;
	m[mp('i', 'i')] = "-1";
	m[mp('i', 'j')] = "k";
	m[mp('i', 'k')] = "-j";
	m[mp('j', 'i')] = "-k";
	m[mp('j', 'j')] = "-1";
	m[mp('j', 'k')] = "i";
	m[mp('k', 'i')] = "j";
	m[mp('k', 'j')] = "-i";
	m[mp('k', 'k')] = "-1";
	int t;
	int len, repeat;
	string s, temp;
	string res;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	cin >> t;
	Rep(i, 1, t)
	{
		cin >> len >> repeat;
		cin >> s;
		temp = s;
		rep(j, 0, repeat - 1)
		{
			s += temp;
		}
		int cou = 0;
		string cur = " ";
		int neg = 1;
		if(s.size() > 2)
		{
			rep(i, 0, s.size())
			{
				if(cur == " ")
					cur[0] = s[i];
				else
					cur = m[mp(cur[0], s[i])];	

				if(cur.size() > 1)
				{
					neg = -neg;
					cur[0] = cur[1];
					cur.pop_back();
					if(cur == "1")
						cur = " ";
				}

				if(!cou && cur == "i")
				{
					cou++;
					cur = " ";
				}
				else if(cou == 1 && cur == "j")
				{
					cou++;
					cur = " ";
				}
				
			}

			if(cou == 2 && cur == "k" && neg > 0) 
			{
				res = "YES";
			}
			else
			{
				res = "NO";	
			}
		}
		else
			res = "NO";
		cout << "Case #" << i << ": " << res << nl;

	}	


	return 0;
}