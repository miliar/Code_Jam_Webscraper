#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string.h>
#include <cassert>
#include <unordered_set>
#include <unordered_map>

#define mp make_pair
#define pb push_back
#define problem "test"
//typedef __int128 ll;
typedef long long ll;
typedef long double ld;
typedef unsigned int ui;
typedef unsigned long long ull;
const int z = 5555;
const double eps = 1e-9;
const int inf = int(1e9);
const ll llinf = ll(1e18);
using namespace std;

int lose[] = {2, 0, 1};
string s = "RPS";
int main()
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	freopen(problem".in", "r", stdin);
	freopen(problem".out", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
	    cerr << test << "\n";
		cout << "Case #" << test << ": ";
		int n, need[3], a[z], cnt[3], ok = 0;
		cin >> n >> need[0] >> need[1] >> need[2];
//		cout << need[0] << " " << need[1] << " " << need[2] << "\n"  ;
		for (int win = 0; win < 3 && !ok; win++)
		{
		    cnt[0] = cnt[1] = cnt[2] = 0;
			a[0] = win;
			for (int i = 0; i < (1 << n) - 1; i++)
				a[2 * i + 1] = a[i], a[2 * i + 2] = lose[a[i]];
			for (int i = (1 << n) - 1; i < (1 << (n + 1)) - 1; i++)
			    cnt[a[i]]++;
			ok = 1;
			for (int i = 0; i < 3; i++)
				ok &= (cnt[i] == need[i]);
			string ans;
			if (ok)
			{
				for (int i = (1 << n) - 1; i < (1 << (n + 1)) - 1; i++)
					ans += s[a[i]];
//				cout << "\nBEFORE " << ans << "\n";
				for (int i = 0; i < n; i++)
					for (int j = 0; j + (1 << i) < (1 << n); j += (1 << (i + 1)))
					{
//					    cerr << i << " " << j << " " << ans.size() << "\t" 
//					    << ans.substr(j, (1 << i)) << " " <<  ans.substr(j + (1 << i), (1 << i)) << "\n";
						if (ans.substr(j, (1 << i)) > ans.substr(j + (1 << i), (1 << i)))
						{
//							cerr << "?";
							string l = ans.substr(0, j);
							string m = ans.substr(j + (1 << i), (1 << i)) + ans.substr(j, (1 << i));
							string r = ans.substr(j + 2 * (1 << i), ans.size() - j - 2 * (1 << j));
//							cerr << l << " " << m << " " << r << "\n";
							ans = l + m + r;
						}
					}
				cout << ans;
				cout << "\n";
				break;
			}
		}
		if (!ok)
			cout << "IMPOSSIBLE\n";
	}	
	
	return 0;
}