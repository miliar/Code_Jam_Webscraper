#pragma warning (disable : 4996)

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <functional>
#include <iomanip>
#include <cassert>
#include <queue>
#include <set>




using namespace std;


#define forn(i, n) for(int i = 0; i < n; ++i)
#define down(i, n) for(int i = n - 1; i >= 0; --i)



typedef long long int i64;
typedef vector<i64> vint;



const int MODULE = 1000000007;


i64 calc(vector<string> & arr)
{
	set<string> st;

	forn(i, arr.size())
	{
		string curr;
		forn(j, arr[i].length())
		{
			curr += arr[i][j];
			st.insert(curr);
		}
	}


	return st.size() + 1;
}

i64 prb(vector<string> & arr, int i, int m, int n, map<int, i64> & mp, vector<vector<string>> & mn)
{
	if (i == m)
	{
		i64 ans = 0;
		forn(j, n)
		{
			if (mn[j].size() == 0)
			{
				return 0;
			}
		}
		forn(j, n)
		{
			ans += calc(mn[j]);
		}
		mp[ans] ++;
		//mp[ans] = mp[ans] % MODULE;
		return ans;
	}
	else
	{
		i64 best = 0;
		forn(j, n)
		{
			mn[j].push_back(arr[i]);
			best = max(best, prb(arr, i + 1, m, n, mp, mn));
			mn[j].pop_back();
		}
		return best;
	}
}

int main()
{

	ios_base::sync_with_stdio(false);
	cout << fixed << setprecision(10);
#ifdef FILE_INPUT
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);

#endif
	int T;
	cin >> T;
	forn(t, T)
	{
		
		int m, n;
		cin >> m >> n;
		vector<string> arr(m);
		forn(i, m)
		{
			cin >> arr[i];
		}



		i64 ans = 0;
		map<int, i64> mp;
		vector<vector<string>> mn(n);
		ans = prb(arr, 0, m, n, mp, mn);

		
		cout << "Case #" << t + 1 << ": ";
		cout << ans << " " << mp[ans];
		cout << "\n";
	}
	return 0;
}