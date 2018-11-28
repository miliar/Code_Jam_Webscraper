#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <unordered_set>

using namespace std;
typedef long long ll;
const double eps = 1e-9;
const ll mod = 1e9 + 7;



ll st = 37;

ll gethash(string str)
{
	ll ans = 0;
	ll cur = 1;
	for (int i = 0; i < str.size(); ++i)
	{
		ans += ((str[i] + 1 - 'a')*cur)%mod;
		ans %= mod;
		cur *= st;
		cur %= mod;
	}
	return ans;
}


int main(){
	freopen("C-small-attempt0 (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		int n;
		cin >> n;
		n -= 2;
		string pr1, pr2;
		unordered_set<ll> s1, s2;
		getchar();
		getline(cin, pr1);
		getline(cin, pr2);
		stringstream stream1;
		stream1 << pr1;
		string tmp;
		while (stream1 >> tmp)
		{
			s1.insert(gethash(tmp));
		}
		stringstream stream2;
		stream2 << pr2;
		while (stream2 >> tmp)
		{
			s2.insert(gethash(tmp));
		}
		
		vector < vector<ll> > v(n);
		for (int i = 0; i < n; ++i)
		{
			string cur;
			getline(cin, cur);
			stringstream stream;
			stream << cur;
			string tmp;
			while (stream >> tmp)
			{
				v[i].push_back(gethash(tmp));
			}
		}

		unordered_set<ll> all;
		for (auto it = s1.begin(); it != s1.end(); ++it)
		{
			if (s2.find(*it) != s2.end())
			{
				all.insert(*it);
			}
		}
		int ans = 1e9;
		if (n != 0)
		{
			for (int i = 0; i < (1 << n); ++i)
			{

				unordered_set<ll> cur, curans;
				for (int j = 0; j < n; ++j)
				{
					if (i & (1 << j))
					{
						for (int q = 0; q < v[j].size(); ++q)
						{
							if (s1.find(v[j][q]) == s1.end())
							{
								cur.insert(v[j][q]);
								if (s2.find(v[j][q]) != s2.end())
									curans.insert(v[j][q]);
							}
						}
					}
				}



				for (int j = 0; j < n; ++j)
				{
					if (!(i & (1 << j)))
					{
						for (int q = 0; q < v[j].size(); ++q)
						{
							ll a = v[j][q];
							if (s2.find(a) != s2.end())
							{
								continue;
							}
							else
							{
								if (cur.find(a) != cur.end() || s1.find(a) != s1.end())
								{
									curans.insert(a);
								}
							}
						}
					}
				}
				ans = min(ans, (int)curans.size());


			}
		}
		else
			ans = 0;
		ans += all.size();

		cout << "Case #" << t << ": " << ans<<"\n";

	}


	return 0;
}
/*
4
2 2
^>
^>
2 2
>v
^<
3 3
...
.^.
...
1 1
.

*/