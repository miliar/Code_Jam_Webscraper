#include <bits/stdc++.h>
#define FOR_LOOP(i, a, b) for(int i = (a); i < (b); ++i)
#define FOR_LOOP_DECREMENT(i, a, b) for(int i = (a - 1); i >= (b); --i)
#define FOR(i, n) for (int i = 0; i < (n); i++)
#define ALL(A) A.begin(), A.end()
#define MOD 100000007

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<vector<int>> matrix;

inline ll power(int a, int b) {return (ll)pow(a, b);}

/*************************************************************************/

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	FOR(i, t)
	{
		cout << "Case #" << i + 1 << ": ";
		string s;
		cin >> s;
		string _tmp;
		_tmp += s[0];
		char highest = s[0];
		for(int i = 1; i < s.size(); ++i)
		{
			if(s[i] >= highest)
			{
				highest = s[i];
				_tmp = s[i] + _tmp;
			}

			else
			{
				_tmp += s[i];
			}
		}
		cout << _tmp << endl;
	}
	
}

/*************************************************************************/