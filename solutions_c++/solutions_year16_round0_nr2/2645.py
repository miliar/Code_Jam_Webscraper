#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string.h>
#include <cassert>
#include <unordered_set>
#include <unordered_map>
#include <queue>

#define mp make_pair
#define pb push_back
#define problem "test"
typedef long long ll;
typedef long double ld;
typedef unsigned int ui;
typedef unsigned long long ull;
const int z = 1111;
const double eps = 1e-9;
const int inf = int(1e9);
const ll llinf = ll(1e18);
using namespace std;

int tests;
queue <string> q;
int n;
string bin(int x)
{
	if (!x)
		return "0";
	string res;
	while (x)
	{
		res += char(x % 2 + '0');
		x /= 2;
	}
	int sz = n - res.size();
	for (int i = 0; i < sz; i++)
		res += "0";

	reverse(res.begin(), res.end());
	return res;
}
unordered_map <string, int> d;
int main()
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	freopen(problem".in", "r", stdin);
	freopen(problem".out", "w", stdout);
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		string s;
		cin >> s;
		int tmp = s.find_last_of('-');
		if (tmp == -1)
		{
			cout << "Case #" << test << ": 0\n";
			continue;
		}
//		cout << s << " " << tmp + 1 << "\t" << s.substr(0, tmp + 1) << "\n";
		s = s.substr(0, tmp + 1);
		int ans = 0;
		while (s.find('-') != -1)
		{
			string tmp;
			int k;
			if (s[0] == '-' && s.find('+') != -1)
			{
				ans++;
				reverse(s.begin(), s.end());
				for (ui i = 0; i < s.size(); i++)
					if (s[i] == '-')
						s[i] = '+';
					else
						s[i] = '-';
			}
			if (s.find('+') == -1)
			{
				tmp = s;
				k = s.size();
			}
			else
			{
			    s = s.substr(0, s.find_last_of('-') + 1);
			    k = s.find_last_of('+');
				tmp = s.substr(0, k + 1);
			}
//			cout << "k = " << k << "\ttmp = " << tmp << "\n";
			reverse(tmp.begin(), tmp.end());
			for (ui i = 0; i < tmp.size(); i++)
				if (tmp[i] == '-')
					tmp[i] = '+';
				else
					tmp[i] = '-';
			if (k == s.size())
				s = tmp;
			else
				s = tmp + s.substr(k + 1, s.size() - k - 1);
//			cout << s << "\n";											
			ans++;
		}	
		cout << "Case #" << test << ": " << ans << "\n";
	}
	return 0;
}